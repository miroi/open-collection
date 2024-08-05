#
#  https://wiki.fysik.dtu.dk/ase/ase/calculators/kim.html#advanced-usage
#

from ase.lattice.cubic import FaceCenteredCubic
from ase.calculators.kim.kim import KIM

atoms = FaceCenteredCubic(symbol='Au', latticeconstant=4.07, size=(1,1,1))
calc = KIM("Sim_LAMMPS_LJcut_AkersonElliott_Alchemy_PbAu")
atoms.calc = calc

energy = atoms.get_potential_energy()
print("Potential energy: {} eV".format(energy))
