import os
import subprocess
import shutil

# --- Paths ---
elk_exe = '/home/milias/work/software/elk/elk-11.0.2/src/elk'
species_dir = '/home/milias/work/software/elk/elk-11.0.2/species/'

# --- Parameters for Rf hcp ---
a = 3.8
c = 6.2

# --- Clean and create directory ---
if os.path.exists('./rf_run'):
    shutil.rmtree('./rf_run')
os.makedirs('./rf_run')

# --- Write GEOMETRY file ---
with open('./rf_run/GEOMETRY', 'w') as f:
    f.write(f"""Rutherfordium hcp
     {a:.6f}    {a:.6f}    {c:.6f}    90.000000    90.000000   120.000000
    0.00000000  0.00000000  0.00000000  0.00000000  0.00000000  0.00000000
    0.33333333  0.66666667  0.50000000  0.00000000  0.00000000  0.00000000
    2  1  0.00000000  0.00000000  0.00000000
'Rf.in'  1  'Rf.in'  1
""")

# --- Write elk.in file ---
with open('./rf_run/elk.in', 'w') as f:
    f.write("""tasks
0

spinpol
.true.

spinorb
.true.

stype
2

ngridk
6 6 6

gmaxvr
10.0

rgkmax
7.0

swidth
0.01

nempty
15

maxscl
100

epspot
1e-6
""")

# --- Write SPECIES file ---
with open('./rf_run/SPECIES', 'w') as f:
    f.write("Rf.in\n")

print("Input files created in ./rf_run/")

# --- Run Elk ---
print("Running Elk...")
os.chdir('./rf_run')
result = subprocess.run([elk_exe], capture_output=True, text=True)
os.chdir('..')

# --- Output results ---
print("\nElk output:")
print(result.stdout)
if result.stderr:
    print("Errors:")
    print(result.stderr)

# --- Check for energy ---
if os.path.exists('./rf_run/TOTENERGY.OUT'):
    with open('./rf_run/TOTENERGY.OUT', 'r') as f:
        lines = f.readlines()
        if lines:
            print(f"\n✅ Calculation finished!")
            print(f"Last line: {lines[-1].strip()}")
else:
    print("\n❌ TOTENERGY.OUT not found")
    if os.path.exists('./rf_run/ERROR.OUT'):
        print("\nERROR.OUT:")
        with open('./rf_run/ERROR.OUT', 'r') as f:
            print(f.read())
