from ase import Atoms
from ase.optimize import BFGS
from deepmd.calculator import DP

# 1. Define the system geometry (Water Molecule)
# Ensure the element symbols match the types your model was trained on
water_molecule = Atoms(
    symbols='H2O',
    positions=[
        (0.7601, 1.9270, 1.0000), # Hydrogen 1
        (1.9575, 1.0000, 1.0000), # Hydrogen 2
        (1.0000, 1.0000, 1.0000)  # Oxygen
    ],
    cell=[10.0, 10.0, 10.0],       # Periodic boundary box dimensions
    pbc=True                       # Turn on periodic boundary conditions
)

# 2. Instantiate and attach the DeePMD-kit Calculator
# Replace 'graph.pb' with the actual path to your frozen model file
dp_calculator = DP(model="graph.pb")
water_molecule.calc = dp_calculator

# 3. Extract Static Physical Properties
# The calculator handles mapping coordinates to model descriptors automatically
potential_energy = water_molecule.get_potential_energy()
atomic_forces = water_molecule.get_forces()
system_stress = water_molecule.get_stress()

print(f"Initial Potential Energy: {potential_energy:.4f} eV")
print("Initial Forces (eV/Å):\n", atomic_forces)
print("System Stress Tensor:\n", system_stress)

# 4. Geometry Optimization (Relaxation)
# Use ASE's optimization algorithms driven by Deep Potential forces
print("\n--- Starting Structure Optimization ---")
optimizer = BFGS(water_molecule, trajectory='relaxation.traj')
optimizer.run(fmax=0.01) # Relax until maximum force component is < 0.01 eV/Å

print(f"\nOptimized Potential Energy: {water_molecule.get_potential_energy():.4f} eV")

