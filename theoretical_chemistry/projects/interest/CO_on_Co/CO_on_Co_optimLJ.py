from ase import Atoms
from ase.build import bulk
from ase.optimize import LBFGS
from ase.build import fcc111, hcp0001, molecule, add_adsorbate
from ase.filters import ExpCellFilter, StrainFilter
from ase.calculators.emt import EMT
from ase.calculators.lj import LennardJones


def get_opt_energy(atoms, fmax=0.001, opt_mode: str = "normal"):
# LJ parameters
    lj_epsilon = 0.01
    lj_sigma = 2.5
    calculator = LennardJones(epsilon=lj_epsilon, sigma=lj_sigma, rc=10.0)
    atoms.set_calculator(calculator)
    if opt_mode == "scale":
        opt1 = LBFGS(StrainFilter(atoms, mask=[1, 1, 1, 0, 0, 0]))
    elif opt_mode == "all":
        opt1 = LBFGS(ExpCellFilter(atoms))
    else:
        opt1 = LBFGS(atoms)
    opt1.run(fmax=fmax)
    return atoms.get_total_energy()

# First, the Co structure is prepared using the bulk, and the appropriate cell size is found by optimizing the cell size.

# LJ parameters
lj_epsilon = 0.01
lj_sigma = 2.5

bulk_atoms = bulk("Co")
bulk_atoms.cell

bulk_atoms = bulk("Co")
calculator = LennardJones(epsilon=lj_epsilon, sigma=lj_sigma, rc=10.0)
bulk_atoms.calc = calculator
E_bulk = get_opt_energy(bulk_atoms, fmax=1e-4, opt_mode="scale")








