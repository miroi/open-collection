from mace.calculators import mace_mp
from ase import build

macemp = mace_mp() # return ASE calculator
atoms = build.molecule('H2O')
descriptors_mp = macemp.get_descriptors(atoms)
print(atoms)
