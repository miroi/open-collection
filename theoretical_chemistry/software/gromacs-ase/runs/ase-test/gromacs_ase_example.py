import os
from ase.calculators.gromacs import Gromacs, GromacsProfile

# 1. Define the exact path to your custom GROMACS executable folder
gmx_bin_dir = "/home/miroi/work/software/gromacs/gromacs_cloned/build_gnu/bin"
gmx_executable = os.path.join(gmx_bin_dir, "gmx_mpi")

# 2. Create the ASE profile pointing to your custom executable
profile = GromacsProfile(command=gmx_executable)

# 3. Provide your initial structural template file
input_structure = '1CRN.pdb' 

print(f"Initializing ASE GROMACS Calculator using: {gmx_executable}")
# Pass the profile into the calculator initialization block
calc = Gromacs(clean=True, profile=profile)

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

# 7. Generate and execute the run file (gmx grompp & mdrun)
print("Compiling parameters and running energy minimization...")
calc.generate_gromacs_run_file()
calc.run()

print("Simulation finished successfully!")

