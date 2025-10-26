#
#  https://chgnet.lbl.gov/#molecular-dynamics
#
from chgnet.model.model import CHGNet
from chgnet.model.dynamics import MolecularDynamics
from pymatgen.core import Structure
import warnings
warnings.filterwarnings("ignore", module="pymatgen")
warnings.filterwarnings("ignore", module="ase")

#structure = Structure.from_file("examples/mp-18767-LiMnO2.cif")
structure = Structure.from_file("../mp-18767-LiMnO2.cif")

chgnet = CHGNet.load()

# set to CPU

#md = MolecularDynamics(use_device='cpu',
md = MolecularDynamics(
    atoms=structure,
    model=chgnet,
    ensemble="nvt",
    temperature=1000,  # in K
    timestep=2,  # in femto-seconds
    trajectory="md_out.traj",
    logfile="md_out.log",
    loginterval=2,
)
md.run(50)  # run a 0.1 ps MD simulation
