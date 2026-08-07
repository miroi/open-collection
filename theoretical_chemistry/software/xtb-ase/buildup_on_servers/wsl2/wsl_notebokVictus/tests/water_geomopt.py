from ase import Atoms
from ase.optimize import BFGS
from xtb.ase.calculator import XTB

# Create water molecule
water = Atoms('H2O',
              positions=[[0.0, 0.0, 0.0],        # O
                        [0.757, 0.586, 0.0],    # H1
                        [-0.757, 0.586, 0.0]],  # H2
              cell=[10, 10, 10])

# Set up XTB calculator
calc = XTB(method='GFN2-xTB')  # or 'GFN1-xTB'
water.calc = calc

# Optimize geometry
opt = BFGS(water)
opt.run(fmax=0.05)

# Print final geometry
print("Optimized geometry:")
print(water.positions)
print(f"Final energy: {water.get_potential_energy():.6f} eV")
