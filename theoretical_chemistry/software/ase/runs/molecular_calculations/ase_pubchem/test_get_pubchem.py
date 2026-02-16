
from ase.build import molecule
from ase import Atoms
from ase.collections import g2
from ase.visualize import view

from ase.data.pubchem import pubchem_atoms_search, pubchem_atoms_conformer_search


# Search for acetic acid by name
#atoms = pubchem_atoms_search(search="acetic acid", field="name")
#atoms = pubchem_atoms_search(name='acetic acid')
atoms = pubchem_atoms_search(name='cumene')

