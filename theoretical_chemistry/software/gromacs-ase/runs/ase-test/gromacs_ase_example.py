import os
import sys
from ase.calculators.gromacs import Gromacs

# 1. Define the exact path to your custom GROMACS binary folder
gmx_bin_dir = "/home/miroi/work/software/gromacs/gromacs_cloned/build_gnu/bin"

# 2. Configure the ASE environment variables for GROMACS execution
# GMXCMD_PREF handles your parallel wrapper (mpirun + core allocation)
os.environ['GMXCMD_PREF'] = "mpirun -np 2"

# Use the absolute path to your custom gmx_mpi executable
os.environ['ASE_GROMACS_COMMAND'] = os.path.join(gmx_bin_dir, "gmx_mpi")

# 3. Define your initial structure template
input_structure = '1CRN.pdb' 

print(f"Initializing ASE GROMACS Calculator...")
print(f"Command prefix: {os.environ['GMXCMD_PREF']}")
print(f"Executable target: {os.environ['ASE_GROMACS_COMMAND']}")

# Initialize the calculator simply; it naturally pulls from os.environ
calc = Gromacs(clean=True)

# 4. Convert PDB to GROMACS format and generate topology
calc.set_own_params_runs('extra_pdb2gmx_parameters', '-ignh')
calc.set_own_params_runs('init_structure', input_structure)
calc.generate_topology_and_g96file()
calc.write_input()

# 5. Define the simulation box boundaries (gmx editconf)
calc.set_own_params_runs('extra_editconf_parameters', '-bt cubic -c -d 0.8')
calc.run_editconf()

# 6. Solvate the system (gmx solvate)
calc.set_own_params_runs('extra_genbox_parameters', '-cs spc216.gro')
calc.run_genbox()

# 7. Compile parameters and run the energy minimization
print("Compiling parameters and running energy minimization via MPI pipeline...")
calc.generate_gromacs_run_file()
calc.run()

print("Simulation finished successfully!")

