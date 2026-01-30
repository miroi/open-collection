from chgnet.model.model import CHGNet

from chgnet.graph import  CrystalGraphConverter

#from chgnet.model.dynamics import MolecularDynamics
from pymatgen.core import Structure
from chgnet.model import StructOptimizer
import warnings
warnings.filterwarnings("ignore", module="pymatgen")
warnings.filterwarnings("ignore", module="ase")

#structure = Structure.from_file("examples/mp-18767-LiMnO2.cif")
structure = Structure.from_file("../../mp-18767-LiMnO2.cif")


#chgnet = CHGNet.load(verbose=True)
chgnet = CHGNet.load()

chgnet.graph_converter = CrystalGraphConverter(
    atom_graph_cutoff=chgnet.graph_converter.atom_graph_cutoff,
    bond_graph_cutoff=chgnet.graph_converter.bond_graph_cutoff,
    algorithm="legacy",
)


#relaxer = StructOptimizer()
relaxer = StructOptimizer(use_device='cpu')

result = relaxer.relax(structure, verbose=True)

print("CHGNet relaxed structure", result["final_structure"])
print("relaxed total energy in eV:", result['trajectory'].energies[-1])

