from ase.io import read

# Read the CIF file
atoms = read('ja030260r_2.cif')

# Explore the structure
print(f"Number of atoms: {len(atoms)}")
print(f"Chemical formula: {atoms.get_chemical_formula()}")
print(f"Cell parameters:\n{atoms.cell}")
print(f"Atomic positions:\n{atoms.get_positions()}")
print(f"Atomic numbers: {atoms.get_atomic_numbers()}")
print(f"Chemical symbols: {atoms.get_chemical_symbols()}")


