import numpy as np
from ase.build import bulk, fcc111, fcc100, fcc110
from ase.calculators.emt import EMT
from ase.optimize import BFGS
from ase.io import write

# 1. Reference: Bulk Energy per atom
a_lattice = 4.08  # Experimental lattice constant for Au
gold_bulk = bulk('Au', 'fcc', a=a_lattice)
gold_bulk.calc = EMT()
e_bulk_per_atom = gold_bulk.get_potential_energy() / len(gold_bulk)

# 2. Define Surface Types to test
# surface_funcs maps the Miller index to the ASE build function
surface_funcs = {
    "(111)": fcc111,
    "(100)": fcc100,
    "(110)": fcc110
}

print(f"{'Surface':<10} | {'Surface Energy (eV/Å²)':<25}")
print("-" * 40)

for name, build_func in surface_funcs.items():
    # Create slab: 3 layers, 10A vacuum on each side
    # size=(2, 2, 3) creates a 2x2 supercell with 3 layers
    slab = build_func('Au', size=(2, 2, 3), vacuum=10.0, a=a_lattice)
    slab.calc = EMT()
    
    # Relax internal atom positions
    dyn = BFGS(slab, logfile=None)
    dyn.run(fmax=0.05)

    # Export structures using ASE's write
    #write(f'saved_slab{name}.vasp',slab,format='vasp', direct=True)
    write(f'saved_slab{build_func}.vasp',slab,format='vasp', direct=True)
    
    # Calculate Area (Area = |a x b| for the unit cell vectors)
    cell = slab.get_cell()
    area = np.linalg.norm(np.cross(cell[0], cell[1]))
    
    # Surface Energy Formula: (E_slab - n * E_bulk) / (2 * Area)
    e_slab = slab.get_potential_energy()
    n_atoms = len(slab)
    gamma = (e_slab - n_atoms * e_bulk_per_atom) / (2 * area)
    
    print(f"{name:<10} | {gamma:.6f}")

