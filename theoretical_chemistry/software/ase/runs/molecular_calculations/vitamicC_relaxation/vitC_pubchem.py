from ase.data.pubchem import pubchem_atoms_search
from ase.visualize import view
from ase.io import write

# 1. Download the structure of Vitamin C (L-ascorbic acid)
# You can search by name, CID (54670067), or SMILES

#atoms = pubchem_atoms_search(name='ascorbic acid') # this does not work
atoms = pubchem_atoms_search(cid=54670067)

# 2. Print basic information
print(f"Formula: {atoms.get_chemical_formula()}")
print(f"Number of atoms: {len(atoms)}")

# 3. Save the structure to a file (e.g., XYZ or PDB format)
xyzfile='vitamin_c.xyz'
write(xyzfile, atoms)
print(xyzfile, " structure file saved .")


# 4. (Optional) Open the ASE visualizer to see the molecule
# view(atoms)

