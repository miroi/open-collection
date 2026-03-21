import os
from ase.build import bulk
from ase.calculators.lammpsrun import LAMMPS

# 1. SET ENVIRONMENT VARIABLES
# Replace '/usr/local/bin/lmp_serial' with the actual path to your LAMMPS binary
# You can find this path by typing 'which lmp_serial' or 'which lmp' in your terminal.
lmp_exe = '/usr/bin/lmp' 
os.environ['ASE_LAMMPSRUN_COMMAND'] = lmp_exe
os.environ['LAMMPS_COMMAND'] = lmp_exe

# 2. DEFINE PATHS
# Use the full absolute path to your potential file
pot_file_path = '/usr/share/lammps/potentials/NiAlH_jea.eam.alloy'
pot_filename = os.path.basename(pot_file_path) # Extract 'NiAlH_jea.eam.alloy'

# 3. SETUP SYSTEM
atoms = bulk('Ni', cubic=True)

# 4. CONFIGURE CALCULATOR
# 'pair_coeff' must use the filename (not path) because ASE copies it to a temp folder
parameters = {
    'pair_style': 'eam/alloy',
    'pair_coeff': [f'* * {pot_filename} Ni'] 
}

# 'files' must use the full path so ASE can find and copy it
calc = LAMMPS(files=[pot_file_path], **parameters)
atoms.calc = calc

# 5. RUN
try:
    energy = atoms.get_potential_energy()
    print(f"Calculation Successful!")
    print(f"Potential Energy: {energy:.4f} eV")
except Exception as e:
    print(f"Error running LAMMPS: {e}")

