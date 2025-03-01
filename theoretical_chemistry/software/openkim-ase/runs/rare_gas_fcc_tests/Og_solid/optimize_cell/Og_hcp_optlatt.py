#
# try Og hcp
#
# see https://docs.matlantis.com/atomistic-simulation-tutorial/en/2_1_opt.html#2.-Lattice-constant-optimization-of-Fe-crystal

from ase.constraints import ExpCellFilter, StrainFilter
from ase.calculators.kim.kim import KIM
from ase.build import bulk
from ase.optimize import LBFGS, BFGS, FIRE

Og_hcp = bulk(name='Og',crystalstructure='hcp', a=5.25)
calc = KIM("LJ_ElliottAkerson_2015_Universal__MO_959249795837_003")
Og_hcp.calc = calc

print ("Og hcp cell befor optim:",Og_hcp.cell)
energy = Og_hcp.get_potential_energy()
print("3D Og hcp potential energy before opt: {} eV".format(energy))

Og_hcp.calc = calc

Og_hcp = StrainFilter(Og_hcp)
opt = LBFGS(Og_hcp, trajectory="lbfgs_Og_fcc.traj")
opt.run()

print ("Og hcp cell AFTER optim:",Og_hcp.atoms.cell)
energy = Og_hcp.get_potential_energy()
print("3D Og hcp potential energy AFTER opt: {} eV".format(energy))

