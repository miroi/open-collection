
#
# from Google AI: openbabel-wheel show force field use
#

from openbabel import openbabel as ob
from openbabel import pybel

# List available force fields
print("\n pybel FFs :",pybel.forcefields)

# does not work
#print("List of force-fields:", ob.OBPlugin.List("forcefields"))

# Load a molecule from a file (e.g., mol.pdb)
#mol = next(pybel.readfile("pdb", "molecule.pdb"))
#mol =  pybel.readstring("smi",'C1=CC=CC=C1')

mol = pybel.readstring("smi", "O")
mol.addh()

mol.make3D()

mol.write("xyz", "water.xyz", overwrite=True)

# some prints 
print(mol.atoms[0].type)
print(pybel.informats.keys())

print(mol.atoms[0].coords)
mol.localopt(forcefield="gaff", steps=500)
print(mol.atoms[0].coords)


# Create and set up the force field
#ff = ob.OBForceField.FindForceField("uff") # Options: uff, mmff94, gaff, ghemical
# 3. Setup the force field (e.g., "mmff94", "uff", or "gaff")
# This initializes the force field for this specific molecule

mol.localopt(forcefield="gaff", steps=500)
print(f"Energy after optimization: {mol.energy:.4f} kJ/mol")

#success = mol.makefields("mmff94")
success = mol.make3D("uff", steps=50)

if success:
    # 4. Calculate and print energy (typically in kJ/mol)
    print(f"Total Energy: {mol.energy:.4f} kJ/mol")
else:
    print("Force field setup failed. Check if the molecule has valid 3D coordinates.")



#if ff.Setup(obmol):
    # Perform energy minimization
#    ff.ConjugateGradients(100) # 100 steps
#    ff.GetCoordinates(obmol) # Update coordinates
    
    # Save the optimized molecule
#    new_mol = pybel.Molecule(obmol)
#    new_mol.write("xyz", "molecule_min.xyz", overwrite=True)
#else:
#    print("Force field setup failed")


