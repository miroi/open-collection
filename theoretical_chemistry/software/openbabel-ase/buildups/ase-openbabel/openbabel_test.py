from openbabel import openbabel

# Initialize an empty molecule
mol = openbabel.OBMol()

# Add a Carbon atom
atom1 = mol.NewAtom()
atom1.SetAtomicNum(6)  # 6 is Carbon
atom1.SetVector(0.0, 0.0, 0.0)

# Add another Carbon atom
atom2 = mol.NewAtom()
atom2.SetAtomicNum(6)
atom2.SetVector(1.5, 0.0, 0.0)

# Add a single bond between atom 1 and 2
mol.AddBond(1, 2, 1)

print(f"Number of Atoms: {mol.NumAtoms()}")
print(f"Number of Bonds: {mol.NumBonds()}")

