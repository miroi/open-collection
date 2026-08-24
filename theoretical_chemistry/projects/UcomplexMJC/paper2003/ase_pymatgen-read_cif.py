from pymatgen.core import Structure
from ase import Atoms
from ase.io import write

# Read with pymatgen
structure = Structure.from_file('ja030260r_2.cif')

# Convert to ASE Atoms object
atoms = Atoms(
    symbols=structure.species,
    positions=structure.cart_coords,
    cell=structure.lattice.matrix,
    pbc=True
)

print(f"Number of atoms: {len(atoms)}")
print(f"Chemical formula: {atoms.get_chemical_formula()}")
print(f"Cell: {atoms.cell}")
