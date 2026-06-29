import sys
from ase.calculators.gromacs import Gromacs

# 1. Provide your initial structural template file
# Replace 'protein.pdb' with your file (e.g., a simple peptide or protein)
input_structure = '1CRN.pdb' 

print("Initializing ASE GROMACS Calculator...")
# 'clean=True' removes old GROMACS temporary files between steps
calc = Gromacs(clean=True)

# 2. Convert PDB to GROMACS format and generate topology
# -ignh tells pdb2gmx to ignore existing hydrogens and use the force field's
calc.set_own_params_runs('extra_pdb2gmx_parameters', '-ignh')
calc.set_own_params_runs('init_structure', input_structure)
calc.generate_topology_and_g96file()
calc.write_input()

# 3. Define the simulation box boundaries (gmx editconf)
# Here we set a cubic box with a 0.8 nm distance from the molecule to the boundary
calc.set_own_params_runs('extra_editconf_parameters', '-bt cubic -c -d 0.8')
calc.run_editconf()

# 4. Solvate the system (gmx solvate / genbox)
# Uses a standard pre-equilibrated 216-water molecule box template
calc.set_own_params_runs('extra_genbox_parameters', '-cs spc216.gro')
calc.run_genbox()

# 5. Generate and execute the run file (gmx grompp & mdrun)
print("Compiling parameters and running energy minimization...")
calc.generate_gromacs_run_file()
calc.run()

print("Simulation finished successfully!")

