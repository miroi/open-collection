import numpy as np
from dftd4.interface import DispersionModel as D4Model, DampingParam

# 1. Define the system: H2 molecule
# Positions in Bohr (1.0 Angstrom = 1.889726 Bohr)
numbers = np.array([1, 1], dtype=np.int32)
positions = np.array([
    [0.0, 0.0, 0.0],
    [0.0, 0.0, 1.889726]
], dtype=np.float64)

# 2. Initialize the model
model = D4Model(numbers, positions)

# 3. Define damping parameters (e.g., for PBE)
params = DampingParam(method="pbe")

# 4. Calculate dispersion
# This returns a dictionary in your version
out = model.get_dispersion(params, grad=False)

# 5. Extract energy from the dictionary
if isinstance(out, dict):
    energy = out['energy']
else:
    # Fallback for older versions
    energy = out[0] if isinstance(out, tuple) else out

print(f"Dispersion energy (PBE): {energy:.10f} Eh")

