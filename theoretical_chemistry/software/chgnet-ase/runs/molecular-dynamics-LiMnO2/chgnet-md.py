#
# https://github.com/CederGroupHub/chgnet?tab=readme-ov-file#molecular-dynamics
#
from chgnet.model.model import CHGNet
from chgnet.model.dynamics import MolecularDynamics
from pymatgen.core import Structure
import warnings
warnings.filterwarnings("ignore", module="pymatgen")
warnings.filterwarnings("ignore", module="ase")

#structure = Structure.from_file("examples/mp-18767-LiMnO2.cif")
structure = Structure.from_file("mp-18767-LiMnO2.cif")
chgnet = CHGNet.load()

md = MolecularDynamics(
    atoms=structure,
    model=chgnet,
    ensemble="nvt",
    temperature=1000,  # in K
    timestep=2,  # in femto-seconds
    trajectory="md_out.traj",
    logfile="md_out.log",
    loginterval=100,
)


print("Starting to run MD with 500 steps per 2fs ..1ps")
#md.run(50)  # run a 0.1 ps MD simulation
md.run(500)  # run a 1 ps MD simulation
print("MD finished, check files ...")
