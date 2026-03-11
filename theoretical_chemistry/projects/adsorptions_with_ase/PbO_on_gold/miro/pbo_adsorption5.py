import os
from ase import Atoms, io
from ase.build import fcc111, add_adsorbate
from ase.optimize import BFGS
from ase.constraints import FixAtoms
from chgnet.model.dynamics import CHGNetCalculator

# 1. Setup
output_dir = "adsorption_results"
os.makedirs(output_dir, exist_ok=True)
calc = CHGNetCalculator()

def get_pbo_molecule(orientation='Pb-down'):
    # Pb at origin, O at 1.92A
    mol = Atoms('PbO', positions=[[0, 0, 0], [0, 0, 1.92]])
    if orientation == 'O-down':
        mol.rotate(180, 'x')
    elif orientation == 'horizontal':
        mol.rotate(90, 'x')
    return mol

# Variables to track the most stable structure
best_energy = float('inf')
best_atoms = None
best_name = ""

sites = ['ontop', 'bridge', 'fcc', 'hcp']
orientations = ['Pb-down', 'O-down', 'horizontal']

print(f"{'Site':<10} | {'Orientation':<12} | {'Energy (eV)':<12}")
print("-" * 40)

# 2. Main Loop
for s in sites:
    for o in orientations:
        try:
            # Build and constrain
            slab = fcc111('Au', size=(3, 3, 4), vacuum=10.0)
            pbo = get_pbo_molecule(o)
            add_adsorbate(slab, pbo, height=2.5, position=s)
            
            slab.calc = calc
            # Fix atoms with tag > 2 (bottom layers)
            c = FixAtoms(indices=[atom.index for atom in slab if atom.tag > 2])
            slab.set_constraint(c)

            # Optimize
            name = f"{s}_{o}"
            dyn = BFGS(slab, logfile=f"{output_dir}/{name}.log")
            dyn.run(fmax=0.05)
            
            energy = slab.get_potential_energy()
            print(f"{s:<10} | {o:<12} | {energy:>12.4f}")

            # Save ALL converged structures to BOTH formats
            # XYZ is good for quick visualization
            io.write(f"{output_dir}/{name}_converged.xyz", slab)
            # VASP (POSCAR format) is good for further DFT calculations
            io.write(f"{output_dir}/{name}_converged.vasp", slab, format='vasp', direct=True)

            # Track the most stable
            if energy < best_energy:
                best_energy = energy
                best_atoms = slab.copy()
                best_name = name

        except Exception as e:
            print(f"{s:<10} | {o:<12} | Failed: {e}")

# 3. Final summary and output for the winner
if best_atoms:
    print(f"\n" + "="*40)
    print(f"WINNER: {best_name}")
    print(f"ENERGY: {best_energy:.4f} eV")
    print("="*40)
    
    io.write("MOST_STABLE_PbO_Au.vasp", best_atoms, format='vasp', direct=True)
    io.write("MOST_STABLE_PbO_Au.xyz", best_atoms)
    print("Final files saved to root and 'adsorption_results' folder.")

