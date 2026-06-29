import os
import subprocess

# 1. Define exact custom environment execution paths
gmx_bin_dir = "/home/miroi/work/software/gromacs/gromacs_cloned/build_gnu/bin"
gmx_exe = os.path.join(gmx_bin_dir, "gmx_mpi")

# Parallel configurations
mpi_parallel_pref = "mpirun -np 2"
# CRITICAL FIX: Use -np 1 to satisfy the MPI binary requirement without parallelizing grompp
mpi_serial_pref = "mpirun -np 1" 

current_working_dir = os.getcwd()
abs_edr = os.path.join(current_working_dir, 'gromacs.edr')

# =============================================================================
# PART 1: EXTRACT THE ENERGY CURVE PROFILE FROM THE COMPLETED EM RUN
# =============================================================================
print("\n--- Part 1: Extracting Energy Curves via gmx energy ---")

energy_selection = "13 0" 
xvg_output = "energy_profile.xvg"
gmx_energy_cmd = f"{mpi_parallel_pref} {gmx_exe} energy -f {abs_edr} -o {xvg_output}"

try:
    process = subprocess.Popen(
        gmx_energy_cmd,
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

# =============================================================================
# PART 2: START SHORT MD EQUILIBRATION RUN (NVT)
# =============================================================================
print("\n--- Part 2: Starting Short Equilibration MD Run ---")

mdp_content = """
integrator              = md        ; Leap-frog Molecular Dynamics integrator
nsteps                  = 5000      ; 2 fs * 5000 = 10 ps short run simulation
dt                      = 0.002     ; 2 femtosecond step interval time
nstxout                 = 500       ; save coordinates every 1.0 ps
nstenergy               = 100       ; energy frame savings frequency
pbc                     = xyz       ; Enable standard periodic boundary conditions
cutoff-scheme           = Verlet    ; Buffered neighbor searching 
ns_type                 = grid      ; Search grid for neighbor lists
coulombtype             = PME       ; Particle Mesh Ewald long-range solver
rcoulomb                = 1.0       ; Short-range electrostatic cutoff distance (nm)
vdwtype                 = Cut-off   ; Van der Waals tracking
rvdw                    = 1.0       ; Short-range Van der Waals cutoff distance (nm)
tcoupl                  = v-rescale ; Velocity rescaling thermostat (NVT)
tc-grps                 = System    ; Monitor system temperatures globally
tau_t                   = 0.1       ; Coupling time constant
ref_t                   = 300       ; Target baseline environment temperature (300K)
pcoupl                  = no        ; No barostat for initial NVT equilibration
"""

with open("gromacs.mdp", "w") as mdp_file:
    mdp_file.write(mdp_content)

print("Compiling MD parameters via mpirun -np 1 grompp...")
# Wrapping grompp inside a single-rank MPI call ensures the binary initializes without aborting
grompp_cmd = f"{mpi_serial_pref} {gmx_exe} grompp -f gromacs.mdp -c gromacs.g96 -p gromacs.top -o md_equilibration.tpr -maxwarn 10"

grompp_proc = subprocess.run(grompp_cmd, shell=True, capture_output=True, text=True)

if grompp_proc.returncode != 0:
    print("\n[ERROR] GROMACS grompp compilation failed!")
    print("="*50)
    print(grompp_proc.stderr)
    print(grompp_proc.stdout)
    print("="*50)
else:
    print("Successfully built 'md_equilibration.tpr' structural binary file.")
    print("Launching parallel execution loop via mdrun...")
    
    # Launch mdrun across the requested parallel processor layout
    mdrun_cmd = f"{mpi_parallel_pref} {gmx_exe} mdrun -deffnm md_equilibration"
    
    mdrun_proc = subprocess.run(mdrun_cmd, shell=True, capture_output=True, text=True)
    
    if mdrun_proc.returncode != 0:
        print("\n[ERROR] GROMACS mdrun failed to execute parallel integration loop!")
        print(mdrun_proc.stderr)
    else:
        print("\nEquilibration Molecular Dynamics Simulation completed successfully!")

