from chgnet.model.model import CHGNet
#from chgnet.model.dynamics import MolecularDynamics
from pymatgen.core import Structure
from chgnet.model import StructOptimizer
import warnings
warnings.filterwarnings("ignore", module="pymatgen")
warnings.filterwarnings("ignore", module="ase")

#structure = Structure.from_file("examples/mp-18767-LiMnO2.cif")
structure = Structure.from_file("../mp-18767-LiMnO2.cif")
chgnet = CHGNet.load()

relaxer = StructOptimizer()
result = relaxer.relax(structure)

print("CHGNet relaxed structure", result["final_structure"])
print("relaxed total energy in eV:", result['trajectory'].energies[-1])

