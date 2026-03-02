from ase.build import fcc111, molecule, add_adsorbate
from ase.optimize import BFGS
from ase.constraints import FixAtoms
import numpy as np

def run_comparison():
    # Delayed imports for Python 3.12 stability
    from chgnet.model.model import CHGNet
    from chgnet.model.dynamics import CHGNetCalculator
    
    # 1. Initialize CHGNet
    model = CHGNet.load()
    calc = CHGNetCalculator(model=model)

    def get_relaxed_energy(atoms, label, fix_bottom=False):
        atoms.calc = calc
        if fix_bottom:
            # Fix atoms with Z-coordinate less than the average (bottom layers)
            indices = [atom.index for atom in atoms if atom.position[2] < np.mean(atoms.positions[:, 2])]
            atoms.set_constraint(FixAtoms(indices=indices))
        
        print(f"Relaxing {label}...")
        dyn = BFGS(atoms, logfile=None)
        dyn.run(fmax=0.05)
        return atoms.get_potential_energy()

    # 2. Relax Reference Slab (Fix bottom layers)
    slab = fcc111('Au', size=(3, 3, 4), vacuum=10.0) # 4 layers is better
    e_slab = get_relaxed_energy(slab.copy(), "Au(111) Slab", fix_bottom=True)

    # 3. Relax Reference Molecule
    hgo = molecule('O')
    hgo.append('Hg')
    hgo.set_distance(0, 1, 2.01)
    hgo.center(vacuum=10.0)
    e_hgo = get_relaxed_energy(hgo, "Isolated HgO")

    # 4. Compare Orientations
    # Configurations: (Bottom_Atom, Top_Atom, Label)
    configs = [
        ('Hg', 'O', 'Mercury-down'),
        ('O', 'Hg', 'Oxygen-down')
    ]
    
    results = {}

    for bot, top, label in configs:
        system = slab.copy()
        # Place the first atom 2.5A above surface, second 2.0A above that
        add_adsorbate(system, bot, height=2.5, position='ontop')
        add_adsorbate(system, top, height=4.5, position='ontop')
        
        e_total = get_relaxed_energy(system, f"System ({label})", fix_bottom=True)
        e_ads = e_total - (e_slab + e_hgo)
        results[label] = e_ads

    # 5. Output Comparison
    print("\n" + "="*40)
    print(f"{'Orientation':<20} | {'Adsorption Energy (eV)':<20}")
    print("-" * 45)
    for label, energy in results.items():
        print(f"{label:<20} | {energy:>18.4f} eV")
    print("="*40)
    
    best = min(results, key=results.get)
    print(f"The most stable configuration is: {best}")

if __name__ == "__main__":
    run_comparison()

