from ase.build import molecule
from mlip.simulation.ase import ViSNetCalculator

# 1. Define the molecular structure (Ethanol)
atoms = molecule('CH3CH2OH')

# 2. Initialize the pre-trained ViSNet ASE calculator
# 'visnet-base' or your local model checkpoint path can be passed here
calc = ViSNetCalculator(model='visnet-base', device='cpu')

# 3. Attach the calculator to the atoms object
atoms.calc = calc

# 4. Perform calculations
energy = atoms.get_potential_energy()
forces = atoms.get_forces()

# 5. Output results
print(f"Total Potential Energy: {energy:.4f} eV")
print("Atomic Forces (eV/Å):")
print(forces)

