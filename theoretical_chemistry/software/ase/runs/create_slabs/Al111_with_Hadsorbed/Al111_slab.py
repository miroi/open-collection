#
# https://wiki.fysik.dtu.dk/ase/ase/build/surface.html
#

from ase.build import fcc111
from ase import atoms
from ase.calculators.emt import EMT
from ase.optimize import QuasiNewton

this_vac=15.0
slab = fcc111('Al', size=(2,2,3), vacuum=this_vac)

slab.write("Al_111.in")

#slab.write("Al_111.xyz")

# see https://mattermodeling.stackexchange.com/questions/4615/how-do-you-write-an-xyz-file-in-the-atomic-simulation-environment
import ase.io
ase.io.write('Al_111.xyz', slab)

slab.calc = EMT()
e_slabUO = slab.get_potential_energy()
print('Unoptimized Al_111(2,2,3)vac EMT potential energy:',e_slabUO)

# optimize 
dyn = QuasiNewton(slab, trajectory='Al_111_relaxing.traj')
dyn.run(fmax=0.005)
e_slabO = slab.get_potential_energy()
print('Optimized Al_111(2,2,3)vac EMT potential energy:',e_slabO)


