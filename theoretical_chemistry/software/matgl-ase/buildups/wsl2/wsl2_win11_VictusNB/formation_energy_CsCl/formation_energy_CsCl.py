# formation_energy_CsCl.py

from pymatgen.core import Lattice, Structure
import matgl

matgl.clear_cache()  # This will prompt for confirmation - you can remove this line if you want to keep cache

print("MatGL pretrained models:",matgl.get_available_pretrained_models())

model = matgl.load_model("MEGNet-Eform-MP-2018.6.1")

# This is the structure obtained from the Materials Project.
struct = Structure.from_spacegroup("Pm-3m", Lattice.cubic(4.1437), ["Cs", "Cl"], [[0, 0, 0], [0.5, 0.5, 0.5]])
eform = model.predict_structure(struct)
print(f"The predicted formation energy for CsCl is {float(eform.numpy()):.3f} eV/atom.")
