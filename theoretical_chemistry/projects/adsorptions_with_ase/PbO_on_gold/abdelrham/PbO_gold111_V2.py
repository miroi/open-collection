import numpy as np
from ase import Atoms, Atom
from ase.build import bulk, fcc111
from ase.optimize import BFGS
from ase.constraints import FixAtoms
from ase.filters import UnitCellFilter  
from ase.io import write
from chgnet.model.model import CHGNet
from chgnet.model.dynamics import CHGNetCalculator
import warnings
warnings.filterwarnings("ignore", message="Skipping unhashable information")

def get_relaxed_energy(atoms, label):
    atoms.calc = calc
    if len(atoms) > 2:
        z_min = np.min(atoms.positions[:, 2])
        mask = [pos[2] < (z_min + 1 ) for pos in atoms.positions]
        atoms.set_constraint(FixAtoms(mask=mask))

    dyn = BFGS(atoms, logfile=None)
    dyn.run(fmax=0.05)
    write(f"{label}_relaxed.xyz", atoms)
    return atoms.get_potential_energy()

# Load Model
model = CHGNet.load()
calc = CHGNetCalculator(model=model)

atoms = bulk('Au', 'fcc', a=4.0, cubic=True)
atoms.calc = calc

# Allow the cell to relax its volume/shape
ucf = UnitCellFilter(atoms)
dyn = BFGS(ucf, logfile=None)
dyn.run(fmax=0.01)

# The lattice constant a
a_opt = atoms.get_cell()[0, 0]
print('The lattice constant a = ',a_opt)

#Setup Au(111) Slab
#slab = fcc111('Au', size=(3, 3, 4), vacuum=10.0, a=a_opt)

slab = Atoms(
    symbols=['Au']*48,
    positions=[ # positions in Angstrom 
        [2.162792418, 0.416273963, 5.000027010],
        [-0.720892382, 2.081170159, 7.354685128],
        [0.720950007, 1.248722043, 9.709145886],
        [5.046592448, 0.416273963, 5.000027010],
        [2.162907605, 2.081170159, 7.354685128],
        [3.604750037, 1.248722043, 9.709145886],
        [7.930392134, 0.416273963, 5.000027010],
        [5.046707978, 2.081170159, 7.354685128],
        [6.488550067, 1.248722043, 9.709145886],
        [10.814192164, 0.416273963, 5.000027010],
        [7.930508008, 2.081170159, 7.354685128],
        [9.372350097, 1.248722043, 9.709145886],
        [0.720892425, 2.913718011, 5.000027010],
        [-2.162792397, 4.578614244, 7.354685128],
        [-0.720950007, 3.746166128, 9.709145886],
        [3.604692455, 2.913718011, 5.000027010],
        [0.721007590, 4.578614244, 7.354685128],
        [2.162850022, 3.746166128, 9.709145886],
        [6.488492141, 2.913718011, 5.000027010],
        [3.604807963, 4.578614244, 7.354685128],
        [5.046650052, 3.746166128, 9.709145886],
        [9.372292170, 2.913718011, 5.000027010],
        [6.488607993, 4.578614244, 7.354685128],
        [7.930450082, 3.746166128, 9.709145886],
        [-0.721007762, 5.411162394, 5.000027010],
        [-3.604692240, 7.076058032, 7.354685128],
        [-2.162850022, 6.243610213, 9.709145886],
        [2.162792268, 5.411162394, 5.000027010],
        [-0.720892253, 7.076058032, 7.354685128],
        [0.720950007, 6.243610213, 9.709145886],
        [5.046591954, 5.411162394, 5.000027010],
        [2.162908120, 7.076058032, 7.354685128],
        [3.604750037, 6.243610213, 9.709145886],
        [7.930391984, 5.411162394, 5.000027010],
        [5.046708150, 7.076058032, 7.354685128],
        [6.488550067, 6.243610213, 9.709145886],
        [-2.162907777, 7.908606479, 5.000027010],
        [-5.046592255, 9.573502117, 7.354685128],
        [-3.604750037, 8.741054298, 9.709145886],
        [0.720892253, 7.908606479, 5.000027010],
        [-2.162792268, 9.573502117, 7.354685128],
        [-0.720950007, 8.741054298, 9.709145886],
        [3.604691939, 7.908606479, 5.000027010],
        [0.721008106, 9.573502117, 7.354685128],
        [2.162850022, 8.741054298, 9.709145886],
        [6.488491969, 7.908606479, 5.000027010],
        [3.604808135, 9.573502117, 7.354685128],
        [5.046650052, 8.741054298, 9.709145886]
    ],
    cell=[ # values in Angstrom
        [11.5352001190, 0.0000000000, 0.0000000000],
        [-5.7676000595, 9.9897763408, 0.0000000000],
        [0.0000000000, 0.0000000000, 19.7091999054]
    ],
    pbc=[True, True, True]
)

z_surf = np.max(slab.positions[:, 2])
e_slab = get_relaxed_energy(slab.copy(), "pure_slab")
print('The Energy of Gold Surface Au(111) = ',e_slab)

#Setup PbO Molecular (Horizontal)
bond_length = 2.3
pbo_mol = Atoms('PbO', positions=[[0, 0, 0], [bond_length, 0, 0]])
pbo_mol.center(vacuum=10.0)
e_pbo_free = get_relaxed_energy(pbo_mol, "isolated_pbo")

print('The Energy of PbO (Isolated) = ',e_pbo_free)

surface_atoms = slab[slab.positions[:, 2] > (z_surf - 0.5)]
ref_atom = surface_atoms[0]
ref_x = ref_atom.position[0]
ref_y = ref_atom.position[1]
# d is the distance between nearest neighbor Au atoms on the (111) surface
d = a_opt / np.sqrt(2)

manual_sites = {
    'ontop':  [ref_x, ref_y],
    'bridge': [ref_x + d / 2.0, ref_y],
    'fcc':    [ref_x + d / 2.0, ref_y + d / (2.0 * np.sqrt(3))],
    'hcp':    [ref_x + d / 2.0, ref_y - d / (2.0 * np.sqrt(3))]
}
angles = np.arange(0, 360, 45)
print(f"\n{'Site':<10} | {'Angle':<12} | {'E_total (eV)':<10} | {'E_ads (eV)':<10}")
print("-" * 50)

results = []
initial_height = 2.3

for site_name, (sx, sy) in manual_sites.items():
    for angle in angles:
        system = slab.copy()
    
        # Place Pb
        #pb_pos = np.array([sx, sy, z_surf + initial_height])
        #system.append(Atom('Pb', position=pb_pos))
    
        mol = Atoms('PbO', positions=[[0, 0, 0], [bond_length, 0, 0]])
        mol.rotate(angle, 'z', center='COM') 
        mol.positions += [sx, sy, z_surf + initial_height]
        system.extend(mol)

        system.set_pbc(True)
        system.wrap()
        label = f"flat_{site_name}_angle_{angle}"
    
        try:
            e_total = get_relaxed_energy(system, label)
            e_ads = e_total - (e_slab + e_pbo_free)
            print(f"{site_name:<10} | {f"{angle}":<12} | {e_total:>10.4f} | {e_ads:>10.4f}")
            results.append((e_ads, site_name))
        except Exception as e:
            print(f"{site_name:<10} | {'Flat':<12} | FAILED: {e}")

if results:
    best_e, best_site = min(results)
    print("-" * 40)
    print(f"Most Stable: {best_site} (Flat) at {best_e:.4f} eV")
