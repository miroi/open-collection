from ase import Atoms, Atom
from ase.build import fcc111, add_adsorbate
from ase.optimize import BFGS
from ase.constraints import FixAtoms
from ase.io import write
import numpy as np

def run_comprehensive_study():
    # Delayed imports for environment stability
    from chgnet.model.model import CHGNet
    from chgnet.model.dynamics import CHGNetCalculator
    
    model = CHGNet.load()
    calc = CHGNetCalculator(model=model)

    def get_relaxed_energy(atoms, label):
        atoms.calc = calc
        # Fix bottom 2 layers of a 4-layer slab
        # fcc111 tags layers from 1 (top) to 4 (bottom)
        if len(atoms) > 2: # Only apply to slab/system, not molecule
            mask = [atom.tag > 2 for atom in atoms]
            atoms.set_constraint(FixAtoms(mask=mask))
        
        dyn = BFGS(atoms, logfile=None)
        dyn.run(fmax=0.05)
        
        # Save the structure for visualization
        write(f"{label}_relaxed.xyz", atoms)
        return atoms.get_potential_energy()

    # 1. Setup Slab (4 layers, Au)
    slab = fcc111('Au', size=(3, 3, 4), vacuum=10.0)
    e_slab = get_relaxed_energy(slab.copy(), "pure_slab")

    # 2. Setup HgO Molecule Manually
    # Hg at (0,0,0), O at (0,0,2.0)
    hgo = Atoms('HgO', positions=[[0, 0, 0], [0, 0, 2.0]])
    hgo.center(vacuum=10.0)
    e_hgo = get_relaxed_energy(hgo, "isolated_hgo")

    # 3. Site and Orientation Matrix
    sites = ['ontop', 'bridge', 'fcc', 'hcp']
    orientations = [('Hg', 'O', 'Hg-down'), ('O', 'Hg', 'O-down')]
    
    print(f"\n{'Site':<10} | {'Orientation':<12} | {'E_ads (eV)':<10}")
    print("-" * 40)

    results = []
    for site in sites:
        for bot_sym, top_sym, orient_label in orientations:
            system = slab.copy()
            
            # Place the base atom at the specific site
            # height=2.3 is a safe starting distance for metal surfaces
            add_adsorbate(system, bot_sym, height=2.3, position=site)
            
            # Add the second atom of the molecule 2.0A above the first
            base_pos = system[-1].position
            top_atom = Atom(top_sym, position=base_pos + [0, 0, 2.0])
            system.append(top_atom)
            
            # Ensure PBC is correct
            system.set_pbc(True)
            
            label = f"{site}_{orient_label}"
            try:
                e_total = get_relaxed_energy(system, label)
                e_ads = e_total - (e_slab + e_hgo)
                print(f"{site:<10} | {orient_label:<12} | {e_ads:>10.4f}")
                results.append((e_ads, site, orient_label))
            except Exception as e:
                print(f"{site:<10} | {orient_label:<12} | FAILED: {e}")

    # 4. Final Summary
    if results:
        best_e, best_site, best_orient = min(results)
        print("-" * 40)
        print(f"Most Stable: {best_site} / {best_orient} ({best_e:.4f} eV)")
        print(f"Check {best_site}_{best_orient}_relaxed.xyz for the geometry.")

if __name__ == "__main__":
    run_comprehensive_study()

