
from rdkit import Chem
from rdkit.Chem import Draw

# Create a molecule object from a SMILES string
mol = Chem.MolFromSmiles('CCO')

# Generate a PIL Image object from the molecule
img = Draw.MolToImage(mol)

# Save the image to a file (e.g., as a PNG)
img.save('ethanol.png')
