import warnings
warnings.filterwarnings("ignore", message="Module .* is under testing")

import numpy as np
from ase.build import molecule
from ase.calculators.calculator import Calculator, all_changes
from ase.optimize import BFGS
from ase.units import Hartree, Bohr
from pyscf import gto, dft

# 1. Lightweight ASE Calculator wrapper for core PySCF RKS
class PySCFRKSCalculator(Calculator):
    implemented_properties = ["energy", "forces"]

    def __init__(self, xc="b3lyp", basis="aug-cc-pVTZ", grid_level=4, **kwargs):
        super().__init__(**kwargs)
        self.xc = xc
        self.basis = basis
        self.grid_level = grid_level
        self.mf = None

    def calculate(self, atoms=None, properties=("energy",), system_changes=all_changes):
        super().calculate(atoms, properties, system_changes)
        mol = gto.Mole()
        mol.atom = [
            (sym, pos)
            for sym, pos in zip(self.atoms.get_chemical_symbols(), self.atoms.get_positions())
        ]
        mol.basis = self.basis
        mol.charge = 0
        mol.spin = 0
        mol.verbose = 0
        mol.build()

        mf = dft.RKS(mol)
        mf.xc = self.xc
        mf.grids.level = self.grid_level
        e_ha = mf.kernel()
        self.mf = mf
        self.results["energy"] = float(e_ha * Hartree)

        if "forces" in properties:
            grad_ha_bohr = mf.nuc_grad_method().kernel()
            self.results["forces"] = -grad_ha_bohr * (Hartree / Bohr)

# 2. Analytical GIAO Molecular Magnetizability (with nocc=1 fix for pyscf-properties 0.1.0)
def compute_giao_magnetizability(mf):
    """Compute exact 3x3 GIAO magnetizability tensor (in a.u.)."""
    from pyscf.prop.magnetizability import rks as mag_rks
    import pyscf.prop.nmr.rhf as rhf_nmr

    orig_solve_mo1 = rhf_nmr.solve_mo1

    def patched_solve_mo1(nmrobj, mo_energy, mo_coeff, mo_occ, h1, s1, with_cphf=True):
        nocc = int(np.sum(mo_occ > 0))
        if nocc > 1:
            return orig_solve_mo1(nmrobj, mo_energy, mo_coeff, mo_occ, h1, s1, with_cphf)

        nmo = len(mo_energy)
        occidx = mo_occ > 0
        viridx = mo_occ == 0
        e_a = mo_energy[viridx]
        e_i = mo_energy[occidx]
        e_ai = 1.0 / (e_a[:, None] - e_i[None, :])  # (nvir, 1)

        mo1 = np.zeros((3, nmo, 1))
        mo1[:, occidx, :] = -0.5 * s1[:, occidx, :]
        rhs = h1[:, viridx, :] - s1[:, viridx, :] * e_i[None, None, :]
        mo1[:, viridx, :] = -rhs * e_ai[None, :, :]

        if with_cphf:
            vresp = nmrobj._scf.gen_response(singlet=False, hermi=2)

            def fvind(x_vir):
                x_3d = x_vir.reshape(3, -1, 1)  # shape (3, nvir, 1)
                dm1 = np.einsum("xai,pa,qi->xpq", x_3d, mo_coeff[:, viridx], mo_coeff[:, occidx])
                dm1 = dm1 - dm1.transpose(0, 2, 1)
                v1 = vresp(dm1)
                v_ai = np.einsum("xpq,pa,qi->xai", v1, mo_coeff[:, viridx], mo_coeff[:, occidx])
                return -(v_ai * e_ai[None, :, :]).reshape(-1)

            rhs_vec = mo1[:, viridx, :].reshape(-1)
            x_cur = rhs_vec.copy()
            for _ in range(30):
                x_next = rhs_vec + fvind(x_cur)
                if np.linalg.norm(x_next - x_cur) < 1e-11:
                    x_cur = x_next
                    break
                x_cur = x_next
            mo1[:, viridx, :] = x_cur.reshape(3, -1, 1)

        mo_e1 = h1[:, occidx, :] - s1[:, occidx, :] * e_i[None, None, :]
        return mo1, mo_e1

    rhf_nmr.solve_mo1 = patched_solve_mo1
    try:
        mag_obj = mag_rks.Magnetizability(mf)
        mag_obj.verbose = 0
        chi_au = mag_obj.kernel()
    finally:
        rhf_nmr.solve_mo1 = orig_solve_mo1
    return chi_au

# 3. Configure DFT functional and augmented triple-zeta basis set
xc_func = "b3lyp"
basis_set = "aug-cc-pVTZ"

# Exact CODATA unit conversion factors from atomic units (e^2 a0^2 / m_e)
AU_TO_J_T2 = 7.8910366e-29      # 1 a.u. = 78.910366 x 10^-30 J/T^2
AU_TO_CM3_MOL = 4.751991e-6     # 1 a.u. = 4.751991 x 10^-6 cm^3/mol (cgs-emu molar susceptibility)

print("=== ASE + PySCF GIAO Molecular Magnetizability Calculation ===")
print(f"Functional / Basis : {xc_func.upper()} / {basis_set}")
print("Target Molecule    : H2 (simplest closed-shell diamagnetic molecule)")

# 4. Optimize H2 geometry with ASE BFGS + PySCF
h2_atoms = molecule("H2")
h2_atoms.pbc = False
calc = PySCFRKSCalculator(xc=xc_func, basis=basis_set, grid_level=4)
h2_atoms.calc = calc

opt = BFGS(h2_atoms, logfile=None)
opt.run(fmax=0.001)

e_opt = h2_atoms.get_potential_energy()
d_hh = h2_atoms.get_distance(0, 1)

# 5. Compute analytical GIAO magnetizability tensor (3x3 in a.u.)
chi_tensor_au = compute_giao_magnetizability(calc.mf)
chi_iso_au = float(np.trace(chi_tensor_au) / 3.0)

# Principal components (two degenerate perpendicular, one parallel to H-H axis)
eigs = np.sort(np.linalg.eigvalsh(chi_tensor_au))
if abs(eigs[0] - eigs[1]) < abs(eigs[1] - eigs[2]):
    chi_perp_au = 0.5 * (eigs[0] + eigs[1])
    chi_par_au = eigs[2]
else:
    chi_perp_au = 0.5 * (eigs[1] + eigs[2])
    chi_par_au = eigs[0]
aniso_au = float(chi_par_au - chi_perp_au)

chi_iso_si = chi_iso_au * AU_TO_J_T2 * 1e30        # in 10^-30 J/T^2
chi_iso_cgs = chi_iso_au * AU_TO_CM3_MOL * 1e6     # in 10^-6 cm^3/mol

print(f"\n[H2] BFGS steps={opt.nsteps} | E_opt={e_opt:.6f} eV | r(H-H)={d_hh:.4f} A")
print("\n=== GIAO Molecular Magnetizability Summary for H2 ===")
print(f"Isotropic chi_iso (a.u.)     : {chi_iso_au:+8.4f} a.u.             (Expt: -0.847 a.u.)")
print(f"Isotropic chi_iso (SI)       : {chi_iso_si:+8.3f} x 10^-30 J/T^2   (Expt: -6.68 x 10^-30 J/T^2)")
print(f"Molar Susceptibility chi_M   : {chi_iso_cgs:+8.3f} x 10^-6 cm^3/mol (Expt: -4.02 x 10^-6 cm^3/mol)")
print(f"Magnetizability Anisotropy   : {aniso_au:+8.4f} a.u.             (Expt: +0.114 a.u.)")

