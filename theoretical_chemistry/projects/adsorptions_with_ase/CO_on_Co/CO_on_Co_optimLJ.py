from ase import Atoms
from ase.build import bulk
from ase.optimize import LBFGS
from ase.build import fcc111, hcp0001, molecule, add_adsorbate
from ase.filters import ExpCellFilter, StrainFilter
from ase.calculators.emt import EMT
from ase.calculators.lj import LennardJones

# Set up the LJ calculator
lj_epsilon = 0.01
lj_sigma = 2.5
calculator = LennardJones(epsilon=lj_epsilon, sigma=lj_sigma, rc=10.0)

def get_opt_energy(atoms, fmax=0.001, opt_mode: str = "normal"):
    atoms.calc = calculator
    print("get_opt_energy: opt_mode=",opt_mode)
    if opt_mode == "scale":
        opt1 = LBFGS(StrainFilter(atoms, mask=[1, 1, 1, 0, 0, 0]))
    elif opt_mode == "all":
        opt1 = LBFGS(ExpCellFilter(atoms))
    else:
        opt1 = LBFGS(atoms)
    opt1.run(fmax=fmax)
    return atoms.get_total_energy()

# First, the Co structure is prepared using the bulk, and the appropriate cell size is found by optimizing the cell size.

bulk_atoms = bulk("Co")
bulk_atoms.cell
print("Co bulk before optimization :",bulk_atoms.cell)

bulk_atoms = bulk("Co")
bulk_atoms.calc = calculator
E_bulk = get_opt_energy(bulk_atoms, fmax=1e-4, opt_mode="scale")
print("CO bulk after optimization:",bulk_atoms.cell)

#  Set lattice parameter from bulk cell
a = bulk_atoms.cell[0,0]
c = bulk_atoms.cell[2,2]

print("bulk cell lattice parameters a=",a," c=",c)
# You can see a slight change in value from the ASE default of a = 2.51A.

# We will use this cell size to create the adsorption structure below
slab =  hcp0001("Co", size=(4, 4, 4), a=a, c=c, vacuum=40.0, periodic=True)
slab.calc = calculator

E_slab = get_opt_energy(slab, fmax=1e-4, opt_mode="normal")

# set up the molecule
mol = molecule("CO")
mol.calc = calculator

E_mol = get_opt_energy(mol, fmax=1e-4)

# Creating adsorption structures
slab_mol =  hcp0001("Co", size=(4, 4, 4), a=a, c=c, vacuum=40.0, periodic=True)
mol2 = molecule("CO")
add_adsorbate(slab_mol, mol2, 3.0, "bridge")

E_slab_mol = get_opt_energy(slab_mol, fmax=1e-2)

# Compute adsorption energy:
E_adsorp = E_slab_mol - (E_slab + E_mol)

print(f"E_adsorp {E_adsorp}, E_slab_mol {E_slab_mol}, E_slab {E_slab}, E_mol {E_mol}")

# From https://docs.matlantis.com/atomistic-simulation-tutorial/en/3_3_slab_adsorption_energy.html#CO-on-Pd :
# An adsorption energy of -1.55 eV was obtained 

# visualize
# ...

