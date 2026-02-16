
from openbabel import pybel

# Create a molecule object from a SMILES string (e.g., Benzene)
smiles = "c1ccccc1"
mol = pybel.readstring("smi", smiles)

# Calculate molecular weight
print(f"Molecular Weight: {mol.molwt:.2f}")

# Convert to another format (e.g., InChI)
inchi = mol.write("inchi").strip()
print(f"InChI: {inchi}")

# Save to a file (SDF format)
mol.write("sdf", "molecule.sdf", overwrite=True)


