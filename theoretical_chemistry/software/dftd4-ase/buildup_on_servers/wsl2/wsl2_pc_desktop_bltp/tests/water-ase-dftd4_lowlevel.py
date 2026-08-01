import numpy as np
from dftd4.interface import DispersionModel, DampingParam

# 1. Define geometry arrays (Water molecule example)
# Atomic numbers: O=8, H=1, H=1
numbers = np.array([8, 1, 1], dtype=np.int32)

# Cartesian coordinates in Bohr (atomic units)
positions = np.array([
    [0.00000000,  0.00000000,  0.22191422],
    [0.00000000,  1.43003054, -0.88765689],
    [0.00000000, -1.43003054, -0.88765689]
], dtype=np.float64)

# 2. Instantiate the DispersionModel
model = DispersionModel(numbers, positions, charge=0.0)

# 3. Load the damping parameters for your functional (e.g., PBE)
param = DampingParam(method="PBE")

# 4. Pass arguments positionally: (param, grad)
# Set the second argument to True to calculate both energy and gradients
results = model.get_dispersion(param, True)

# The output dictionary contains the results
energy = results["energy"]
gradient = results["gradient"]

print(f"Dispersion Energy (Hartree): {energy:.8f}")
print(f"Nuclear Gradient (Hartree/Bohr):\n{gradient}")

