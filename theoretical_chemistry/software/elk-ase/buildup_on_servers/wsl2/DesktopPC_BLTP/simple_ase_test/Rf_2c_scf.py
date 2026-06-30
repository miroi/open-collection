import os
import subprocess
import numpy as np
from ase import Atoms
from ase.calculators.elk import ELK, ElkProfile

# --- 0. Debugging: Check if Elk works ---
elk_exe = '/home/milias/work/software/elk/elk-11.0.2/src/elk'
species_path = '/home/milias/work/software/elk/elk-11.0.2/species/'

# Check if executable exists and is runnable
print("="*60)
print("DEBUG: Checking Elk setup")
print("="*60)
print(f"Elk executable: {elk_exe}")
print(f"Exists: {os.path.exists(elk_exe)}")
print(f"Is executable: {os.access(elk_exe, os.X_OK)}")

# Try to run elk --version
try:
    result = subprocess.run([elk_exe, '--version'], 
                          capture_output=True, text=True, timeout=5)
    print(f"Elk version output: {result.stdout.strip()}")
except Exception as e:
    print(f"Could not run elk: {e}")

# Check if Rf.in exists
rf_species = os.path.join(species_path, 'Rf.in')
print(f"\nRf.in species file: {rf_species}")
print(f"Exists: {os.path.exists(rf_species)}")

# If Rf.in exists, print first few lines
if os.path.exists(rf_species):
    with open(rf_species, 'r') as f:
        lines = f.readlines()[:10]
    print("First 10 lines of Rf.in:")
    for line in lines:
        print(f"  {line.rstrip()}")
print("="*60 + "\n")

# --- 1. Define the hcp structure ---
a = 3.8  # Å
c = 6.2  # Å

from ase.build import bulk
Rf = bulk('Rf', 'hcp', a=a, c=c)

print(f"Rutherfordium crystal structure:")
print(f"a = {a:.3f} Å, c = {c:.3f} Å")
print(f"Number of atoms: {len(Rf)}")

# --- 2. Set up the Elk calculator with verbose output ---
elk_profile = ElkProfile(command=elk_exe, sppath=species_path)

# Clean up previous calculation directory if it exists
import shutil
if os.path.exists('./rf_scf'):
    print("\nRemoving previous calculation directory...")
    shutil.rmtree('./rf_scf')

calc = ELK(profile=elk_profile,
           directory='./rf_scf',
           tasks=[0],
           spinpol=True,
           spinorb=True,
           ngridk=[8, 8, 8],  # Reduced for testing
           gmaxvr=10.0,       # Reduced for testing
           rgkmax=7.0,        # Reduced for testing
           swidth=0.01,
           nempty=10,
           maxscl=50,
           epspot=1e-5,       # Looser tolerance for testing
           fsmtype=0,
           stype=2,
           nspins=4,
           chgmult=0.5,
           maxit=30,
           )

Rf.calc = calc  # New syntax

# --- 3. Run the calculation ---
print("\n" + "="*60)
print("Starting two-component SO-SCF calculation for Rutherfordium (Rf)")
print("="*60)
print(f"Calculation directory: ./rf_scf")
print("="*60 + "\n")

# Check what files are created in the calculation directory
try:
    # Create the directory and write input files manually to see what's happening
    os.makedirs('./rf_scf', exist_ok=True)
    
    # Write input files
    calc.write_input(Rf)
    
    print("Input files written to ./rf_scf/")
    print("Files in ./rf_scf/:")
    for f in os.listdir('./rf_scf'):
        if os.path.isfile(os.path.join('./rf_scf', f)):
            size = os.path.getsize(os.path.join('./rf_scf', f))
            print(f"  {f} ({size} bytes)")
    
    # Now run the calculation
    energy = Rf.get_potential_energy()
    print(f"✅ SCF calculation converged successfully!")
    print(f"Total energy: {energy:.6f} eV")
    print(f"Energy per atom: {energy/len(Rf):.6f} eV")
    
except Exception as e:
    print(f"❌ An error occurred: {e}")
    print("\n=== DEBUG: Checking calculation directory ===")
    if os.path.exists('./rf_scf'):
        print(f"Files in ./rf_scf/:")
        for f in os.listdir('./rf_scf'):
            path = os.path.join('./rf_scf', f)
            if os.path.isfile(path):
                size = os.path.getsize(path)
                print(f"  {f} ({size} bytes)")
                # Print first few lines of key files
                if f in ['INPUT', 'GEOMETRY', 'SPECIES', 'elk.log']:
                    print(f"  --- First 5 lines of {f}:")
                    try:
                        with open(path, 'r') as file:
                            lines = file.readlines()[:5]
                            for line in lines:
                                print(f"    {line.rstrip()}")
                    except:
                        pass
    else:
        print("No calculation directory found!")
