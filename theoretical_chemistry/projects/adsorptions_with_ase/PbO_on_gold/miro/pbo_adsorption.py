import numpy as np
from ase import Atoms
from ase.build import fcc111, add_adsorbate
from ase.optimize import BFGS
from chgnet.model.dynamics import CHGNetCalculator

# Initialize Calculator
calc = CHGNetCalculator()

def get_pbo_molecule(orientation='Pb-down'):
    # Pb at origin, O at 1.92A
    mol = Atoms('PbO', positions=[[0, 0, 0], [0, 0, 1.92]])
    if orientation == 'O-down':
        mol.rotate(180, 'x')
    elif orientation == 'horizontal':
        mol.rotate(90, 'x')
    return mol

def run_adsorption(site, orientation):
    # 1. Build Slab
    slab = fcc111('Au', size=(3, 3, 4), vacuum=10.0)
    
    # 2. Add Adsorbate
    pbo = get_pbo_molecule(orientation)
    add_adsorbate(slab, pbo, height=2.5, position=site)
    
    # 3. Setup Calculator & Constraints
    slab.calc = calc
    from ase.constraints import FixAtoms
    # Fix bottom two layers (tags 3 and 4)
    c = FixAtoms(indices=[atom.index for atom in slab if atom.tag > 2])
    slab.set_constraints(c)

    # 4. Optimize
    dyn = BFGS(slab, logfile=None)
    dyn.run(fmax=0.05)
    
    return slab.get_potential_energy()

# Example Test
energy = run_adsorption('ontop', 'Pb-down')
print(f"Final Potential Energy: {energy:.4f} eV")

