# surface_energy_fixed.py
import numpy as np
import torch
from ase.build import bulk, surface
from ase.optimize import BFGS
from ase.constraints import FixAtoms
from ase.io import write
from nequip.integrations.ase import NequIPCalculator
import warnings
warnings.filterwarnings('ignore')

# Load model
print("Loading NequIP model...")
calc = NequIPCalculator.from_compiled_model(
    "allegro_oam_l_gpu.nequip.pt2",
    device="cuda",
    chemical_species_to_atom_type_map=True,
)
print("✓ Model loaded!")

def get_surface_energy(orientation, layers, size=(1, 1), a=5.43, relax=True):
    """
    Calculate surface energy for a given orientation and layers.
    """
    
    print(f"\n{'='*60}")
    print(f"Calculating {orientation} surface with {layers} layers...")
    print(f"{'='*60}")
    
    # Miller indices
    miller_map = {
        '111': (1, 1, 1),
        '100': (1, 0, 0),
        '110': (1, 1, 0)
    }
    miller = miller_map[orientation]
    
    # Create bulk structure
    bulk_atoms = bulk('Si', 'diamond', a=a, cubic=True)
    
    # Create surface slab
    slab = surface(bulk_atoms, miller, layers, vacuum=10.0, periodic=True)
    
    # Repeat in surface directions if needed
    if size != (1, 1):
        slab = slab * size
    
    print(f"  Atoms in slab: {len(slab)}")
    
    # Calculate surface area
    cell = slab.cell
    area = np.linalg.norm(np.cross(cell[0], cell[1]))
    print(f"  Surface area: {area:.2f} Å²")
    
    # Fix bottom layers
    positions = slab.get_positions()
    z_min = np.min(positions[:, 2])
    z_max = np.max(positions[:, 2])
    z_mid = (z_min + z_max) / 2
    mask = positions[:, 2] < z_mid
    constraint = FixAtoms(mask=mask)
    slab.set_constraint(constraint)
    n_fixed = np.sum(mask)
    print(f"  Fixed {n_fixed} atoms ({n_fixed/len(slab)*100:.1f}%)")
    
    # Relax
    if relax:
        print("  Relaxing slab...")
        slab.calc = calc
        opt = BFGS(slab, 
                   logfile=f'{orientation}_{layers}layers.log')
        # Don't use trajectory to avoid write issues
        opt.run(fmax=0.02)
        print(f"  Relaxation: {opt.get_number_of_steps()} steps")
    
    # Calculate slab energy
    slab.calc = calc
    slab_energy = slab.get_potential_energy()
    print(f"  Slab energy: {slab_energy:.6f} eV")
    
    # Get bulk energy per atom
    bulk_atoms = bulk('Si', 'diamond', a=a, cubic=True)
    bulk_atoms.calc = calc
    bulk_energy = bulk_atoms.get_potential_energy()
    bulk_energy_per_atom = bulk_energy / len(bulk_atoms)
    print(f"  Bulk energy per atom: {bulk_energy_per_atom:.6f} eV")
    
    # Surface energy: (E_slab - N*E_bulk) / (2*area)
    surface_energy = (slab_energy - len(slab) * bulk_energy_per_atom) / (2 * area)
    
    print(f"\n  Surface energy:")
    print(f"    {surface_energy:.6f} eV/Å²")
    print(f"    {surface_energy * 160.21766208:.3f} J/m²")
    
    # Save structure without extra data (simpler format)
    try:
        # Save as simple XYZ
        from ase.io import write
        write(f'{orientation}_{layers}layers_final.xyz', slab, format='xyz')
        print(f"  Saved structure to {orientation}_{layers}layers_final.xyz")
    except Exception as e:
        print(f"  Could not save structure: {e}")
    
    return surface_energy, len(slab), slab_energy, area

# Main calculation
print("\n" + "=" * 70)
print("SURFACE ENERGY CALCULATIONS")
print("=" * 70)

results = {}

for orientation in ['111', '100', '110']:
    # Use different layer numbers for different orientations
    if orientation == '111':
        layers = 8
    elif orientation == '100':
        layers = 6
    else:  # '110'
        layers = 6
    
    try:
        se, n_atoms, slab_energy, area = get_surface_energy(
            orientation, layers, size=(1, 1), a=5.43, relax=True
        )
        
        results[orientation] = {
            'surface_energy': se,
            'atoms': n_atoms,
            'energy': slab_energy,
            'area': area,
            'layers': layers
        }
        
    except Exception as e:
        print(f"Error calculating {orientation}: {e}")
        import traceback
        traceback.print_exc()

# Summary
print("\n" + "=" * 70)
print("SUMMARY")
print("=" * 70)
print(f"{'Orientation':<12} {'Layers':<8} {'Atoms':<8} {'Surface Energy (eV/Å²)':<25} {'J/m²':<10}")
print("-" * 70)

for orient, data in results.items():
    se = data['surface_energy']
    se_jm2 = se * 160.21766208
    print(f"  {orient:<10} {data['layers']:<8} {data['atoms']:<8} {se:<20.6f} {se_jm2:<10.3f}")

print("\n" + "=" * 70)
print("Done!")
print("=" * 70)
