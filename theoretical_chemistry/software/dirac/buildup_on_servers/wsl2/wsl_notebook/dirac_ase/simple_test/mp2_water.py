# Example of the use of the ASE interface
# 20-1-2025, L. Visscher
from ase import Atoms
from ase.build import molecule
from ase.units import Ha
from ase_dirac import DIRAC

# check pam in the $PATH variable

import os
from pathlib import Path

def find_file_in_path(filename):
    # Get the system PATH and split it (';' for Windows, ':' for Linux/macOS)
    path_dirs = os.environ.get("PATH", "").split(os.pathsep)

    for directory in path_dirs:
        # Combine directory with our filename
        full_path = Path(directory) / filename
        
        try:
            # resolve(strict=True) will raise FileNotFoundError if the file isn't there
            resolved_path = full_path.resolve(strict=True)
            
            # Double-check it's a file, not just a directory that happens to have this name
            if resolved_path.is_file():
                return resolved_path
                
        except (FileNotFoundError, PermissionError):
            # If not found or no permission, just move to the next directory in PATH
            continue
            
    return None

target_file = "pam" 
result = find_file_in_path(target_file)
if result:
    print(f"Success! pam script found at: {result}")
else:
    print(f"Could not find '{target}' in any $PATH directory.")
    exit(-1)    

# check dirac.x in pam directory
target_file = "dirac.x" 
result = find_file_in_path(target_file)
if result:
    print(f"Success! dirac.x executable found at: {result}")
else:
    print(f"Could not find '{target}' in any $PATH directory.")
    exit(-1)    

# check dirac.x has all libs connected
import subprocess
def check_linux_dependencies(executable_path):
    try:
        # Run ldd and capture output
        result = subprocess.run(['ldd', executable_path], capture_output=True, text=True)
        if "not found" in result.stdout:
            print("❌ Missing libraries detected:")
            for line in result.stdout.split('\n'):
                if "not found" in line:
                    print(line.strip())
        else:
            print("✅ All libraries are connected to dirac.x.")
            
    except FileNotFoundError:
        print("Error: 'ldd' command not found. Are you on Linux?")

check_linux_dependencies(result)


# Some simple small molecules taken from the G2 set in the ASE database
#molecules = ['H2O','N2','F2','Cl2','CH4','C2H4']
molecules = ['H2O']
# Defines the **HAMILTONIAN input block, note that two lines input for the full DCG Hamiltonian
#hamiltonian_inputs = ['.nonrel','.x2cmmf','.gaunt\n.dossss']
hamiltonian_inputs = ['.nonrel']
# Labeling the different inputs with a descriptive string
#calculation_labels = ['NR-MP2','X2Cmmf-MP2','DCG-MP2']
calculation_labels = ['NR-MP2']
# Making an empty list to store results (energies) for each molecule
results = []

# Outermost loop over different molecules
for mol in molecules:
    ase_molecule = molecule(mol)
    energy = []
    # Loop over the three different Hamiltonians that we consider
    for ham, calc in zip(hamiltonian_inputs,calculation_labels):
        label=calc+'_'+mol
        try:
            ase_molecule.calc = DIRAC(
              hamiltonian={ham: ''},
              wave_function={'.scf': '', '.mp2': '',
                             '*scf': {'.ergcnv': '1.E-8 1.E-6',
                                      '.maxitr': '35'},
                             '*mp2cal': {'.occup': 'all','.virtual': 'all'},
                            },
              molecule={'*basis': {'.default': 'cc-pVDZ'}},
              label=label)
            energy.append(ase_molecule.get_potential_energy() / Ha)
        except:
            print (f'Calculation {label} could not be run correctly, please check')
            energy.append(0)
    results.append(energy)
    
# Print results in a table
#print(' Møller-Plesset second order (MP2) energies computed with different Hamiltonians\n')
#print(80*'-')
#print('  {:<15} {:>20} {:>20} {:>20}'.format('Molecule',*calculation_labels))
#print(80*'-')
for mol, result in zip(molecules,results):
#    print ('  {:<15} {:>20.8f} {:>20.8f} {:>20.8f}'.format(mol,*result))
   # print(mol, result)

    print('mol=',mol)
    print('result=',result)

#print(80*'-')

