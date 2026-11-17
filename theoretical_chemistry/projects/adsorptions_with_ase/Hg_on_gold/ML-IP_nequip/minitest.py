from ase.build import bulk
from nequip.ase import NequIPCalculator

atoms = bulk("Au", "fcc", a=4.08)
atoms.calc = NequIPCalculator.from_compiled_model(
    compile_path="model.nequip.pt2",
    device="cuda",
)
print("Potential energy (eV):", atoms.get_potential_energy())

