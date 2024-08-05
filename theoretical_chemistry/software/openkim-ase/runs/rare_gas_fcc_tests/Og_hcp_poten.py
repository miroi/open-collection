#
# try Og hcp
#

from ase.lattice.cubic import FaceCenteredCubic
from ase.calculators.kim.kim import KIM
from ase.build import bulk

atoms = bulk(name='Og',crystalstructure='hcp', a=5.25)
calc = KIM("LJ_ElliottAkerson_2015_Universal__MO_959249795837_003")
atoms.calc = calc

print ("Og hcp cell ",atoms.cell)

energy = atoms.get_potential_energy()
print("3D Og hcp potential energy: {} eV".format(energy))



