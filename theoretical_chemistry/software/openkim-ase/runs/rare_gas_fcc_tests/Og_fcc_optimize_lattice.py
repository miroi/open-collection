#
#

from ase.constraints import ExpCellFilter, StrainFilter
from ase.calculators.kim.kim import KIM
from ase.build import bulk
from ase.optimize import LBFGS, BFGS, FIRE

Og_fcc = bulk(name='Og',crystalstructure='fcc', a=5.25)
calc = KIM("LJ_ElliottAkerson_2015_Universal__MO_959249795837_003")
Og_fcc.calc = calc

print ("Og fcc cell befor optim:",Og_fcc.cell)
energy = Og_fcc.get_potential_energy()
print("Og fcc potential energy before opt: {} eV".format(energy))

Og_fcc.calc = calc

Og_fcc = StrainFilter(Og_fcc)
opt = LBFGS(Og_hcp, trajectory="lbfgs_Og_fcc.traj")
opt.run()

print ("Og fcc cell AFTER optim:",Og_fcc.atoms.cell)
energy = Og_fcc.get_potential_energy()
print("Og fcc potential energy AFTER opt: {} eV".format(energy))
