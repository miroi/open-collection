

from rdkit import Chem
from rdkit.Chem import Draw

# Create a molecule object from a SMILES string
mol = Chem.MolFromSmiles('CCO') # Ethanol

#print(mol)

# Draw the molecule and save it as a PNG image

#Chem.Draw.MolToImageFile(mol, 'ethanol.png')
#Chem.Draw.MolToImage(mol, 'ethanol.png')

img = Draw.MolToImage(mol)
img = Draw.MolToImageFile(mol,'ethanol.png')
