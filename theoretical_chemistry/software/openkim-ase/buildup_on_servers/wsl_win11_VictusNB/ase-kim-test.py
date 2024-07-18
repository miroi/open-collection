#
# https://wiki.fysik.dtu.dk/ase/ase/calculators/kim.html#overview
#

# As an example, suppose we want to know the potential energy predicted by the example model “ex_model_Ar_P_Morse_07C” 
# for an FCC argon lattice at a lattice spacing of 5.25 Angstroms.  
# This can be accomplished in a manner similar to how most other ASE calculators are used, 
# where the name of the KIM model is passed as an argument:
#

from ase.lattice.cubic import FaceCenteredCubic
from ase.calculators.kim.kim import KIM

atoms = FaceCenteredCubic(symbol='Ar', latticeconstant=5.25, size=(1,1,1))
calc = KIM("ex_model_Ar_P_Morse_07C")
atoms.calc = calc

energy = atoms.get_potential_energy()
print("Potential energy: {} eV".format(energy))
