import numpy as np
import warnings
from ase import Atoms, Atom
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
    """Attaches calculator, fixes bottom layers, and returns optimized energy."""
    atoms.calc = calc
    if len(atoms) > 2:
        # Fix atoms below a certain Z-threshold (bottom layers)
        z_min = np.min(atoms.positions[:, 2])
        mask = [pos[2] < (z_min + 1.0) for pos in atoms.positions]
        atoms.set_constraint(FixAtoms(mask=mask))

    dyn = BFGS(atoms, logfile=None)
    dyn.run(fmax=0.05)
    write(f"{label}_relaxed.xyz", atoms)
    return atoms.get_potential_energy()

def get_rotated_molecule(symbols, bond_length, theta, phi):
    """
    Creates a diatomic molecule rotated by polar angle theta 
    and azimuthal angle phi.
    - theta=0: Vertical (O above Pb)
    - theta=90: Horizontal (Flat)
    - theta=180: Flipped (Pb above O)
    """
    # Define molecule with Pb at origin and O on Z-axis
    mol = Atoms(symbols, positions=[[0, 0, 0], [0, 0, bond_length]])
    
    # 1. Tilt relative to surface normal (Y-axis rotation)
    mol.rotate(theta, 'y', center=(0, 0, 0))
    # 2. Rotate around surface normal (Z-axis rotation)
    mol.rotate(phi, 'z', center=(0, 0, 0))
    
    return mol

# --- 1. Setup Calculator & Bulk Optimization ---
model = CHGNet.load()
calc = CHGNetCalculator(model=model)

# Find optimized lattice constant for Au
bulk_au = bulk('Au', 'fcc', a=4.0, cubic=True)
bulk_au.calc = calc
ucf = UnitCellFilter(bulk_au)
dyn = BFGS(ucf, logfile=None)
dyn.run(fmax=0.01)

a_opt = bulk_au.get_cell()[0, 0]
d = a_opt / np.sqrt(2) # Nearest neighbor distance
print(f'Optimized lattice constant a = {a_opt:.4f}')

# --- 2. Setup Au(111) Slab ---
# Using your provided coordinates and cell
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
    cell=[
        [11.5352001190, 0.0000000000, 0.0000000000],
        [-5.7676000595, 9.9897763408, 0.0000000000],
        [0.0000000000, 0.0000000000, 19.7091999054]
    ],
    pbc=[True, True, True]
)

z_surf = np.max(slab.positions[:, 2])
e_slab = get_relaxed_energy(slab.copy(), "pure_slab")
print(f'Energy of Pure Au(111) Slab = {e_slab:.4f} eV')

# --- 3. Setup Isolated PbO ---
bond_length = 2.3
pbo_mol = Atoms('PbO', positions=[[0, 0, 0], [0, 0, bond_length]])
pbo_mol.center(vacuum=10.0)
e_pbo_free = get_relaxed_energy(pbo_mol, "isolated_pbo")
print(f'Energy of Isolated PbO = {e_pbo_free:.4f} eV')

# --- 4. Adsorption Site Calculation ---
# Identify a reference atom on the top layer
surface_atoms = slab[slab.positions[:, 2] > (z_surf - 0.5)]
ref_atom = surface_atoms[0]
ref_x, ref_y = ref_atom.position[0], ref_atom.position[1]

manual_sites = {
    'ontop':  [ref_x, ref_y],
    'bridge': [ref_x + d / 2.0, ref_y],
    'fcc':    [ref_x + d / 2.0, ref_y + d / (2.0 * np.sqrt(3))],
    'hcp':    [ref_x + d / 2.0, ref_y - d / (2.0 * np.sqrt(3))]
}

# Rotation parameters: 
# thetas: 0 (vertical O-up), 90 (flat), 180 (vertical Pb-up)
# phis: rotation around the normal
thetas = [0, 45, 90, 135, 180]
phis = [0, 90, 180, 270]
initial_height = 2.3

results = []
print(f"\n{'Site':<8} | {'Theta':<6} | {'Phi':<6} | {'E_total':<10} | {'E_ads':<10}")
print("-" * 55)

for site_name, (sx, sy) in manual_sites.items():
    for theta in thetas:
        for phi in phis:
            # Prepare the system
            system = slab.copy()
            
            # Generate the rotated molecule (Pb is first atom, at origin)
            mol = get_rotated_molecule('PbO', bond_length, theta, phi)
            
            # Add adsorbate: height is relative to the top atom of the slab
            # add_adsorbate handles PBC and wrapping automatically
            add_adsorbate(system, mol, height=initial_height, position=(sx, sy))
            
            label = f"{site_name}_t{theta}_p{phi}"
            
            try:
                e_total = get_relaxed_energy(system, label)
                e_ads = e_total - (e_slab + e_pbo_free)
                print(f"{site_name:<8} | {theta:<6} | {phi:<6} | {e_total:>10.4f} | {e_ads:>10.4f}")
                results.append((e_ads, label))
            except Exception as e:
                print(f"{label:<20} | FAILED: {e}")

# --- 5. Summary ---
if results:
    best_e, best_label = min(results)
    print("-" * 55)
    print(f"Global Minimum: {best_label}")
    print(f"Adsorption Energy: {best_e:.4f} eV")

