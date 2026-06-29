import os
from ase.calculators.gromacs import Gromacs, GromacsProfile

# 1. Define the exact path to your custom GROMACS executable folder
gmx_bin_dir = "/home/miroi/work/software/gromacs/gromacs_cloned/build_gnu/bin"
gmx_executable = os.path.join(gmx_bin_dir, "gmx_mpi")

# 2. Inject the mpirun wrapper prefix directly into the profile command definition
# Adjust "-np 2" to change the total number of parallel processor ranks
mpi_prefix = "mpirun -np 2"
custom_parallel_command = f"{mpi_prefix} {gmx_executable}"

# 3. Create the profile instructing ASE to route execution through your MPI environment
profile = GromacsProfile(command=custom_parallel_command)

# 4. Define your initial structure template
input_structure = '1CRN.pdb' 

print(f"Initializing ASE GROMACS Calculator using: {custom_parallel_command}")
calc = Gromacs(clean=True, profile=profile)

# 5. Convert PDB to GROMACS format and generate topology
calc.set_own_params_runs('extra_pdb2gmx_parameters', '-ignh')
calc.set_own_params_runs('init_structure', input_structure)
calc.generate_topology_and_g96file()
calc.write_input()

# 6. Define the simulation box boundaries (gmx editconf)
calc.set_own_params_runs('extra_editconf_parameters', '-bt cubic -c -d 0.8')
calc.run_editconf()

# 7. Solvate the system (gmx solvate)
calc.set_own_params_runs('extra_genbox_parameters', '-cs spc216.gro')
calc.run_genbox()

# 8. Compile calculations and run the energy minimization
print("Compiling parameters and running energy minimization via MPI pipeline...")
calc.generate_gromacs_run_file()
calc.run()

print("Simulation finished successfully!")

