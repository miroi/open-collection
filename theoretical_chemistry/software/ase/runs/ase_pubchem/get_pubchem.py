
from ase.data.pubchem import pubchem_atoms_search, pubchem_atoms_conformer_search


# Search for acetic acid by name
#atoms = pubchem_atoms_search(name="acetic acid")

cumene = pubchem_atoms_search(name='cumene')
benzene = pubchem_atoms_search(cid=241)
#ethanol = pubchem_atoms_search(smiles='CCOH')
octane_conformers = pubchem_atoms_conformer_search(name='octane')



# If successful, atoms will be an Atoms object containing the structure of acetic acid
if cumene:
    print(cumene.get_chemical_formula())
    print(cumene.get_positions())
    # You can also access other properties like
    # atoms.get_masses(), atoms.get_positions(), etc.

# Search for a compound by CID
#atoms_cid = pubchem_atoms_search(search="579", field="CID")

# Search for a compound by SMILES string
#atoms_smiles = pubchem_atoms_search(search="CC(=O)O", field="smiles")


