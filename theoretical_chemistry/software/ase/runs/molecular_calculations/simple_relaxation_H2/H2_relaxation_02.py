#
#  https://wiki.fysik.dtu.dk/gpaw/tutorialsexercises/structureoptimization/gettingstarted/gettingstarted.html
#

from ase import Atoms
from ase.calculators.emt import EMT
from ase.optimize import QuasiNewton
from ase.geometry import get_distances
import numpy as np

#d = starting geometry distance of H2 molecule
for d in np.arange(1.6, 2.8, 0.1):
   print("\n initial distance d(H-H)=",d)
   system = Atoms('H2',positions=[[0.0, 0.0, 0.0],[0.0, 0.0, d]])
   calc = EMT()
   system.calc = calc
   opt = QuasiNewton(system,logfile='opt.logfile')
   opt.run(fmax=0.02)
   print ("number of geometry steps ",opt.get_number_of_steps()+1)
   print("optimized distance d(H-H)=",system.get_distance(0,1))
