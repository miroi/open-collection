import os
import subprocess
import numpy as np
from ase.build import bulk
import shutil

# --- 0. Setup paths ---
elk_exe = '/home/milias/work/software/elk/elk-11.0.2/src/elk'
species_path = '/home/milias/work/software/elk/elk-11.0.2/species/'

print("="*60)
print("Setting up calculation for Rutherfordium (Rf)")
print("="*60)

# --- 1. Define the hcp structure ---
a = 3.8  # Å
c = 6.2  # Å

# Create hcp structure
Rf = bulk('Rf', 'hcp', a=a, c=c)

print(f"Rutherfordium hcp structure:")
print(f"a = {a:.3f} Å, c = {c:.3f} Å")
print(f"c/a ratio = {c/a:.4f}")
print(f"Number of atoms: {len(Rf)}")
print()

# --- 2. Set up the Elk calculation directory ---
if os.path.exists('./rf_scf'):
    print("Removing previous calculation directory...")
    shutil.rmtree('./rf_scf')

os.makedirs('./rf_scf', exist_ok=True)
print("✅ Calculation directory created")

# --- 3. Create GEOMETRY file ---
geometry_content = f"""Rutherfordium (Rf) hcp structure
      {a:.6f}    {a:.6f}    {c:.6f}    90.000000    90.000000   120.000000
    0.00000000  0.00000000  0.00000000  0.00000000  0.00000000  0.00000000
    0.33333333  0.66666667  0.50000000  0.00000000  0.00000000  0.00000000
    2  1  0.00000000  0.00000000  0.00000000
'Rf.in'  1  'Rf.in'  1
"""

with open('./rf_scf/GEOMETRY', 'w') as f:
    f.write(geometry_content)
print("✅ GEOMETRY file created")

# --- 4. Create elk.in file with spin-orbit parameters ---
elk_in_content = """tasks
0

spinpol
.true.

spinorb
.true.

stype
2

ngridk
8 8 8

gmaxvr
12.0

rgkmax
8.0

swidth
0.01

nempty
15

maxscl
150

epspot
1e-6

! Additional parameters for better convergence
xctype
20

! Note: 'nspins' is NOT needed - determined automatically
! 'chgmult' and 'maxit' are NOT valid in this version
"""
with open('./rf_scf/elk.in', 'w') as f:
    f.write(elk_in_content)
print("✅ elk.in file created")

# --- 5. Create SPECIES file ---
with open('./rf_scf/SPECIES', 'w') as f:
    f.write("Rf.in\n")
print("✅ SPECIES file created")

# --- 6. Verify the species file is accessible ---
rf_species = os.path.join(species_path, 'Rf.in')
if os.path.exists(rf_species):
    print(f"✅ Species file found: {rf_species}")
    # Verify the species file has the correct format
    with open(rf_species, 'r') as f:
        first_line = f.readline().strip()
        print(f"   First line: {first_line}")
else:
    print(f"❌ Species file not found: {rf_species}")
    print("   Please ensure Rf.in is in the species directory")

print("\nInput files written to ./rf_scf/")
print("Files in ./rf_scf/:")
for f in os.listdir('./rf_scf'):
    size = os.path.getsize(os.path.join('./rf_scf', f))
    print(f"  {f} ({size} bytes)")

# --- 7. Run the calculation ---
print("\n" + "="*60)
print("Running two-component SO-SCF calculation for Rutherfordium (Rf)")
print("="*60)
print(f"Elk executable: {elk_exe}")
print(f"Species path: {species_path}")
print(f"Calculation directory: ./rf_scf")
print(f"k-point grid: 8x8x8")
print(f"Spin-orbit coupling: Enabled")
print("="*60 + "\n")

try:
    # Run Elk
    result = subprocess.run(
        [elk_exe],
        cwd='./rf_scf',
        capture_output=True,
        text=True,
        timeout=1800  # 30 minute timeout for superheavy element
    )
    
    print("Elk output:")
    print(result.stdout)
    if result.stderr:
        print("Elk errors:")
        print(result.stderr)
    
    # Check if calculation succeeded
    if os.path.exists('./rf_scf/TOTENERGY.OUT'):
        with open('./rf_scf/TOTENERGY.OUT', 'r') as f:
            lines = f.readlines()
            if lines:
                # The last line contains the total energy
                energy_line = lines[-1].strip()
                print(f"\n" + "="*60)
                print("✅ SCF calculation converged successfully!")
                print("="*60)
                print(f"Total energy line: {energy_line}")
                
                try:
                    # Parse energy (last number in the line)
                    energy_parts = energy_line.split()
                    if len(energy_parts) > 0:
                        energy_ha = float(energy_parts[-1])
                        energy_ev = energy_ha * 27.2114  # Hartree to eV
                        
                        print(f"\nTotal energy: {energy_ha:.10f} Hartree")
                        print(f"Total energy: {energy_ev:.6f} eV")
                        print(f"Energy per atom: {energy_ev/len(Rf):.6f} eV")
                        
                        # Save energy to file
                        with open('./rf_scf/energy.txt', 'w') as f:
                            f.write(f"Total energy (Hartree): {energy_ha:.10f}\n")
                            f.write(f"Total energy (eV): {energy_ev:.6f}\n")
                            f.write(f"Energy per atom (eV): {energy_ev/len(Rf):.6f}\n")
                        print("✅ Energy saved to ./rf_scf/energy.txt")
                        
                except Exception as e:
                    print(f"Could not parse energy: {e}")
            else:
                print("TOTENERGY.OUT is empty")
    else:
        print("\n❌ TOTENERGY.OUT not found. Calculation may have failed.")
        
        # Check for error files
        error_files = ['ERROR.OUT', 'elk.log', 'elk.err', 'STOP']
        found_error = False
        for err_file in error_files:
            err_path = f'./rf_scf/{err_file}'
            if os.path.exists(err_path):
                found_error = True
                print(f"\nContents of {err_file}:")
                with open(err_path, 'r') as f:
                    content = f.read()
                    print(content[:1000])  # Print first 1000 chars
                    if len(content) > 1000:
                        print("... (truncated)")
        
        if not found_error:
            print("No error files found. Calculation may still be running or died unexpectedly.")
        
        # List all files
        print("\nAll files in ./rf_scf/:")
        for f in sorted(os.listdir('./rf_scf')):
            path = os.path.join('./rf_scf', f)
            if os.path.isfile(path):
                size = os.path.getsize(path)
                print(f"  {f} ({size} bytes)")
            else:
                print(f"  {f}/ (directory)")
                    
except subprocess.TimeoutExpired:
    print("❌ Calculation timed out after 30 minutes")
    print("   Superheavy elements often require more time for SCF convergence.")
    print("   You may need to increase the timeout or run in a background job.")
    
except KeyboardInterrupt:
    print("\n⚠️ Calculation interrupted by user")
    print("   You can check the output files in ./rf_scf/")
    
except Exception as e:
    print(f"❌ An unexpected error occurred: {e}")
    import traceback
    traceback.print_exc()
