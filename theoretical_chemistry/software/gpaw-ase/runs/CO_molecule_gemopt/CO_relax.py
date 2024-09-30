from ase import Atoms
from ase.io import write
from ase.optimize import QuasiNewton
from gpaw import GPAW

# https://gpaw.readthedocs.io/setups/generation_of_setups.html
from gpaw import setup_paths
setup_paths.insert(0, '.')

d = 1.10 # starting guess
atoms = Atoms('CO',positions=((0,0,0),(0,0,d)),pbc=False)

atoms.center(vacuum=4.0)

write('CO.cif', atoms)

# h ... grid space
calc = GPAW(h=0.20, xc='PBE', txt='CO_relax.txt')
atoms.set_calculator(calc)

relax = QuasiNewton(atoms, trajectory='CO.traj', logfile='qn.log')
relax.run(fmax=0.05)


