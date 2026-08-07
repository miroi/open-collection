from ase import Atoms
from xtb.ase.calculator import XTB
from ase.md.verlet import VelocityVerlet
from ase.md import MDLogger
from ase.units import fs

# Create water molecule
water = Atoms('H2O',
              positions=[[0.000, 0.000, 0.000],
                        [0.757, 0.586, 0.000],
                        [-0.757, 0.586, 0.000]],
              cell=[10.0, 10.0, 10.0])

# Set up calculator
calc = XTB(method='GFN2-xTB')
water.calc = calc

# Set initial velocities at 300K
water.set_velocities(300)

# Run MD
dt = 1.0 * fs  # 1 fs time step
md = VelocityVerlet(water, dt)

# Run for 50 steps
print("Running MD simulation...")
for step in range(50):
    md.run(1)
    if step % 10 == 0:
        print(f"Step {step}: Potential energy = {water.get_potential_energy():.4f} eV")
EOF

