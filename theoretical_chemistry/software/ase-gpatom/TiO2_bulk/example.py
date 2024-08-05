from gpatom.beacon import BEACON
from gpatom.beacon.str_gen import RandomCell

from ase import Atoms
from gpaw import GPAW, PW
from gpaw.mixer import Mixer

# Create system
atoms = Atoms(['Ti'] * 4 + ['O'] * 8, positions=[[0., 0., 0.]]*12)
atoms.cell = [4.594, 4.594, 2*2.959]
atoms.pbc = True

# Define calculator
calc = GPAW
calc_params = dict(mode=PW(700),
                   xc='PBE',
                   symmetry='off',
                   kpts={'size': (4, 4, 4)},
                   mixer=Mixer(beta=0.1, nmaxold=5, weight=50.0),
                   txt='gpaw.txt')

# How to generate random structures?
sgen = RandomCell(atoms)

# Initialize
glopt = BEACON(calc=calc,
               calcparams=calc_params,
               gp_args={'params': dict(limit=4.0, Rlimit=3.6)},
               sgen=sgen,
               nsur=24,
               nrattle=4,
               nbest=6,
               ndft=60)
# Run
glopt.run()

