from ase.build import molecule
from ase.optimize import BFGS
from ase.vibrations import Vibrations
from alignn.ff.ff import AlignnAtomwiseCalculator, default_path

# 1. Build a molecule and put it in a vacuum box
atoms = molecule("H2O")
atoms.center(vacuum=8.0)
atoms.pbc = True            # ALIGNN builds graphs with periodic neighbor lists

# 2. Attach the ALIGNN-FF calculator
calc = AlignnAtomwiseCalculator(
    path=default_path(),    # or path to your own trained model folder
    device="cpu",           # "cuda" if available
    stress_wt=0.0,          # no cell relaxation for a molecule
)
atoms.calc = calc

# 3. Single-point properties
print("E  (eV):", atoms.get_potential_energy())
print("F (eV/Å):\n", atoms.get_forces())

# 4. Geometry optimization
opt = BFGS(atoms, trajectory="relax.traj", logfile="relax.log")
opt.run(fmax=0.02)
print("Relaxed E (eV):", atoms.get_potential_energy())
print("O-H distance (Å):", atoms.get_distance(0, 1))
print("H-O-H angle (°):", atoms.get_angle(1, 0, 2))

# 5. Vibrational frequencies (finite differences)
vib = Vibrations(atoms, name="vib")
vib.run()
vib.summary()
vib.clean()

# 6. Reaction/binding-type energy differences
e_mol = atoms.get_potential_energy()
