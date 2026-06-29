import os
import subprocess
from ase.calculators.gromacs import Gromacs

# 1. Define custom environment execution paths
gmx_bin_dir = "/home/miroi/work/software/gromacs/gromacs_cloned/build_gnu/bin"
os.environ['GMXCMD_PREF'] = "mpirun -np 2"
os.environ['ASE_GROMACS_COMMAND'] = os.path.join(gmx_bin_dir, "gmx_mpi")

# =============================================================================
# PART 1: EXTRACT THE ENERGY CURVE PROFILE FROM THE COMPLETED EM RUN
# =============================================================================
print("\n--- Part 1: Extracting Energy Curves via gmx energy ---")

# Define the properties to extract (Potential=13, Kinetic=14, Total=15 depending on system)
# Echoing '13 0' asks gmx energy to parse Potential Energy and terminate selection
energy_selection = "13 0" 
xvg_output = "energy_profile.xvg"

# Construct the terminal pipeline for extracting data
gmx_energy_cmd = f"{os.environ['ASE_GROMACS_COMMAND']} energy -f gromacs.edr -o {xvg_output}"

try:
    process = subprocess.Popen(
        f"{os.environ['GMXCMD_PREF']} {gmx_energy_cmd}",
        shell=True,
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True
    )
    stdout, stderr = process.communicate(input=energy_selection)
    print(f"Energy extraction profile written to: {xvg_output}")
except Exception as e:
    print(f"Error extracting energy profile: {e}")

# Optional: Print raw values directly to the python terminal from the output file
if os.path.exists(xvg_output):
    print("\nSample Data Points (Time vs Potential Energy):")
    with open(xvg_output, 'r') as f:
        # Skip header lines starting with @ or #
        data_lines = [line.strip() for line in f if not line.startswith(('@', '#'))]
        for line in data_lines[:5]:  # Display first 5 structural relaxation steps
            print(line)

# =============================================================================
# PART 2: START SHORT MD EQUILIBRATION RUN (NVT/NPT MIX)
# =============================================================================
print("\n--- Part 2: Starting Short Equilibration MD Run ---")

# Step 2a: Define standard Molecular Dynamics parameters inside gromacs.mdp
# This changes the engine from a 'steepest descent' minimizer to an md integrator
mdp_content = """
integrator              = md        ; Leap-frog Molecular Dynamics integrator
nsteps                  = 5000      ; 2 fs * 5000 = 10 ps short run simulation
dt                      = 0.002     ; 2 femtosecond step interval time
nstxout                 = 500       ; save coordinates every 1.0 ps
nstenergy               = 100       ; energy frame savings frequency
cutoff-scheme           = Verlet    ; Buffered neighbor searching 
coulombtype             = PME       ; Particle Mesh Ewald long-range solver
vdwtype                 = Cut-off   ; Van der Waals tracking
tcoupl                  = v-rescale ; Velocity rescaling thermostat (NVT)
tc-grps                 = System    ; Monitor system temperatures globally
tau_t                   = 0.1       ; Coupling time constant
ref_t                   = 300       ; Target baseline environment temperature (300K)
pcoupl                  = no        ; Set to 'c-rescale' or 'Berendsen' for NPT
"""

with open("gromacs.mdp", "w") as mdp_file:
    mdp_file.write(mdp_content)

# Step 2b: Re-initialize the active state calculator using existing outputs
# We seed the simulation coordinates with the minimized 'gromacs.g96' output
calc_md = Gromacs(clean=True)
calc_md.set_own_params_runs('init_structure', 'gromacs.g96')

print("Compiling MD files via grompp and starting parallel execution...")
calc_md.generate_gromacs_run_file()
calc_md.run()

print("\nEquilibration Molecular Dynamics Simulation completed successfully!")

