import numpy as np
from ase.build import fcc111, add_adsorbate
from ase import Atoms
from ase.optimize import BFGS
from chgnet.model.dynamics import CHGNetCalculator

calc = CHGNetCalculator()

def get_pbo_molecule(orientation='Pb-down'):
    # Pb at origin, O at 1.92A
    mol = Atoms('PbO', positions=[[0, 0, 0], [0, 0, 1.92]])
    if orientation == 'O-down':
        mol.rotate(180, 'x')
    elif orientation == 'horizontal':
        mol.rotate(90, 'x')
    return mol

# --- Pre-calculate Reference Energies ---
# 1. Clean Slab
slab_ref = fcc111('Au', size=(3, 3, 4), vacuum=10.0)
slab_ref.calc = calc
e_slab = slab_ref.get_potential_energy()

# 2. Isolated Molecule (Orientation doesn't matter for energy in vacuum)
mol_ref = get_pbo_molecule()
mol_ref.set_cell([20, 20, 20])
mol_ref.center()
mol_ref.calc = calc
e_mol = mol_ref.get_potential_energy()

def run_adsorption(site, orientation):
    slab = fcc111('Au', size=(3, 3, 4), vacuum=10.0)
    pbo = get_pbo_molecule(orientation)
    
    # 'height' is distance from surface to the first atom in the molecule object
    add_adsorbate(slab, pbo, height=2.2, position=site)
    
    slab.calc = calc
    from ase.constraints import FixAtoms
    c = FixAtoms(indices=[atom.index for atom in slab if atom.tag > 2])
    slab.set_constraint(c)

    dyn = BFGS(slab, logfile=None)
    dyn.run(fmax=0.05)
    
    e_total = slab.get_potential_energy()
    return e_total - (e_slab + e_mol)

# --- Execution Loop ---
sites = ['ontop', 'bridge', 'fcc', 'hcp']
orientations = ['Pb-down', 'O-down', 'horizontal']

print(f"{'Site':<10} | {'Orientation':<12} | {'E_ads (eV)':<10}")
print("-" * 38)

for s in sites:
    for o in orientations:
        try:
            e_ads = run_adsorption(s, o)
            print(f"{s:<10} | {o:<12} | {e_ads:>10.4f}")
        except Exception as e:
            print(f"{s:<10} | {o:<12} | Error: {e}")

