# https://wiki.fysik.dtu.dk/ase/ase/calculators/kim.html

from ase.lattice.cubic import FaceCenteredCubic
from ase.calculators.kim.kim import KIM

a=5.25
atoms = FaceCenteredCubic(symbol='Ar', latticeconstant=a, size=(1,1,1))
calc = KIM("ex_model_Ar_P_Morse_07C")
atoms.calc = calc

energy = atoms.get_potential_energy()
print("Potential energy of FCC Ar: {} eV".format(energy))
