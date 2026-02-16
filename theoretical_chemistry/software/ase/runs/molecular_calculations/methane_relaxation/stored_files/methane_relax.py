# from Google AI, modified by MI
#

from ase import Atoms
from ase.build import molecule
from ase.calculators.emt import EMT
from ase.optimize import BFGS
from ase.io import write

import itertools

def analyze_methane_geometry():
    """Prints all bond lengths and angles for a methane molecule."""
    # Initialize methane: Carbon is index 0, Hydrogens are 1-4
    atoms = molecule('CH4')
    
    print("--- Methane Geometry Analysis ---")

    # 1. Print all C-H Bond Lengths
    print("\n[Bond Lengths]")
    for i in range(1, 5):
        length = atoms.get_distance(0, i)
        print(f"C-H{i} distance: {length:.4f} Å")

    # 2. Print all H-C-H Bond Angles
    print("\n[Bond Angles]")
    h_indices = [1, 2, 3, 4]
    # Get all unique combinations of two hydrogens around the central Carbon
    for h1, h2 in itertools.combinations(h_indices, 2):
        angle = atoms.get_angle(h1, 0, h2)
        print(f"H{h1}-C-H{h2} angle: {angle:.2f}°")

# 1. Create a molecule (Methane)
atoms = molecule('CH4')
write('CH4_nonoptimized.xyz', atoms)

# Iterate to see all unique bond lengths
for i in range(1, 5):
    print(f"Nonptimized C-H{i} bond length: {atoms.get_distance(0, i):.3f} Å")

# Get ALL unique bond angles (H-C-H angles)
# Methane has 6 unique H-C-H angles (combinations of 4 hydrogens around central C)
h_indices = [1, 2, 3, 4]
h_combinations = list(itertools.combinations(h_indices, 2))

print("\nAll H-C-H Bond Angles (°):")
for h1, h2 in h_combinations:
    # get_angle(index1, vertex_index, index2)
    angle = atoms.get_angle(h1, 0, h2)
    print(f" Nonoptimized H{h1}-C-H{h2}: {angle:.2f}")


# 2. Set a calculator (Effective Medium Theory - fast for simple systems)
atoms.calc = EMT()

print("\n Welcome to CH4 molecule relaxation with EMT calculator !")

# 3. Optimize the geometry
print(f"Initial energy: {atoms.get_total_energy():.4f} eV")
dyn = BFGS(atoms, trajectory='ch4_opt.traj')
dyn.run(fmax=0.05)  # Optimize until forces are small

# 4. Final results
print(f"Final energy: {atoms.get_total_energy():.4f} eV")
print("Optimization complete.")

write('CH4_optimized.xyz', atoms)

