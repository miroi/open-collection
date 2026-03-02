
from ase.build import fcc111, molecule, add_adsorbate
from ase.optimize import BFGS
import numpy as np

def run_hgo_adsorption():
    # Specific imports to avoid the circular error and attribute error
    from chgnet.model.model import CHGNet
    from chgnet.model.dynamics import CHGNetCalculator
    
    # 1. Load the model and manually create the calculator
    model = CHGNet.load()
    calc = CHGNetCalculator(model=model)

    def get_relaxed_energy(atoms, label):
        atoms.calc = calc
        print(f"Relaxing {label}...")
        dyn = BFGS(atoms, logfile=None)
        dyn.run(fmax=0.05)
        return atoms.get_potential_energy()

    # 2. Relax the Au(111) Slab
    # Using a 3x3x3 slab for speed; use more layers for better accuracy
    slab = fcc111('Au', size=(3, 3, 3), vacuum=10.0)
    e_slab = get_relaxed_energy(slab, "Gold Slab")

    # 3. Relax the HgO Molecule
    hgo = molecule('O')
    hgo.append('Hg')
    hgo.set_distance(0, 1, 2.01) # Approx bond length for HgO
    hgo.center(vacuum=10.0)
    e_hgo = get_relaxed_energy(hgo, "HgO Molecule")

    # 4. Adsorption System (Hg-down on top site)
    system = slab.copy()
    # Placing Hg 2.5A above the surface, O above Hg
    add_adsorbate(system, 'Hg', height=2.5, position='ontop')
    add_adsorbate(system, 'O', height=4.5, position='ontop')
    
    e_total = get_relaxed_energy(system, "Adsorbed System")

    # 5. Adsorption Energy Calculation
    # E_ads = E_total - (E_slab + E_molecule)
    e_ads = e_total - (e_slab + e_hgo)
    
    print("\n" + "="*30)
    print(f"Adsorption Energy: {e_ads:.4f} eV")
    print("="*30)
    if e_ads < 0:
        print("Adsorption is EXOTHERMIC (stable).")
    else:
        print("Adsorption is ENDOTHERMIC (unstable).")

if __name__ == "__main__":
    run_hgo_adsorption()

