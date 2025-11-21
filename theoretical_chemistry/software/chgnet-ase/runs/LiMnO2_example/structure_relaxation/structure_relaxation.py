#
# https://github.com/CederGroupHub/chgnet?tab=readme-ov-file#direct-inference-static-calculation
#
from chgnet.model.model import CHGNet
from pymatgen.core import Structure
from chgnet.model import StructOptimizer

chgnet = CHGNet.load()

#structure = Structure.from_file('examples/mp-18767-LiMnO2.cif')
structure = Structure.from_file('../mp-18767-LiMnO2.cif')

relaxer = StructOptimizer()
result = relaxer.relax(structure)
print("CHGNet relaxed structure", result["final_structure"])
print("relaxed total energy in eV:", result['trajectory'].energies[-1])


