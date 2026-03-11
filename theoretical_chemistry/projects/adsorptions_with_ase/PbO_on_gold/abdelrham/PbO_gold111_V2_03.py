import numpy as np
import warnings
from ase import Atoms
from ase.build import bulk, add_adsorbate
from ase.optimize import BFGS
from ase.constraints import FixAtoms
from ase.filters import UnitCellFilter  
from ase.io import write
from chgnet.model.model import CHGNet
from chgnet.model.dynamics import CHGNetCalculator

# Ignore specific unhashable info warnings from CHGNet/ASE integration
warnings.filterwarnings("ignore", message="Skipping unhashable information")

def get_relaxed_energy(atoms, label):
    """
    Attaches calculator, fixes bottom layers, and returns optimized energy.
    Now writes .traj (binary trajectory) and .log (text log) files.
    """
    atoms.calc = calc
    
    # 1. Apply Constraints
    if len(atoms) > 2:
        # Fix atoms below a certain Z-threshold (bottom layers)
        z_min = np.min(atoms.positions[:, 2])
        # Fix atoms within 1.0 Angstrom of the bottom
        mask = [pos[2] < (z_min + 1.0) for pos in atoms.positions]
        atoms.set_constraint(FixAtoms(mask=mask))

    # 2. Setup Optimizer with Trajectory and Logfile
    # label_relaxed.traj: Can be opened with 'ase gui filename.traj'
    # label_relaxed.log: Text file with force and energy per step
    traj_file = f"{label}_relaxed.traj"
    log_file = f"{label}_relaxed.log"
    
    dyn = BFGS(atoms, trajectory=traj_file, logfile=log_file)
    
    # 3. Run Relaxation
    dyn.run(fmax=0.05)
    
    # Write final state to XYZ for easy viewing in other software
    write(f"{label}_final.xyz", atoms)
    
    return atoms.get_potential_energy()

def get_rotated_molecule(symbols, bond_length, theta, phi):
    """Creates a diatomic molecule rotated by polar (theta) and azimuthal (phi) angles."""
    mol = Atoms(symbols, positions=[[0, 0, 0], [0, 0, bond_length]])
    mol.rotate(theta, 'y', center=(0, 0, 0))
    mol.rotate(phi, 'z', center=(0, 0, 0))
    return mol

# --- 1. Setup Calculator & Bulk Optimization ---
model = CHGNet.load()
calc = CHGNetCalculator(model=model)

# Find optimized lattice constant for Au
bulk_au = bulk('Au', 'fcc', a=4.0, cubic=True)
bulk_au.calc = calc
ucf = UnitCellFilter(bulk_au)
# Log the bulk relaxation too
dyn = BFGS(ucf, trajectory='bulk_relax.traj', logfile='bulk_relax.log')
dyn.run(fmax=0.01)

# Extract optimized cell parameters
cell_opt = bulk_au.get_cell()
a_opt = cell_opt[0,0] 
d = a_opt / np.sqrt(2) # Nearest neighbor distance
print(f'Optimized lattice constant a = {a_opt:.4f}')

# --- 2. Setup Au(111) Slab ---
# (Using your provided coordinates)
slab = Atoms(
    symbols=['Au']*48,
    positions=[
        [2.162792418, 0.416273963, 5.000027010], [-0.720892382, 2.081170159, 7.354685128],
        [0.720950007, 1.248722043, 9.709145886], [5.046592448, 0.416273963, 5.000027010],
        [2.162907605, 2.081170159, 7.354685128], [3.604750037, 1.248722043, 9.709145886],
        [7.930392134, 0.416273963, 5.000027010], [5.046707978, 2.081170159, 7.354685128],
        [6.488550067, 1.248722043, 9.709145886], [10.814192164, 0.416273963, 5.000027010],
        [7.930508008, 2.081170159, 7.354685128], [9.372350097, 1.248722043, 9.709145886],
        [0.720892425, 2.913718011, 5.000027010], [-2.162792397, 4.578614244, 7.354685128],
        [-0.720950007, 3.746166128, 9.709145886], [3.604692455, 2.913718011, 5.000027010],
        [0.721007590, 4.578614244, 7.354685128], [2.162850022, 3.746166128, 9.709145886],
        [6.488492141, 2.913718011, 5.000027010], [3.604807963, 4.578614244, 7.354685128],
        [5.046650052, 3.746166128, 9.709145886], [9.372292170, 2.913718011, 5.000027010],
        [6.488607993, 4.578614244, 7.354685128], [7.930450082, 3.746166128, 9.709145886],
        [-0.721007762, 5.411162394, 5.000027010], [-3.604692240, 7.076058032, 7.354685128],
        [-2.162850022, 6.243610213, 9.709145886], [2.162792268, 5.411162394, 5.000027010],
        [-0.720892253, 7.076058032, 7.354685128], [0.720950007, 6.243610213, 9.709145886],
        [5.046591954, 5.411162394, 5.000027010], [2.162908120, 7.076058032, 7.354685128],
        [3.604750037, 6.243610213, 9.709145886], [7.930391984, 5.411162394, 5.000027010],
        [5.046708150, 7.076058032, 7.354685128], [6.488550067, 6.243610213, 9.709145886],
        [-2.162907777, 7.908606479, 5.000027010], [-5.046592255, 9.573502117, 7.354685128],
        [-3.604750037, 8.741054298, 9.709145886], [0.720892253, 7.908606479, 5.000027010],
        [-2.162792268, 9.573502117, 7.354685128], [-0.720950007, 8.741054298, 9.709145886],
        [3.604691939, 7.908606479, 5.000027010], [0.721008106, 9.573502117, 7.354685128],
        [2.162850022, 8.741054298, 9.709145886], [6.488491969, 7.908606479, 5.000027010],
        [3.604808135, 9.573502117, 7.354685128], [5.046650052, 8.741054298, 9.709145886]
    ],
    cell=[[11.535200119, 0, 0], [-5.7676000595, 9.9897763408, 0], [0, 0, 19.7091999054]],
    pbc=True
)

z_surf = np.max(slab.positions[:, 2])
e_slab = get_relaxed_energy(slab.copy(), "pure_slab")

# --- 3. Setup Isolated PbO ---
bond_length = 2.3
pbo_mol = Atoms('PbO', positions=[[0, 0, 0], [0, 0, bond_length]])
pbo_mol.center(vacuum=10.0)
e_pbo_free = get_relaxed_energy(pbo_mol, "isolated_pbo")

# --- 4. Adsorption Site Calculation ---
surface_atoms = slab[slab.positions[:, 2] > (z_surf - 0.5)]
ref_atom = surface_atoms[0]
ref_x, ref_y = ref_atom.position[0], ref_atom.position[1]

manual_sites = {
    'ontop':  [ref_x, ref_y],
    'bridge': [ref_x + d / 2.0, ref_y],
    'fcc':    [ref_x + d / 2.0, ref_y + d / (2.0 * np.sqrt(3))],
    'hcp':    [ref_x + d / 2.0, ref_y - d / (2.0 * np.sqrt(3))]
}

thetas = [0, 90, 180] 
phis = [0, 90, 180, 270]
initial_height = 2.3
results = []

print(f"\n{'Site':<8} | {'Theta':<6} | {'Phi':<6} | {'E_ads':<10}")
print("-" * 40)

for site_name, (sx, sy) in manual_sites.items():
    for theta in thetas:
        for phi in phis:
            system = slab.copy()
            mol = get_rotated_molecule('PbO', bond_length, theta, phi)
            add_adsorbate(system, mol, height=initial_height, position=(sx, sy))
            
            label = f"ads_{site_name}_t{theta}_p{phi}"
            
            try:
                e_total = get_relaxed_energy(system, label)
                e_ads = e_total - (e_slab + e_pbo_free)
                print(f"{site_name:<8} | {theta:<6} | {phi:<6} | {e_ads:>10.4f}")
                results.append((e_ads, label))
            except Exception as e:
                print(f"{label:<20} | FAILED: {e}")

if results:
    best_e, best_label = min(results)
    print("-" * 40)
    print(f"Global Minimum: {best_label} at {best_e:.4f} eV")

