
#
# from Google AI: openbabel-wheel show force field use
#

from openbabel import openbabel as ob
from openbabel import pybel

from ase import Atoms
from ase.visualize import view

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

#mol.makefields("mmff94")
# This calculates energy without moving atoms
mol.localopt(forcefield="mmff94", steps=0)

print(f"Energy: {mol.energy} kJ/mol")

ff = pybel._forcefields["mmff94"]
success = ff.Setup(mol.OBMol)
if success:
    print(f"success Energy: {ff.Energy()} kJ/mol")

print(f"Energy before optimization: {mol.energy:.4f} kJ/mol")

# 2. Initialize the force field (e.g., mmff94, uff, gaff)
#mol.makefields("mmff94")

# 3. Access the energy property (result is in kJ/mol)
print(f"Total Energy: {mol.energy:.4f} kJ/mol")
# some prints a

print(mol.atoms[0].type)
print(pybel.informats.keys())

print(mol.atoms[0].coords)
mol.localopt(forcefield="mmff94", steps=500)
print(mol.atoms[0].coords)


# Create and set up the force field
#ff = ob.OBForceField.FindForceField("uff") # Options: uff, mmff94, gaff, ghemical
# 3. Setup the force field (e.g., "mmff94", "uff", or "gaff")
# This initializes the force field for this specific molecule

mol.localopt(forcefield="mmff94", steps=500)
print(f"Energy after optimization: {mol.energy:.4f} kJ/mol")

success = ff.Setup(mol.OBMol)
if success:
    print(f"success 2 Energy: {ff.Energy()} kJ/mol")

#mol = pybel.readstring("smi", "C1=NC2=C(N1)C(=NC=N2)N") # Adenine
mol.draw(show=True, filename=None)

def pybel_to_ase(mol):
    # 1. Get atomic numbers
    numbers = [a.atomicnum for a in mol.atoms]
    # 2. Get 3D coordinates
    coords = [a.coords for a in mol.atoms]
    # 3. Create ASE Atoms object
    return Atoms(numbers=numbers, positions=coords)

# Convert
ase_mol = pybel_to_ase(mol)

# Display
# This opens a separate GUI window (ase-gui)
view(ase_mol)

#if ff.Setup(obmol):
    # Perform energy minimization
#    ff.ConjugateGradients(100) # 100 steps
#    ff.GetCoordinates(obmol) # Update coordinates
    
    # Save the optimized molecule
#    new_mol = pybel.Molecule(obmol)
#    new_mol.write("xyz", "molecule_min.xyz", overwrite=True)
#else:
#    print("Force field setup failed")


