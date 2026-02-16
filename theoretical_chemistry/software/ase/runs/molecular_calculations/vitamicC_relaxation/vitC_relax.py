from ase.build import molecule
from ase.optimize import BFGS
from ase.calculators.emt import EMT
from ase.visualize import view

# 1. Define Vitamin C (Ascorbic Acid)
# Note: 'Ascorbic_acid' is the internal name in ASE's g2 database
atoms = molecule('Ascorbic_acid')

# 2. Attach a Calculator (using EMT for a fast, simple example)
atoms.calc = EMT()

# 3. Set up the Optimizer
# 'trajectory' saves the optimization steps for later visualization
opt = BFGS(atoms, trajectory='vitC_relax.traj', logfile='relax.log')

# 4. Run the relaxation
# fmax=0.05 is the force convergence criterion in eV/Angstrom
print("Starting relaxation...")
opt.run(fmax=0.05)

# 5. Output Results
print(f"Final Potential Energy: {atoms.get_potential_energy():.4f} eV")

# Optional: Visualize the final structure (requires ase-gui)
# view(atoms)

