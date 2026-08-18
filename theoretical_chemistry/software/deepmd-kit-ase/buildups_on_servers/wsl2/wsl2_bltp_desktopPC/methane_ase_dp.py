from ase import Atoms
from ase.optimize import BFGS
from deepmd.calculator import DP

# Define a Methane system instead of Water to match your model's elements
molecule = Atoms(
    symbols='CH4',
    positions=[
        (0.0000, 0.0000, 0.0000),   # Carbon (C)
        (0.6291, 0.6291, 0.6291),   # Hydrogen (H)
        (-0.6291, -0.6291, 0.6291),
        (-0.6291, 0.6291, -0.6291),
        (0.6291, -0.6291, -0.6291)
    ],
    cell=[10.0, 10.0, 10.0],
    pbc=True
)

# Explicitly tell the calculator which index maps to which element name
# (For the tutorial model: H is 0, C is 1)
dp_calculator = DP(model="graph.pb", type_dict={"H": 0, "C": 1})
molecule.calc = dp_calculator

# Run properties extraction
print(f"Calculated Potential Energy: {molecule.get_potential_energy():.4f} eV")

