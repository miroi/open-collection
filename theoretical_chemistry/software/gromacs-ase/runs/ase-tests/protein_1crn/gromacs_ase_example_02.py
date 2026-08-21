#!/usr/bin/env python3
"""
gromacs_ase_example_02.py
Complete GROMACS workflow for protein (1CRN) from PDB file
"""

import os
import subprocess
import sys
import glob
import shutil

# =============================================================================
# CONFIGURATION
# =============================================================================

# Environment setup
gmx_bin_dir = "/home/miroi/work/software/gromacs/gromacs_cloned/build_gnu/bin"
gmx_exe = os.path.join(gmx_bin_dir, "gmx_mpi")

# Parallel configurations
MPI_NPROCS_MDRUN = 2
MPI_NPROCS_SERIAL = 1

mpi_parallel_cmd = f"mpirun -np {MPI_NPROCS_MDRUN}"
mpi_serial_cmd = f"mpirun -np {MPI_NPROCS_SERIAL}"

current_dir = os.getcwd()

# =============================================================================
# HELPER FUNCTIONS
# =============================================================================

def run_gmx_command(cmd, input_data=None, description="", check_output=False):
    """Generic GROMACS command runner with error handling"""
    print(f"\n--- {description} ---")
    print(f"Executing: {cmd}")
    
    try:
        process = subprocess.Popen(
            cmd,
            shell=True,
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        stdout, stderr = process.communicate(input=input_data)
        
        if process.returncode != 0:
            print(f"[ERROR] Command failed with return code {process.returncode}")
            if stderr:
                print("STDERR:", stderr[:500])
            if stdout:
                print("STDOUT:", stdout[:500])
            return False
        
        print("✓ Command completed successfully")
        return True
        
    except Exception as e:
        print(f"[ERROR] Exception occurred: {e}")
        return False

def check_file_exists(filename, description="File"):
    """Check if a file exists and print status"""
    if os.path.isfile(filename):
        print(f"✓ {description} found: {filename}")
        return True
    else:
        print(f"✗ {description} not found: {filename}")
        return False

# =============================================================================
# PART 0: SETUP GROMACS INPUT FILES FROM PDB
# =============================================================================

def setup_from_pdb():
    """Create GROMACS input files from PDB using pdb2gmx"""
    print("\n" + "="*60)
    print("PART 0: Converting PDB to GROMACS Format")
    print("="*60)
    
    # Check if PDB file exists
    pdb_file = None
    if os.path.isfile('1CRN.pdb'):
        pdb_file = '1CRN.pdb'
    else:
        # Look for any PDB file
        pdb_files = glob.glob('*.pdb')
        if pdb_files:
            pdb_file = pdb_files[0]
            print(f"✓ Found PDB file: {pdb_file}")
        else:
            print("[ERROR] No PDB file found!")
            return False
    
    print(f"Using PDB file: {pdb_file}")
    
    # Check if we already have GROMACS files
    if check_file_exists('gromacs.g96', "GROMACS structure file") and \
       check_file_exists('gromacs.top', "GROMACS topology file"):
        print("✓ GROMACS files already exist, skipping conversion")
        return True
    
    # Try to use pdb2gmx to convert PDB to GROMACS format
    print("\nAttempting to convert PDB to GROMACS format using pdb2gmx...")
    
    # Note: pdb2gmx requires force field selection. We'll use charmm27
    pdb2gmx_cmd = f"{mpi_serial_cmd} {gmx_exe} pdb2gmx -f {pdb_file} -o gromacs.g96 -p gromacs.top -ff charmm27 -water tip3p"
    
    # pdb2gmx may ask for force field selection interactively
    # We'll try with charmm27 and see if it works
    if not run_gmx_command(pdb2gmx_cmd, description="Running pdb2gmx"):
        print("[WARNING] pdb2gmx failed. Trying alternative approach...")
        
        # Alternative: Try to use different force field
        print("Trying with charmm36 force field...")
        pdb2gmx_cmd_alt = f"{mpi_serial_cmd} {gmx_exe} pdb2gmx -f {pdb_file} -o gromacs.g96 -p gromacs.top -ff charmm36 -water tip3p"
        
        if not run_gmx_command(pdb2gmx_cmd_alt, description="Running pdb2gmx with charmm36"):
            print("[ERROR] pdb2gmx failed with both force fields.")
            print("This could be due to:")
            print("1. Missing force field files in your GROMACS installation")
            print("2. Issues with the PDB file format")
            print("\nTrying manual conversion with editconf...")
            
            # If pdb2gmx fails, try just converting the coordinates with editconf
            editconf_cmd = f"{mpi_serial_cmd} {gmx_exe} editconf -f {pdb_file} -o gromacs.g96"
            if run_gmx_command(editconf_cmd, description="Converting PDB to G96 format"):
                print("✓ Structure file converted, but topology file may be missing")
                print("You may need to create a topology file manually.")
                return True
            return False
    
    # Check if files were created
    if os.path.isfile('gromacs.g96') and os.path.isfile('gromacs.top'):
        print("✓ Successfully converted PDB to GROMACS format")
        
        # Add solvent box if not present
        print("\nAdding solvent box...")
        editconf_cmd = f"{mpi_serial_cmd} {gmx_exe} editconf -f gromacs.g96 -o box.g96 -c -d 1.0 -bt cubic"
        if run_gmx_command(editconf_cmd, description="Creating solvent box"):
            # Replace structure with boxed version
            shutil.copy('box.g96', 'gromacs.g96')
            print("✓ Solvent box added")
        
        return True
    else:
        print("[ERROR] Could not create GROMACS files from PDB")
        return False

# =============================================================================
# PART 1: ENERGY MINIMIZATION
# =============================================================================

def run_energy_minimization():
    """Perform energy minimization"""
    print("\n" + "="*60)
    print("PART 1: Energy Minimization")
    print("="*60)
    
    # Check if minimization output exists
    if os.path.isfile('minim.edr'):
        print("✓ Found existing minimization output (minim.edr), skipping...")
        return True
    
    # Check input files
    if not check_file_exists('gromacs.g96', "Structure file") or \
       not check_file_exists('gromacs.top', "Topology file"):
        print("[ERROR] Missing required input files")
        return False
    
    # Create minimization MDP
    mdp_minim_content = """
integrator              = steep       ; Steepest Descent Minimization
nsteps                  = 50000      ; Maximum number of steps
emtol                   = 10.0       ; Stop when max force < 10 kJ/mol/nm
emstep                  = 0.01       ; Initial step size (nm)
nstenergy               = 100        ; Energy frame savings frequency
pbc                     = xyz        ; Periodic boundary conditions
cutoff-scheme           = Verlet     ; Buffered neighbor searching
ns_type                 = grid       ; Search grid for neighbor lists
coulombtype             = PME        ; Particle Mesh Ewald
rcoulomb                = 1.0        ; Electrostatic cutoff (nm)
vdwtype                 = Cut-off    ; Van der Waals
rvdw                    = 1.0        ; Van der Waals cutoff (nm)
"""
    
    with open("minim.mdp", "w") as f:
        f.write(mdp_minim_content)
    print("✓ Minimization MDP file created: minim.mdp")
    
    # Run grompp
    grompp_cmd = f"{mpi_serial_cmd} {gmx_exe} grompp -f minim.mdp -c gromacs.g96 -p gromacs.top -o minim.tpr -maxwarn 10"
    
    if not run_gmx_command(grompp_cmd, description="Running grompp for minimization"):
        return False
    
    # Run mdrun
    mdrun_cmd = f"{mpi_parallel_cmd} {gmx_exe} mdrun -v -deffnm minim"
    
    if not run_gmx_command(mdrun_cmd, description="Running energy minimization"):
        return False
    
    # Check output
    if os.path.isfile('minim.edr'):
        print("✓ Energy minimization completed successfully")
        return True
    else:
        print("[ERROR] Minimization did not produce expected output files")
        return False

# =============================================================================
# PART 2: NVT EQUILIBRATION
# =============================================================================

def run_nvt_equilibration():
    """Run NVT equilibration"""
    print("\n" + "="*60)
    print("PART 2: NVT Equilibration")
    print("="*60)
    
    # Check if NVT output exists
    if os.path.isfile('nvt.edr'):
        print("✓ Found existing NVT output, skipping...")
        return True
    
    # Check for minimized structure
    if not check_file_exists('minim.gro', "Minimized structure"):
        print("[ERROR] Minimized structure file not found. Run minimization first.")
        return False
    
    # Create NVT MDP
    nvt_mdp_content = """
integrator              = md        ; Leap-frog MD
nsteps                  = 5000      ; 10 ps
dt                      = 0.002     ; 2 fs step
nstxout                 = 500       ; Save coordinates every 1 ps
nstenergy               = 100       ; Energy frequency
pbc                     = xyz       ; Periodic boundaries
cutoff-scheme           = Verlet    ; Verlet scheme
ns_type                 = grid      ; Grid search
coulombtype             = PME       ; PME electrostatics
rcoulomb                = 1.0       ; Cutoff (nm)
vdwtype                 = Cut-off   ; Van der Waals
rvdw                    = 1.0       ; VdW cutoff (nm)
tcoupl                  = v-rescale ; Thermostat
tc-grps                 = System    ; Global coupling
tau_t                   = 0.1       ; Coupling time (ps)
ref_t                   = 300       ; Target temperature (K)
pcoupl                  = no        ; No barostat
gen-vel                 = yes       ; Generate velocities
gen-temp                = 300       ; Initial temperature (K)
"""
    
    with open("nvt.mdp", "w") as f:
        f.write(nvt_mdp_content)
    print("✓ NVT MDP file created: nvt.mdp")
    
    # Run grompp
    grompp_cmd = f"{mpi_serial_cmd} {gmx_exe} grompp -f nvt.mdp -c minim.gro -p gromacs.top -o nvt.tpr -maxwarn 10"
    
    if not run_gmx_command(grompp_cmd, description="Running grompp for NVT"):
        return False
    
    # Run mdrun
    mdrun_cmd = f"{mpi_parallel_cmd} {gmx_exe} mdrun -v -deffnm nvt"
    
    if not run_gmx_command(mdrun_cmd, description="Running NVT equilibration"):
        return False
    
    # Check output
    if os.path.isfile('nvt.edr'):
        print("✓ NVT equilibration completed successfully")
        return True
    else:
        print("[ERROR] NVT equilibration did not produce expected output files")
        return False

# =============================================================================
# PART 3: EXTRACT ENERGY PROFILE
# =============================================================================

def extract_energy_profile():
    """Extract energy profile from simulation"""
    print("\n" + "="*60)
    print("PART 3: Extracting Energy Profile")
    print("="*60)
    
    # Find EDR file
    edr_file = None
    for f in ['minim.edr', 'nvt.edr']:
        if os.path.isfile(f):
            edr_file = f
            break
    
    if edr_file is None:
        print("[ERROR] No EDR file found")
        return False
    
    print(f"Using EDR file: {edr_file}")
    
    # Extract potential energy
    energy_cmd = f"{mpi_serial_cmd} {gmx_exe} energy -f {edr_file} -o energy_profile.xvg"
    energy_selection = "Potential\n0\n"
    
    if run_gmx_command(energy_cmd, input_data=energy_selection, 
                      description="Extracting energy profile"):
        print("✓ Energy profile extracted to energy_profile.xvg")
        return True
    else:
        print("[ERROR] Energy extraction failed")
        return False

# =============================================================================
# MAIN EXECUTION
# =============================================================================

def main():
    """Main workflow execution"""
    print("\n" + "="*60)
    print("GROMACS-ASE Workflow for Protein (1CRN)")
    print("="*60)
    print(f"Working directory: {current_dir}")
    print(f"GROMACS executable: {gmx_exe}")
    
    # Check if GROMACS executable exists
    if not os.path.isfile(gmx_exe):
        print(f"[ERROR] GROMACS executable not found: {gmx_exe}")
        sys.exit(1)
    
    # Check for PDB file
    if not os.path.isfile('1CRN.pdb'):
        print("[WARNING] 1CRN.pdb not found!")
        pdb_files = glob.glob('*.pdb')
        if pdb_files:
            print(f"Found other PDB files: {pdb_files}")
        else:
            print("[ERROR] No PDB files found in current directory")
            sys.exit(1)
    
    # Execute workflow steps
    success = True
    
    # Step 0: Setup from PDB
    if not setup_from_pdb():
        print("[ERROR] Failed to setup GROMACS files from PDB")
        sys.exit(1)
    
    # Step 1: Energy minimization
    if not run_energy_minimization():
        success = False
        print("[ERROR] Energy minimization failed")
    
    # Step 2: NVT equilibration
    if success and not run_nvt_equilibration():
        success = False
        print("[ERROR] NVT equilibration failed")
    
    # Step 3: Extract energy profile
    if success and not extract_energy_profile():
        success = False
        print("[ERROR] Energy extraction failed")
    
    # Final summary
    print("\n" + "="*60)
    if success:
        print("✓ WORKFLOW COMPLETED SUCCESSFULLY")
    else:
        print("✗ WORKFLOW FAILED")
    
    print("\nGenerated files:")
    output_files = glob.glob('*.edr') + glob.glob('*.log') + glob.glob('*.gro') + \
                   glob.glob('*.xvg') + glob.glob('*.tpr') + glob.glob('*.g96')
    
    if output_files:
        for f in sorted(set(output_files)):
            print(f"  - {f}")
    else:
        print("  No output files found.")
    
    print("\n" + "="*60)

if __name__ == "__main__":
    main()
