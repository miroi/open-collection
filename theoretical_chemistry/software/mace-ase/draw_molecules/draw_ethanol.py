from rdkit import Chem
from rdkit.Chem import Draw

# Create a molecule object from a SMILES string
mol = Chem.MolFromSmiles('CCO') # Ethanol

# Draw the molecule and save it as a PNG image
Draw.MolToImageFile(mol, 'ethanol.png')
