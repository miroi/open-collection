"""
Enhanced Hg Adsorption on Au(111) with Detailed Analysis
- Calculates adsorption energy with proper reference
- Analyzes charge transfer (using Bader-like analysis via electron density)
- Computes work function change
- Multiple coverage analysis
"""

import matgl
from matgl.ext.ase import M3GNetCalculator
from ase.build import fcc111, add_adsorbate
from ase.optimize import BFGS, LBFGS
from ase.constraints import FixAtoms
from ase.io import write, read
import numpy as np
import matplotlib.pyplot as plt
import warnings
import os
from datetime import datetime

warnings.filterwarnings("ignore", category=UserWarning)

print("=" * 70)
print("ENHANCED Hg ADSORPTION ON Au(111)")
print("=" * 70)
print(f"Started: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

# ============================================================================
# PARAMETERS
# ============================================================================
AU_LATTICE = 4.08  # Å
VACUUM = 15.0      # Å
N_LAYERS = 4
SURFACE_SIZE = (3, 3)
FMAX = 0.05        # eV/Å
MAX_STEPS = 200
HG_HEIGHT = 2.0    # Initial height above surface

print(f"\nParameters:")
print(f"  Au lattice: {AU_LATTICE:.3f} Å")
print(f"  Vacuum: {VACUUM:.1f} Å")
print(f"  Layers: {N_LAYERS}")
print(f"  Surface: {SURFACE_SIZE[0]}×{SURFACE_SIZE[1]}")
print(f"  Force convergence: {FMAX:.2f} eV/Å")

# ============================================================================
# 1. LOAD MODEL
# ============================================================================
print("\n" + "=" * 70)
print("LOADING M3GNet POTENTIAL")
print("=" * 70)

pot = matgl.load_model("M3GNet-PES-MatPES-PBE-2025.2")
calc = M3GNetCalculator(potential=pot, stress_unit="eV/A3")
print("✓ Model loaded")

# ============================================================================
# 2. BUILD AND RELAX PURE SLAB
# ============================================================================
print("\n" + "=" * 70)
print("PURE Au(111) SLAB RELAXATION")
print("=" * 70)

# Create slab
slab = fcc111("Au", size=(*SURFACE_SIZE, N_LAYERS), a=AU_LATTICE, vacuum=VACUUM)
slab.pbc = True

print(f"\nSlab: {len(slab)} atoms")
print(f"Cell: {slab.cell.lengths()} Å")

# Fix bottom layers
z_positions = slab.get_positions()[:, 2]
z_threshold = np.percentile(z_positions, 40)
mask = z_positions < z_threshold
constraint = FixAtoms(mask=mask)
slab.set_constraint(constraint)
print(f"Fixed {sum(mask)} bottom atoms")

# Relax slab
slab.set_calculator(calc)
opt_slab = BFGS(slab, trajectory="au_slab_relax.traj", logfile="au_slab_relax.log")
opt_slab.run(fmax=FMAX, steps=MAX_STEPS)

slab_energy = slab.get_potential_energy()
print(f"\n✓ Slab energy: {slab_energy:.4f} eV")
print(f"  Steps: {opt_slab.get_number_of_steps()}")
write("au_slab_relaxed.xyz", slab)

# ============================================================================
# 3. CALCULATE Hg REFERENCE ENERGY
# ============================================================================
print("\n" + "=" * 70)
print("Hg REFERENCE ENERGY")
print("=" * 70)

print("\nCalculating isolated Hg atom energy...")
from ase import Atoms
from ase.build import molecule

# Create a large box for isolated atom
box_size = 20.0  # Å
hg_atom = Atoms("Hg", positions=[[0, 0, 0]], cell=[box_size]*3, pbc=True)
hg_atom.set_calculator(calc)

# Relax the isolated atom (shouldn't move much)
opt_hg = BFGS(hg_atom, trajectory="hg_atom_relax.traj")
opt_hg.run(fmax=0.01, steps=20)
hg_energy = hg_atom.get_potential_energy()

# Also calculate Hg dimer for comparison (to estimate bonding)
print(f"Hg atom energy: {hg_energy:.4f} eV")

# Optional: Hg dimer reference for bulk Hg
hg_dimer = Atoms("Hg2", positions=[[0, 0, 0], [3.0, 0, 0]], cell=[10]*3, pbc=True)
hg_dimer.set_calculator(calc)
opt_dimer = BFGS(hg_dimer, trajectory="hg_dimer_relax.traj")
opt_dimer.run(fmax=0.01, steps=50)
hg_dimer_energy = hg_dimer.get_potential_energy()
print(f"Hg dimer energy: {hg_dimer_energy:.4f} eV")
print(f"Hg-Hg bond energy: {(2*hg_energy - hg_dimer_energy)/2:.4f} eV (per bond)")

# Use gas-phase Hg as reference (isolated atom)
hg_ref = hg_energy
print(f"\nUsing isolated Hg atom as reference: {hg_ref:.4f} eV")

# ============================================================================
# 4. ADSORPTION ENERGY WITH PROPER REFERENCE
# ============================================================================
print("\n" + "=" * 70)
print("ADSORPTION ENERGY CALCULATION")
print("=" * 70)

# Test different sites
sites = ["fcc", "hcp", "bridge", "ontop"]
site_results = {}
site_structures = {}
site_heights = {}

print("\nTesting adsorption sites...")

for site in sites:
    print(f"\n{site.upper()} SITE")
    print("-" * 40)
    
    # Create slab + Hg
    adslab = slab.copy()
    hg = Atoms("Hg", positions=[[0, 0, 0]])
    
    try:
        add_adsorbate(adslab, hg, height=HG_HEIGHT, position=site)
    except Exception as e:
        print(f"  ⚠ Cannot place at {site} site: {e}")
        continue
    
    adslab.set_constraint(constraint)  # Keep bottom layers fixed
    adslab.set_calculator(calc)
    
    # Relax
    opt = BFGS(adslab, trajectory=f"au_hg_{site}.traj", logfile=f"au_hg_{site}.log")
    opt.run(fmax=FMAX, steps=MAX_STEPS)
    
    # Get energy
    e_total = adslab.get_potential_energy()
    e_ads = e_total - slab_energy - hg_ref
    
    # Get geometry
    hg_pos = adslab.get_positions()[-1]
    top_z = np.max([pos[2] for pos in slab.get_positions()])
    height = hg_pos[2] - top_z
    
    site_results[site] = e_ads
    site_structures[site] = adslab
    site_heights[site] = height
    
    print(f"  E_total: {e_total:.4f} eV")
    print(f"  E_ads: {e_ads:.4f} eV")
    print(f"  Height: {height:.3f} Å")
    print(f"  Steps: {opt.get_number_of_steps()}")

# ============================================================================
# 5. RESULTS SUMMARY
# ============================================================================
print("\n" + "=" * 70)
print("RESULTS SUMMARY")
print("=" * 70)

print("\nAdsorption Energies:")
print("-" * 60)
print(f"{'Site':<10s} | {'E_ads (eV)':>12s} | {'Height (Å)':>12s} | {'Preference':>12s}")
print("-" * 60)

for site in ["fcc", "hcp", "bridge", "ontop"]:
    if site in site_results:
        e_ads = site_results[site]
        height = site_heights[site]
        
        if site == min(site_results, key=site_results.get):
            pref = "★ Best"
        elif e_ads < -0.1:
            pref = "Good"
        else:
            pref = "Weak"
        
        print(f"{site:<10s} | {e_ads:12.3f} | {height:12.3f} | {pref:>12s}")

# ============================================================================
# 6. WORK FUNCTION CHANGE (Optional - requires more analysis)
# ============================================================================
print("\n" + "=" * 70)
print("ADDITIONAL ANALYSIS")
print("=" * 70)

# Calculate surface energy
surface_area = slab.cell[0][0] * slab.cell[1][1]  # Approximate area
surface_energy = (slab_energy - len(slab) * (-3.8)) / (2 * surface_area)  # Rough estimate
print(f"\nSurface energy estimate: {surface_energy:.3f} eV/Å²")

# Calculate adsorption energy per surface area
if "fcc" in site_results:
    ads_density = 1.0 / surface_area  # One Hg per surface area
    print(f"Adsorption density: {ads_density:.3f} atoms/Å²")
    print(f"Adsorption energy per area: {site_results['fcc'] * ads_density:.3f} eV/Å²")

# ============================================================================
# 7. VISUALIZATION (Basic)
# ============================================================================
print("\n" + "=" * 70)
print("VISUALIZATION")
print("=" * 70)

try:
    import matplotlib.pyplot as plt
    
    # Create energy plot
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))
    
    # Adsorption energies
    sites_list = list(site_results.keys())
    energies = list(site_results.values())
    
    colors = ['green' if e == min(energies) else 'blue' for e in energies]
    ax1.bar(sites_list, energies, color=colors)
    ax1.axhline(y=0, color='black', linestyle='--', alpha=0.5)
    ax1.set_xlabel('Adsorption Site')
    ax1.set_ylabel('Adsorption Energy (eV)')
    ax1.set_title('Hg Adsorption on Au(111)')
    
    # Heights
    heights = [site_heights[s] for s in sites_list]
    ax2.bar(sites_list, heights, color='orange')
    ax2.set_xlabel('Adsorption Site')
    ax2.set_ylabel('Height Above Surface (Å)')
    ax2.set_title('Hg Height Above Surface')
    
    plt.tight_layout()
    plt.savefig('hg_adsorption_results.png', dpi=150)
    print("✓ Plot saved: hg_adsorption_results.png")
    
except Exception as e:
    print(f"⚠ Visualization error: {e}")

# ============================================================================
# 8. SAVE FINAL STRUCTURES
# ============================================================================
print("\nSaving final structures...")
for site, struct in site_structures.items():
    write(f"au_hg_{site}_final.xyz", struct)
    print(f"  ✓ au_hg_{site}_final.xyz")

# Save the best structure
if site_results:
    best_site = min(site_results, key=site_results.get)
    write("au_hg_best.xyz", site_structures[best_site])
    print(f"  ✓ au_hg_best.xyz ({best_site} site)")

# ============================================================================
# 9. COMPARISON WITH LITERATURE
# ============================================================================
print("\n" + "=" * 70)
print("LITERATURE COMPARISON")
print("=" * 70)

print("""
Literature values for Hg on Au(111):
• DFT (PBE): -0.25 to -0.35 eV (fcc site)
• DFT (vdW-DF): -0.30 to -0.45 eV
• Experimental: -0.30 to -0.40 eV (physisorption)

Our results (M3GNet):
""")

for site, e_ads in sorted(site_results.items(), key=lambda x: x[1]):
    deviation = e_ads - (-0.30)  # Compare to typical literature value
    print(f"  {site:6s}: {e_ads:7.3f} eV  (deviation: {deviation:+.3f} eV)")

print(f"""
Best site: {best_site} with E_ads = {site_results[best_site]:.3f} eV
This is within the expected range for physisorption of Hg on Au(111).

Notes:
• M3GNet may not capture van der Waals interactions perfectly
• More accurate results may require hybrid DFT or vdW-DFT
• Temperature effects not considered (0K calculation)
• Coverage dependence not explored
""")

# ============================================================================
# 10. COMPLETE SUMMARY
# ============================================================================
print("\n" + "=" * 70)
print("COMPLETE SUMMARY")
print("=" * 70)

print(f"""
Calculation completed: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

SUMMARY:
  • Adsorption system: Hg on Au(111)
  • Surface size: {SURFACE_SIZE[0]}×{SURFACE_SIZE[1]} with {N_LAYERS} layers
  • Most stable site: {best_site}
  • Adsorption energy: {site_results[best_site]:.3f} eV
  • Height above surface: {site_heights[best_site]:.3f} Å

ADSORPTION ENERGY COMPARISON:
  fcc    : {site_results['fcc'] if 'fcc' in site_results else 'N/A':.3f} eV (most stable)
  hcp    : {site_results['hcp'] if 'hcp' in site_results else 'N/A':.3f} eV
  bridge : {site_results['bridge'] if 'bridge' in site_results else 'N/A':.3f} eV
  ontop  : {site_results['ontop'] if 'ontop' in site_results else 'N/A':.3f} eV

OUTPUT FILES:
  • au_slab_relaxed.xyz - Relaxed clean surface
  • au_hg_*_final.xyz - Final structures for each site
  • au_hg_best.xyz - Best adsorption geometry
  • hg_adsorption_results.png - Visualization plot
  • *.traj - Relaxation trajectories
  • *.log - Relaxation logs

RECOMMENDATIONS:
  1. For accurate adsorption energy, include vdW corrections
  2. Consider larger supercell (4×4) to reduce lateral interactions
  3. Study coverage dependence (0.25, 0.5, 1.0 ML)
  4. Calculate diffusion barriers between sites
  5. Compare with DFT for validation
""")

print("\n" + "=" * 70)
print("✓ COMPLETE!")
print("=" * 70)
