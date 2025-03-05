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

#atoms = FaceCenteredCubic(symbol='Ar', latticeconstant=5.25, size=(1,1,1))
#atoms = FaceCenteredCubic(symbol='Og', latticeconstant=5.25, size=(1,1,1))
atoms = FaceCenteredCubic(symbol='Og', latticeconstant=5.25, size=(2,2,2))
#calc = KIM("ex_model_Ar_P_Morse_07C")
calc = KIM("LJ_ElliottAkerson_2015_Universal__MO_959249795837_003")
atoms.calc = calc

energy = atoms.get_potential_energy()
print("3D Og fcc potential energy: {} eV".format(energy))
