from ase import Atoms
from xtb.ase.calculator import XTB
from ase.md.langevin import Langevin
from ase.md import MDLogger
from ase.units import fs, kB
import numpy as np

# Create water molecule
water = Atoms('H2O',
              positions=[[0.000, 0.000, 0.000],
                        [0.757, 0.586, 0.000],
                        [-0.757, 0.586, 0.000]],
              cell=[10.0, 10.0, 10.0])

# Set up calculator
calc = XTB(method='GFN2-xTB')
water.calc = calc

# Set initial velocities manually at 300K
temperature = 300  # Kelvin
masses = water.get_masses()
velocities = np.random.randn(len(water), 3) * np.sqrt(kB * temperature / masses[:, np.newaxis])
velocities -= np.average(velocities, weights=masses, axis=0)
water.set_velocities(velocities)

# Run NVT MD with Langevin thermostat - using correct API
dt = 1.0 * fs  # 1 fs time step
friction = 0.01  # Friction coefficient in 1/fs

# Use fixcm=False with constraint for better sampling
from ase.constraints import FixCom
water.set_constraint(FixCom())

md = Langevin(water, dt, temperature_K=temperature, friction=friction, fixcm=False)

print("Running MD simulation with Langevin thermostat...")
print("Step\tPotential (eV)\tKinetic (eV)\tTemperature (K)")
print("-" * 65)

for step in range(50):
    md.run(1)
    if step % 10 == 0:
        pot = water.get_potential_energy()
        kin = water.get_kinetic_energy()
        temp = water.get_temperature()
        print(f"{step:4d}\t{pot:10.4f}\t{kin:10.4f}\t{temp:10.2f}")
