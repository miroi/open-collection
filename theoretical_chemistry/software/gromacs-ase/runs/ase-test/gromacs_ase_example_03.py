#!/usr/bin/env python3
"""
gromacs_ase_example_02_enhanced.py
Enhanced GROMACS workflow with analysis and visualization
"""

import os
import subprocess
import sys
import glob
import shutil
import matplotlib.pyplot as plt
import numpy as np

# =============================================================================
# CONFIGURATION
# =============================================================================

gmx_bin_dir = "/home/miroi/work/software/gromacs/gromacs_cloned/build_gnu/bin"
gmx_exe = os.path.join(gmx_bin_dir, "gmx_mpi")
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
# WORKFLOW STEPS
# =============================================================================

def setup_from_pdb():
    """Create GROMACS input files from PDB"""
    print("\n" + "="*60)
    print("PART 0: Converting PDB to GROMACS Format")
    print("="*60)
    
    pdb_file = '1CRN.pdb' if os.path.isfile('1CRN.pdb') else None
    
    if not pdb_file:
        pdb_files = glob.glob('*.pdb')
        if pdb_files:
            pdb_file = pdb_files[0]
            print(f"✓ Found PDB file: {pdb_file}")
        else:
            print("[ERROR] No PDB file found!")
            return False
    
    print(f"Using PDB file: {pdb_file}")
    
    if check_file_exists('gromacs.g96', "GROMACS structure file") and \
       check_file_exists('gromacs.top', "GROMACS topology file"):
        print("✓ GROMACS files already exist, skipping conversion")
        return True
    
    # Convert PDB to GROMACS format
    pdb2gmx_cmd = f"{mpi_serial_cmd} {gmx_exe} pdb2gmx -f {pdb_file} -o gromacs.g96 -p gromacs.top -ff charmm27 -water tip3p"
    
    if not run_gmx_command(pdb2gmx_cmd, description="Running pdb2gmx"):
        print("[ERROR] pdb2gmx failed")
        return False
    
    # Add solvent box
    editconf_cmd = f"{mpi_serial_cmd} {gmx_exe} editconf -f gromacs.g96 -o box.g96 -c -d 1.0 -bt cubic"
    if run_gmx_command(editconf_cmd, description="Creating solvent box"):
        shutil.copy('box.g96', 'gromacs.g96')
        print("✓ Solvent box added")
    
    return os.path.isfile('gromacs.g96') and os.path.isfile('gromacs.top')

def run_energy_minimization():
    """Perform energy minimization"""
    print("\n" + "="*60)
    print("PART 1: Energy Minimization")
    print("="*60)
    
    if os.path.isfile('minim.edr'):
        print("✓ Found existing minimization output, skipping...")
        return True
    
    if not check_file_exists('gromacs.g96', "Structure file") or \
       not check_file_exists('gromacs.top', "Topology file"):
        print("[ERROR] Missing required input files")
        return False
    
    # Create minimization MDP
    with open("minim.mdp", "w") as f:
        f.write("""
integrator              = steep
nsteps                  = 50000
emtol                   = 10.0
emstep                  = 0.01
nstenergy               = 100
pbc                     = xyz
cutoff-scheme           = Verlet
ns_type                 = grid
coulombtype             = PME
rcoulomb                = 1.0
vdwtype                 = Cut-off
rvdw                    = 1.0
""")
    
    # Run grompp and mdrun
    grompp_cmd = f"{mpi_serial_cmd} {gmx_exe} grompp -f minim.mdp -c gromacs.g96 -p gromacs.top -o minim.tpr -maxwarn 10"
    if not run_gmx_command(grompp_cmd, description="Running grompp for minimization"):
        return False
    
    mdrun_cmd = f"{mpi_parallel_cmd} {gmx_exe} mdrun -v -deffnm minim"
    if not run_gmx_command(mdrun_cmd, description="Running energy minimization"):
        return False
    
    return os.path.isfile('minim.edr')

def run_nvt_equilibration():
    """Run NVT equilibration"""
    print("\n" + "="*60)
    print("PART 2: NVT Equilibration")
    print("="*60)
    
    if os.path.isfile('nvt.edr'):
        print("✓ Found existing NVT output, skipping...")
        return True
    
    if not check_file_exists('minim.gro', "Minimized structure"):
        print("[ERROR] Minimized structure file not found")
        return False
    
    # Create NVT MDP
    with open("nvt.mdp", "w") as f:
        f.write("""
integrator              = md
nsteps                  = 5000
dt                      = 0.002
nstxout                 = 500
nstenergy               = 100
pbc                     = xyz
cutoff-scheme           = Verlet
ns_type                 = grid
coulombtype             = PME
rcoulomb                = 1.0
vdwtype                 = Cut-off
rvdw                    = 1.0
tcoupl                  = v-rescale
tc-grps                 = System
tau_t                   = 0.1
ref_t                   = 300
pcoupl                  = no
gen-vel                 = yes
gen-temp                = 300
""")
    
    # Run grompp and mdrun
    grompp_cmd = f"{mpi_serial_cmd} {gmx_exe} grompp -f nvt.mdp -c minim.gro -p gromacs.top -o nvt.tpr -maxwarn 10"
    if not run_gmx_command(grompp_cmd, description="Running grompp for NVT"):
        return False
    
    mdrun_cmd = f"{mpi_parallel_cmd} {gmx_exe} mdrun -v -deffnm nvt"
    if not run_gmx_command(mdrun_cmd, description="Running NVT equilibration"):
        return False
    
    return os.path.isfile('nvt.edr')

def extract_and_plot_energy():
    """Extract and plot energy profile"""
    print("\n" + "="*60)
    print("PART 3: Extract and Plot Energy Profile")
    print("="*60)
    
    edr_file = None
    for f in ['minim.edr', 'nvt.edr']:
        if os.path.isfile(f):
            edr_file = f
            break
    
    if edr_file is None:
        print("[ERROR] No EDR file found")
        return False
    
    # Extract energy
    energy_cmd = f"{mpi_serial_cmd} {gmx_exe} energy -f {edr_file} -o energy_profile.xvg"
    if not run_gmx_command(energy_cmd, input_data="Potential\n0\n", 
                          description="Extracting energy profile"):
        return False
    
    # Plot energy profile
    try:
        data = []
        with open('energy_profile.xvg', 'r') as f:
            for line in f:
                if line.startswith('#') or line.startswith('@'):
                    continue
                if line.strip():
                    data.append([float(x) for x in line.split()])
        
        if data:
            data = np.array(data)
            plt.figure(figsize=(10, 6))
            plt.plot(data[:, 0], data[:, 1], 'b-', linewidth=2)
            plt.xlabel('Time (ps)', fontsize=12)
            plt.ylabel('Potential Energy (kJ/mol)', fontsize=12)
            plt.title('Energy Minimization Profile', fontsize=14)
            plt.grid(True, alpha=0.3)
            plt.tight_layout()
            plt.savefig('energy_profile.png', dpi=300, bbox_inches='tight')
            print("✓ Energy profile plotted: energy_profile.png")
    except Exception as e:
        print(f"[WARNING] Could not plot energy profile: {e}")
    
    return True

def analyze_structure():
    """Analyze the final structure"""
    print("\n" + "="*60)
    print("PART 4: Structure Analysis")
    print("="*60)
    
    if os.path.isfile('nvt.gro'):
        # RMSD calculation
        rmsd_cmd = f"echo '1 1' | {mpi_serial_cmd} {gmx_exe} rms -s minim.tpr -f nvt.gro -o rmsd.xvg"
        run_gmx_command(rmsd_cmd, description="Calculating RMSD")
        
        # Radius of gyration
        gyrate_cmd = f"{mpi_serial_cmd} {gmx_exe} gyrate -s nvt.tpr -f nvt.gro -o gyrate.xvg"
        run_gmx_command(gyrate_cmd, description="Calculating radius of gyration")
    
    return True

# =============================================================================
# MAIN EXECUTION
# =============================================================================

def main():
    """Main workflow execution"""
    print("\n" + "="*60)
    print("GROMACS-ASE Enhanced Workflow for Protein (1CRN)")
    print("="*60)
    
    # Check GROMACS executable
    if not os.path.isfile(gmx_exe):
        print(f"[ERROR] GROMACS executable not found: {gmx_exe}")
        sys.exit(1)
    
    # Run workflow
    success = True
    
    if not setup_from_pdb():
        success = False
    if success and not run_energy_minimization():
        success = False
    if success and not run_nvt_equilibration():
        success = False
    if success and not extract_and_plot_energy():
        success = False
    if success and not analyze_structure():
        success = False
    
    # Summary
    print("\n" + "="*60)
    if success:
        print("✓ WORKFLOW COMPLETED SUCCESSFULLY")
    else:
        print("✗ WORKFLOW FAILED")
    
    print("\nGenerated files:")
    for f in sorted(glob.glob('*.edr') + glob.glob('*.log') + glob.glob('*.gro') + 
                    glob.glob('*.xvg') + glob.glob('*.png') + glob.glob('*.tpr') + 
                    glob.glob('*.g96')):
        print(f"  - {f}")
    print("="*60)

if __name__ == "__main__":
    main()
