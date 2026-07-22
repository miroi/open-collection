import os
from ase import Atoms
from ase.calculators.mopac import MOPAC
from ase.optimize import BFGS

# 1. Set the environment variable for the MOPAC executable path
os.environ['ASE_MOPAC_COMMAND'] = 'path/to/mopac'

# 2. Define the molecule (Water)
molecule = Atoms('H2O',
                 positions=[[0.000,  0.000,  0.000],
                            [0.000,  0.757,  0.586],
                            [0.000, -0.757,  0.586]])

# 3. Attach the MOPAC calculator
molecule.calc = MOPAC(label='h2o_opt', method='PM7', task='1SCF')

# 4. Optimize the geometry
opt = BFGS(molecule, trajectory='opt.traj')
opt.run(fmax=0.05)

# 5. Extract structural parameters (Indices: O=0, H1=1, H2=2)
r_oh1 = molecule.get_distance(0, 1)
r_oh2 = molecule.get_distance(0, 2)
angle_hoh = molecule.get_angle(1, 0, 2)

# 6. Print the structural results
print(f"\n--- Optimized Geometry Results ---")
print(f"O-H1 Bond Length : {r_oh1:.3f} Å")
print(f"O-H2 Bond Length : {r_oh2:.3f} Å")
print(f"H-O-H Bond Angle : {angle_hoh:.1f}°")

