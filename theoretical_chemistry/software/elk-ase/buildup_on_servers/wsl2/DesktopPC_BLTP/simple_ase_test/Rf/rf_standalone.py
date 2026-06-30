import os
import subprocess
import shutil
import math

# --- Paths ---
elk_exe = '/home/milias/work/software/elk/elk-11.0.2/src/elk'
species_dir = '/home/milias/work/software/elk/elk-11.0.2/species/'

# --- Parameters for Rf hcp ---
a = 3.8   # Å (predicted)
c = 6.2   # Å (predicted)

# Convert to lattice vectors for hcp
a1x = a
a1y = 0.0
a1z = 0.0
a2x = -a/2.0
a2y = a * math.sqrt(3.0) / 2.0
a2z = 0.0
a3x = 0.0
a3y = 0.0
a3z = c

print("="*60)
print("Setting up calculation for Rutherfordium (Rf)")
print("="*60)

print(f"Rf hcp structure:")
print(f"a = {a:.3f} Å, c = {c:.3f} Å")
print(f"c/a ratio = {c/a:.4f}")
print()

# --- Check if Rf.in exists in species directory ---
rf_species_path = os.path.join(species_dir, 'Rf.in')
if not os.path.exists(rf_species_path):
    print(f"❌ Rf.in not found in {species_dir}")
    print("Available species files:")
    for f in sorted(os.listdir(species_dir)):
        if f.endswith('.in'):
            print(f"  {f}")
    exit(1)
else:
    print(f"✅ Found Rf.in in {species_dir}")
    # Show first few lines
    with open(rf_species_path, 'r') as f:
        lines = f.readlines()[:5]
        print("First 5 lines of Rf.in:")
        for line in lines:
            print(f"  {line.rstrip()}")

# --- Clean and create directory ---
if os.path.exists('./rf_run'):
    print("Removing previous calculation directory...")
    shutil.rmtree('./rf_run')
os.makedirs('./rf_run')
print("✅ Calculation directory created")

# --- Copy Rf.in to run directory ---
shutil.copy2(rf_species_path, './rf_run/Rf.in')
print("✅ Copied Rf.in to run directory")

# --- Create elk.in file (same format as working Tl) ---
elk_in_content = f"""! Rutherfordium (Rf) hcp structure with spin-orbit coupling

! SCF calculation
tasks
  0

! Use Broyden mixing
mixtype
  3

! Lattice vectors for hcp
avec
  {a1x:.6f}  {a1y:.6f}  {a1z:.6f}
  {a2x:.6f}  {a2y:.6f}  {a2z:.6f}
  {a3x:.6f}  {a3y:.6f}  {a3z:.6f}

! Atoms (species file is in current directory)
atoms
  1                                 : nspecies
  'Rf.in'                           : spfname
  2                                 : natoms; atposl below
  0.0  0.0  0.0
  0.33333333  0.66666667  0.50000000

! k-point grid
ngridk
  8  8  8

! Spin-orbit coupling
spinpol
  .true.

spinorb
  .true.

stype
  2

! Basis and cutoff
gmaxvr
  8.0

rgkmax
  6.0

! Smearing for metallic system
swidth
  0.01

! Empty bands (more for heavy elements)
nempty
  15

! SCF control (more iterations for heavy elements)
maxscl
  150

epspot
  1e-6
"""

with open('./rf_run/elk.in', 'w') as f:
    f.write(elk_in_content)
print("✅ elk.in file created")

print("\nInput files written to ./rf_run/")
print("Files in ./rf_run/:")
for f in os.listdir('./rf_run'):
    size = os.path.getsize(os.path.join('./rf_run', f))
    print(f"  {f} ({size} bytes)")

# --- Set OpenMP threads to 1 ---
os.environ['OMP_NUM_THREADS'] = '1'
os.environ['MKL_NUM_THREADS'] = '1'

# --- Run the calculation ---
print("\n" + "="*60)
print("Running Elk for Rutherfordium (Rf)")
print("="*60)
print(f"Using species file: ./rf_run/Rf.in")
print(f"k-point grid: 8x8x8")
print(f"Spin-orbit coupling: Enabled")
print("="*60 + "\n")

try:
    os.chdir('./rf_run')
    result = subprocess.run(
        [elk_exe],
        capture_output=True,
        text=True,
        timeout=1800  # 30 minutes for superheavy element
    )
    os.chdir('..')
    
    print("Elk output:")
    print(result.stdout)
    if result.stderr:
        print("Elk stderr:")
        print(result.stderr)
    
    # Check if calculation succeeded
    if os.path.exists('./rf_run/TOTENERGY.OUT'):
        with open('./rf_run/TOTENERGY.OUT', 'r') as f:
            lines = f.readlines()
            if lines:
                print("\n" + "="*60)
                print("✅ Calculation completed successfully!")
                print("="*60)
                print(f"Total energy: {lines[-1].strip()}")
                
                try:
                    parts = lines[-1].split()
                    if len(parts) > 0:
                        energy_ha = float(parts[-1])
                        energy_ev = energy_ha * 27.2114
                        print(f"\nEnergy in Hartree: {energy_ha:.10f} Ha")
                        print(f"Energy in eV: {energy_ev:.6f} eV")
                        print(f"Energy per atom: {energy_ev/2:.6f} eV")
                        
                        # Save energy
                        with open('energy.txt', 'w') as f:
                            f.write(f"Total energy: {energy_ha:.10f} Ha\n")
                            f.write(f"Total energy: {energy_ev:.6f} eV\n")
                            f.write(f"Energy per atom: {energy_ev/2:.6f} eV\n")
                        print("\n✅ Energy saved to ./rf_run/energy.txt")
                except Exception as e:
                    print(f"Could not parse energy: {e}")
            else:
                print("TOTENERGY.OUT is empty")
    else:
        print("\n❌ TOTENERGY.OUT not found.")
        
        # Check for error files
        for fname in ['ERROR.OUT', 'elk.log', 'elk.err']:
            if os.path.exists(f'./rf_run/{fname}'):
                print(f"\nContents of {fname}:")
                with open(f'./rf_run/{fname}', 'r') as f:
                    content = f.read()
                    print(content[:500])
                    if len(content) > 500:
                        print("... (truncated)")
        
        # Check if GEOMETRY.OUT was created
        if os.path.exists('./rf_run/GEOMETRY.OUT'):
            print("\n✅ GEOMETRY.OUT was created!")
            with open('./rf_run/GEOMETRY.OUT', 'r') as f:
                lines = f.readlines()[:10]
                print("First 10 lines:")
                for line in lines:
                    print(f"  {line.rstrip()}")
        
        print("\nAll files in ./rf_run/:")
        for f in sorted(os.listdir('./rf_run')):
            path = os.path.join('./rf_run', f)
            if os.path.isfile(path):
                size = os.path.getsize(path)
                print(f"  {f} ({size} bytes)")
            else:
                print(f"  {f}/ (directory)")
                    
except subprocess.TimeoutExpired:
    print("❌ Calculation timed out after 30 minutes")
    print("   Rf is a superheavy element and may require more time.")
    print("   Check ./rf_run/ for partial output files.")
except KeyboardInterrupt:
    print("\n⚠️ Calculation interrupted by user")
    print("   Check ./rf_run/ for partial output files.")
except Exception as e:
    print(f"❌ Error: {e}")
    import traceback
    traceback.print_exc()
