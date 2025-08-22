from dftd4.parameters import get_damping_param
from dftd4.ase import DFTD4
from ase.build import molecule

# Get default params and tweak s6
params_tweaks = {'s6': 0.8}

# Setup calculator
d4calc = DFTD4(method="PBE", params_tweaks=params_tweaks, verbose=True)

# Build molecule
atoms = molecule('H2O')
atoms.calc = d4calc

print("Tweaked parameters:", d4calc.parameters)
energy = atoms.get_potential_energy()
print("DFT-D4 energy with s6=0.8:", energy)