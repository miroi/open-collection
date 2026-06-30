import os
import subprocess
import numpy as np
from ase import Atoms
from ase.build import bulk
import shutil

# --- 0. Check Elk setup ---
elk_exe = '/home/milias/work/software/elk/elk-11.0.2/src/elk'
species_path = '/home/milias/work/software/elk/elk-11.0.2/species/'

print("="*60)
print("Setting up calculation for Rutherfordium (Rf)")
print("="*60)

# --- 1. Define the hcp structure ---
a = 3.8  # Å
c = 6.2  # Å

# Create hcp structure using ASE's bulk function
Rf = bulk('Rf', 'hcp', a=a, c=c)

print(f"Rutherfordium hcp structure:")
print(f"a = {a:.3f} Å, c = {c:.3f} Å")
print(f"Number of atoms: {len(Rf)}")
print()

# --- 2. Set up the Elk calculation directory ---
# Clean up previous calculation
if os.path.exists('./rf_scf'):
    print("Removing previous calculation directory...")
    shutil.rmtree('./rf_scf')

# Create directory
os.makedirs('./rf_scf', exist_ok=True)

# --- 3. Create GEOMETRY file manually (Elk format) ---
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

# --- 4. Create elk.in file with proper block format ---
# IMPORTANT: Each parameter must be on its own line, followed by its value on the next line
# A blank line is required after the tasks block
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
10.0

rgkmax
7.0

swidth
0.01

nempty
10

maxscl
50

epspot
1e-5

chgmult
0.5

maxit
30
"""
with open('./rf_scf/elk.in', 'w') as f:
    f.write(elk_in_content)

print("✅ elk.in file created")

# --- 5. Create SPECIES file ---
species_content = """Rf.in
"""
with open('./rf_scf/SPECIES', 'w') as f:
    f.write(species_content)

print("✅ SPECIES file created")

print("\nInput files written to ./rf_scf/")
print("Files in ./rf_scf/:")
for f in os.listdir('./rf_scf'):
    size = os.path.getsize(os.path.join('./rf_scf', f))
    print(f"  {f} ({size} bytes)")

# Print the contents of elk.in for debugging
print("\nContents of elk.in:")
with open('./rf_scf/elk.in', 'r') as f:
    print(f.read())

# --- 6. Run the calculation by directly calling Elk ---
print("\n" + "="*60)
print("Running Elk calculation for Rutherfordium (Rf)")
print("="*60)

try:
    # Run Elk directly in the calculation directory
    result = subprocess.run(
        [elk_exe],
        cwd='./rf_scf',
        capture_output=True,
        text=True,
        timeout=600  # 10 minute timeout
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
                energy_line = lines[-1].strip()
                print(f"\n✅ Calculation completed successfully!")
                print(f"Total energy line: {energy_line}")
                try:
                    energy_parts = energy_line.split()
                    if len(energy_parts) > 0:
                        energy_ha = float(energy_parts[-1])
                        energy_ev = energy_ha * 27.2114
                        print(f"Total energy: {energy_ha:.10f} Hartree")
                        print(f"Total energy: {energy_ev:.6f} eV")
                        print(f"Energy per atom: {energy_ev/len(Rf):.6f} eV")
                except Exception as e:
                    print(f"Could not parse energy: {e}")
    else:
        print("\n❌ TOTENERGY.OUT not found. Calculation may have failed.")
        
        # Check for error files
        error_files = ['ERROR.OUT', 'elk.log', 'elk.err', 'STOP']
        for err_file in error_files:
            err_path = f'./rf_scf/{err_file}'
            if os.path.exists(err_path):
                print(f"\nContents of {err_file}:")
                with open(err_path, 'r') as f:
                    content = f.read()
                    print(content)
        
        # List all files
        print("\nAll files in ./rf_scf/:")
        for f in os.listdir('./rf_scf'):
            size = os.path.getsize(os.path.join('./rf_scf', f))
            print(f"  {f} ({size} bytes)")
                    
except subprocess.TimeoutExpired:
    print("❌ Calculation timed out after 10 minutes")
except Exception as e:
    print(f"❌ An error occurred: {e}")
