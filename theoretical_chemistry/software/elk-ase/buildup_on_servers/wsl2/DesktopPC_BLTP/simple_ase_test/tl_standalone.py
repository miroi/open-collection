import os
import subprocess
import shutil
import math

# --- Paths ---
elk_exe = '/home/milias/work/software/elk/elk-11.0.2/src/elk'
species_dir = '/home/milias/work/software/elk/elk-11.0.2/species/'

# --- Parameters for Tl hcp ---
a = 3.45   # Å
c = 5.52   # Å

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
print("Setting up calculation for Thallium (Tl)")
print("="*60)

print(f"Tl hcp structure:")
print(f"a = {a:.3f} Å, c = {c:.3f} Å")
print(f"c/a ratio = {c/a:.4f}")
print()

# --- Check if Tl.in exists in species directory ---
tl_species_path = os.path.join(species_dir, 'Tl.in')
if not os.path.exists(tl_species_path):
    print(f"❌ Tl.in not found in {species_dir}")
    print("Available species files:")
    for f in sorted(os.listdir(species_dir)):
        if f.endswith('.in'):
            print(f"  {f}")
    exit(1)
else:
    print(f"✅ Found Tl.in in {species_dir}")
    # Show first few lines
    with open(tl_species_path, 'r') as f:
        lines = f.readlines()[:5]
        print("First 5 lines of Tl.in:")
        for line in lines:
            print(f"  {line.rstrip()}")

# --- Clean and create directory ---
if os.path.exists('./tl_run'):
    print("Removing previous calculation directory...")
    shutil.rmtree('./tl_run')
os.makedirs('./tl_run')
print("✅ Calculation directory created")

# --- Create elk.in file (matching Si format exactly) ---
elk_in_content = f"""! Thallium (Tl) hcp structure with spin-orbit coupling

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

! Species path
sppath
  {species_dir}

! Atoms
atoms
  1                                 : nspecies
  'Tl.in'                           : spfname
  2                                 : natoms; atposl below
  0.0  0.0  0.0
  0.33333333  0.66666667  0.50000000

! k-point grid
ngridk
  6  6  6

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

! Empty bands
nempty
  12

! SCF control
maxscl
  100

epspot
  1e-6
"""

with open('./tl_run/elk.in', 'w') as f:
    f.write(elk_in_content)
print("✅ elk.in file created")

print("\nInput files written to ./tl_run/")
print("Files in ./tl_run/:")
for f in os.listdir('./tl_run'):
    size = os.path.getsize(os.path.join('./tl_run', f))
    print(f"  {f} ({size} bytes)")

# --- Set OpenMP threads to 1 for debugging ---
os.environ['OMP_NUM_THREADS'] = '1'
os.environ['MKL_NUM_THREADS'] = '1'

# --- Run the calculation ---
print("\n" + "="*60)
print("Running Elk for Thallium (Tl)")
print("="*60)
print(f"Using species file: {tl_species_path}")
print("="*60 + "\n")

try:
    os.chdir('./tl_run')
    result = subprocess.run(
        [elk_exe],
        capture_output=True,
        text=True,
        timeout=600
    )
    os.chdir('..')
    
    print("Elk output:")
    print(result.stdout)
    if result.stderr:
        print("Elk stderr:")
        print(result.stderr)
    
    # Check if calculation succeeded
    if os.path.exists('./tl_run/TOTENERGY.OUT'):
        with open('./tl_run/TOTENERGY.OUT', 'r') as f:
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
                        print(f"Energy in Hartree: {energy_ha:.10f} Ha")
                        print(f"Energy in eV: {energy_ev:.6f} eV")
                        print(f"Energy per atom: {energy_ev/2:.6f} eV")
                except:
                    pass
    else:
        print("\n❌ TOTENERGY.OUT not found.")
        
        # Check for error files
        for fname in ['ERROR.OUT', 'elk.log', 'elk.err']:
            if os.path.exists(f'./tl_run/{fname}'):
                print(f"\nContents of {fname}:")
                with open(f'./tl_run/{fname}', 'r') as f:
                    content = f.read()
                    print(content[:500])
                    if len(content) > 500:
                        print("... (truncated)")
        
        print("\nAll files in ./tl_run/:")
        for f in sorted(os.listdir('./tl_run')):
            path = os.path.join('./tl_run', f)
            if os.path.isfile(path):
                size = os.path.getsize(path)
                print(f"  {f} ({size} bytes)")
            else:
                print(f"  {f}/ (directory)")
                    
except subprocess.TimeoutExpired:
    print("❌ Calculation timed out after 10 minutes")
except Exception as e:
    print(f"❌ Error: {e}")
    import traceback
    traceback.print_exc()
