from rdkit import Chem
from rdkit.Chem import Draw

mol = Chem.MolFromSmiles('c1ccccc1C(=O)O') # Benzoic acid

# Create drawing options
drawer = Draw.MolDraw2DCairo(400, 300) # For PNG output
options = drawer.drawOptions()
options.bondLineWidth = 2
options.atomLabelFontSize = 18
drawer.drawOptions = options

# Draw the molecule with highlights and options
drawer.DrawMolecule(mol, highlightAtoms=[0, 6])
drawer.FinishDrawing()
drawer.WriteDrawingText('benzoic_acid_highlighted.png')
