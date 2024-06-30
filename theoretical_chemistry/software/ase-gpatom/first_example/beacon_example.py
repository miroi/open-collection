#
#  https://gitlab.com/gpatom/ase-gpatom/-/wikis/How-to-use-BEACON#first-example
#
from gpatom.beacon import BEACON
from gpatom.beacon.str_gen import RandomBranch
from ase.calculators.emt import EMT
from ase import Atoms

# Create Atoms object:
atoms = Atoms(['Cu'] * 3 + ['Ag'] * 3, positions=[[0., 0., 0]] * 6)
atoms.center(vacuum=6.0)
atoms.pbc = False

# Define calculator:
calc = EMT
calcparams = dict()

# How to generate random structures?
sgen = RandomBranch(atoms)

# Initialize:
go = BEACON(calc=calc,
            calcparams=calcparams,
            sgen=sgen,
            nsur=3,
            nbest=1,
            nrattle=0,
            ndft=40)

# Run:
go.run()

