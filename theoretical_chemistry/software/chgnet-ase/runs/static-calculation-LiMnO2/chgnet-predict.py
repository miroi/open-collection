#
# https://github.com/CederGroupHub/chgnet?tab=readme-ov-file#direct-inference-static-calculation
#
from chgnet.model.model import CHGNet
from pymatgen.core import Structure

chgnet = CHGNet.load()

#structure = Structure.from_file('examples/mp-18767-LiMnO2.cif')
structure = Structure.from_file('mp-18767-LiMnO2.cif')


prediction = chgnet.predict_structure(structure)

for key, unit in [
    ("energy", "eV/atom"),
    ("forces", "eV/A"),
    ("stress", "GPa"),
    ("magmom", "mu_B"),
]:
    print(f"CHGNet-predicted {key} ({unit}):\n{prediction[key[0]]}\n")
