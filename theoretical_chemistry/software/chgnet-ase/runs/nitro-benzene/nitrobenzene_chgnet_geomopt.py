from ase.build import molecule
from ase.optimize import BFGS
from chgnet.model.dynamics import CHGNetCalculator
from chgnet.model.model import CHGNet

# 1. Initialize the nitrobenzene molecule (C6H5NO2)
# ASE contains a database of common molecules
atoms = molecule('C6H5NO2')

# 2. Load the pretrained CHGNet model
# By default, this loads the latest version (e.g., v0.3.0)
model = CHGNet.load()

# 3. Attach the CHGNet Calculator to the atoms object
atoms.calc = CHGNetCalculator(model)

# 4. Set up the Optimizer
# BFGS is a common choice for molecular geometry optimization
# 'trajectory' saves the optimization steps for later visualization
dyn = BFGS(atoms, trajectory='nitrobenzene_opt.traj', logfile='opt.log')

# 5. Run the optimization
# fmax defines the convergence criteria (force < 0.05 eV/Å)
dyn.run(fmax=0.05)

print(f"Optimization complete. Final energy: {atoms.get_potential_energy():.4f} eV")
print(f"Final positions:\n{atoms.get_positions()}")

