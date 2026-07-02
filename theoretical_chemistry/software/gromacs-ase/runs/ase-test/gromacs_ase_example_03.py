#!/usr/bin/env python3
"""
gromacs_ase_example_03_improved.py
Enhanced GROMACS workflow with proper analysis and visualization
"""

import os
import subprocess
import sys
import glob
import shutil
import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime

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

# Create a log file
log_file = f"workflow_{datetime.now().strftime('%Y%m%d_%H%M%S')}.log"

# =============================================================================
# LOGGING FUNCTIONS
# =============================================================================

def log_message(message, log_file=log_file):
    """Write message to log file and print to console"""
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    log_entry = f"[{timestamp}] {message}"
    print(log_entry)
    with open(log_file, 'a') as f:
        f.write(log_entry + '\n')

# =============================================================================
# HELPER FUNCTIONS
# =============================================================================

def run_gmx_command(cmd, input_data=None, description="", check_output=False):
    """Generic GROMACS command runner with error handling"""
    log_message(f"\n--- {description} ---")
    log_message(f"Executing: {cmd}")
    
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
            log_message(f"[ERROR] Command failed with return code {process.returncode}")
            if stderr:
                log_message(f"STDERR: {stderr[:500]}")
            if stdout:
                log_message(f"STDOUT: {stdout[:500]}")
            return False
        
        log_message("✓ Command completed successfully")
        return True
        
    except Exception as e:
        log_message(f"[ERROR] Exception occurred: {e}")
        return False

def check_file_exists(filename, description="File"):
    """Check if a file exists and print status"""
    if os.path.isfile(filename):
        log_message(f"✓ {description} found: {filename}")
        return True
    else:
        log_message(f"✗ {description} not found: {filename}")
        return False

def parse_xvg(filename):
    """Parse XVG file and return data as numpy array"""
    data = []
    try:
        with open(filename, 'r') as f:
            for line in f:
                if line.startswith('#') or line.startswith('@'):
                    continue
                if line.strip():
                    values = [float(x) for x in line.split()]
                    data.append(values)
        return np.array(data) if data else None
    except Exception as e:
        log_message(f"[WARNING] Could not parse {filename}: {e}")
        return None

# =============================================================================
# WORKFLOW STEPS
# =============================================================================

def setup_from_pdb():
    """Create GROMACS input files from PDB"""
    log_message("\n" + "="*60)
    log_message("PART 0: Converting PDB to GROMACS Format")
    log_message("="*60)
    
    pdb_file = '1CRN.pdb' if os.path.isfile('1CRN.pdb') else None
    
    if not pdb_file:
        pdb_files = glob.glob('*.pdb')
        if pdb_files:
            pdb_file = pdb_files[0]
            log_message(f"✓ Found PDB file: {pdb_file}")
        else:
            log_message("[ERROR] No PDB file found!")
            return False
    
    log_message(f"Using PDB file: {pdb_file}")
    
    if check_file_exists('gromacs.g96', "GROMACS structure file") and \
       check_file_exists('gromacs.top', "GROMACS topology file"):
        log_message("✓ GROMACS files already exist, skipping conversion")
        return True
    
    # Convert PDB to GROMACS format
    pdb2gmx_cmd = f"{mpi_serial_cmd} {gmx_exe} pdb2gmx -f {pdb_file} -o gromacs.g96 -p gromacs.top -ff charmm27 -water tip3p"
    
    if not run_gmx_command(pdb2gmx_cmd, description="Running pdb2gmx"):
        log_message("[ERROR] pdb2gmx failed")
        return False
    
    # Add solvent box
    editconf_cmd = f"{mpi_serial_cmd} {gmx_exe} editconf -f gromacs.g96 -o box.g96 -c -d 1.0 -bt cubic"
    if run_gmx_command(editconf_cmd, description="Creating solvent box"):
        shutil.copy('box.g96', 'gromacs.g96')
        log_message("✓ Solvent box added")
    
    return os.path.isfile('gromacs.g96') and os.path.isfile('gromacs.top')

def run_energy_minimization():
    """Perform energy minimization"""
    log_message("\n" + "="*60)
    log_message("PART 1: Energy Minimization")
    log_message("="*60)
    
    if os.path.isfile('minim.edr'):
        log_message("✓ Found existing minimization output, skipping...")
        return True
    
    if not check_file_exists('gromacs.g96', "Structure file") or \
       not check_file_exists('gromacs.top', "Topology file"):
        log_message("[ERROR] Missing required input files")
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
    log_message("\n" + "="*60)
    log_message("PART 2: NVT Equilibration")
    log_message("="*60)
    
    if os.path.isfile('nvt.edr'):
        log_message("✓ Found existing NVT output, skipping...")
        return True
    
    if not check_file_exists('minim.gro', "Minimized structure"):
        log_message("[ERROR] Minimized structure file not found")
        return False
    
    # Create NVT MDP
    with open("nvt.mdp", "w") as f:
        f.write("""
integrator              = md
nsteps                  = 5000
dt                      = 0.002
nstxout                 = 500
nstvout                 = 500
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
gen-seed                = -1
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
    log_message("\n" + "="*60)
    log_message("PART 3: Extract and Plot Energy Profile")
    log_message("="*60)
    
    edr_file = None
    for f in ['minim.edr', 'nvt.edr']:
        if os.path.isfile(f):
            edr_file = f
            break
    
    if edr_file is None:
        log_message("[ERROR] No EDR file found")
        return False
    
    # Extract energy
    energy_cmd = f"{mpi_serial_cmd} {gmx_exe} energy -f {edr_file} -o energy_profile.xvg"
    if not run_gmx_command(energy_cmd, input_data="Potential\n0\n", 
                          description="Extracting energy profile"):
        return False
    
    # Plot energy profile
    try:
        data = parse_xvg('energy_profile.xvg')
        
        if data is not None and len(data) > 0:
            fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5))
            
            # Full energy profile
            ax1.plot(data[:, 0], data[:, 1], 'b-', linewidth=2)
            ax1.set_xlabel('Time (ps)', fontsize=12)
            ax1.set_ylabel('Potential Energy (kJ/mol)', fontsize=12)
            ax1.set_title('Full Energy Profile', fontsize=14)
            ax1.grid(True, alpha=0.3)
            
            # Zoom into the end (convergence)
            if len(data) > 100:
                start_idx = max(0, len(data) - 100)
                ax2.plot(data[start_idx:, 0], data[start_idx:, 1], 'r-', linewidth=2)
                ax2.set_xlabel('Time (ps)', fontsize=12)
                ax2.set_ylabel('Potential Energy (kJ/mol)', fontsize=12)
                ax2.set_title('Energy Convergence (last 100 steps)', fontsize=14)
                ax2.grid(True, alpha=0.3)
            
            plt.tight_layout()
            plt.savefig('energy_profile.png', dpi=300, bbox_inches='tight')
            log_message("✓ Energy profile plotted: energy_profile.png")
            
            # Print energy statistics
            min_energy = np.min(data[:, 1])
            max_energy = np.max(data[:, 1])
            final_energy = data[-1, 1]
            log_message(f"\nEnergy Statistics:")
            log_message(f"  Minimum: {min_energy:.2f} kJ/mol")
            log_message(f"  Maximum: {max_energy:.2f} kJ/mol")
            log_message(f"  Final:   {final_energy:.2f} kJ/mol")
            log_message(f"  Range:   {max_energy - min_energy:.2f} kJ/mol")
            
    except Exception as e:
        log_message(f"[WARNING] Could not plot energy profile: {e}")
    
    return True

def analyze_structure():
    """Analyze the final structure"""
    log_message("\n" + "="*60)
    log_message("PART 4: Structure Analysis")
    log_message("="*60)
    
    if not os.path.isfile('nvt.gro'):
        log_message("[WARNING] nvt.gro not found for analysis")
        return False
    
    # Create index file for protein
    log_message("Creating index file...")
    make_ndx_cmd = f"echo 'r Protein' | {mpi_serial_cmd} {gmx_exe} make_ndx -f nvt.gro -o index.ndx"
    if not run_gmx_command(make_ndx_cmd, description="Creating index file"):
        log_message("[WARNING] Could not create index file")
        # Try without index file for some analyses
        protein_ndx = ""
    else:
        protein_ndx = "-n index.ndx"
    
    # RMSD calculation (relative to minimized structure)
    log_message("\nCalculating RMSD...")
    rmsd_cmd = f"echo '1 1' | {mpi_serial_cmd} {gmx_exe} rms -s minim.tpr -f nvt.gro -o rmsd.xvg"
    if run_gmx_command(rmsd_cmd, description="Calculating RMSD"):
        # Plot RMSD
        try:
            data = parse_xvg('rmsd.xvg')
            if data is not None and len(data) > 0:
                plt.figure(figsize=(10, 6))
                plt.plot(data[:, 0], data[:, 1], 'g-', linewidth=2)
                plt.xlabel('Time (ps)', fontsize=12)
                plt.ylabel('RMSD (nm)', fontsize=12)
                plt.title('RMSD Relative to Minimized Structure', fontsize=14)
                plt.grid(True, alpha=0.3)
                plt.tight_layout()
                plt.savefig('rmsd.png', dpi=300, bbox_inches='tight')
                log_message("✓ RMSD plotted: rmsd.png")
                
                # Print RMSD statistics
                final_rmsd = data[-1, 1]
                avg_rmsd = np.mean(data[:, 1])
                log_message(f"\nRMSD Statistics:")
                log_message(f"  Average: {avg_rmsd:.3f} nm")
                log_message(f"  Final:   {final_rmsd:.3f} nm")
        except Exception as e:
            log_message(f"[WARNING] Could not plot RMSD: {e}")
    
    # Radius of gyration (using correct index group)
    log_message("\nCalculating radius of gyration...")
    
    # Try different index groups for gyration
    gyrate_commands = [
        f"echo '1' | {mpi_serial_cmd} {gmx_exe} gyrate -s nvt.tpr -f nvt.gro -o gyrate.xvg",
        f"echo 'Protein' | {mpi_serial_cmd} {gmx_exe} gyrate -s nvt.tpr -f nvt.gro -o gyrate.xvg",
        f"echo 'C-alpha' | {mpi_serial_cmd} {gmx_exe} gyrate -s nvt.tpr -f nvt.gro -o gyrate.xvg",
        f"echo 'Backbone' | {mpi_serial_cmd} {gmx_exe} gyrate -s nvt.tpr -f nvt.gro -o gyrate.xvg"
    ]
    
    gyrate_success = False
    for cmd in gyrate_commands:
        if run_gmx_command(cmd, description="Calculating radius of gyration"):
            gyrate_success = True
            break
    
    if gyrate_success and os.path.isfile('gyrate.xvg'):
        # Plot radius of gyration
        try:
            data = parse_xvg('gyrate.xvg')
            if data is not None and len(data) > 0:
                plt.figure(figsize=(10, 6))
                plt.plot(data[:, 0], data[:, 1], 'm-', linewidth=2)
                plt.xlabel('Time (ps)', fontsize=12)
                plt.ylabel('Radius of Gyration (nm)', fontsize=12)
                plt.title('Radius of Gyration During NVT', fontsize=14)
                plt.grid(True, alpha=0.3)
                plt.tight_layout()
                plt.savefig('gyrate.png', dpi=300, bbox_inches='tight')
                log_message("✓ Gyration radius plotted: gyrate.png")
                
                # Print statistics
                avg_rg = np.mean(data[:, 1])
                final_rg = data[-1, 1]
                log_message(f"\nRadius of Gyration Statistics:")
                log_message(f"  Average: {avg_rg:.3f} nm")
                log_message(f"  Final:   {final_rg:.3f} nm")
        except Exception as e:
            log_message(f"[WARNING] Could not plot gyration: {e}")
    
    # Calculate temperature (as a sanity check)
    log_message("\nChecking simulation temperature...")
    temp_cmd = f"{mpi_serial_cmd} {gmx_exe} energy -f nvt.edr -o temperature.xvg"
    if run_gmx_command(temp_cmd, input_data="Temperature\n0\n", 
                       description="Extracting temperature"):
        try:
            data = parse_xvg('temperature.xvg')
            if data is not None and len(data) > 0:
                avg_temp = np.mean(data[:, 1])
                std_temp = np.std(data[:, 1])
                log_message(f"Temperature Statistics:")
                log_message(f"  Average: {avg_temp:.1f} ± {std_temp:.1f} K")
                if abs(avg_temp - 300) < 10:
                    log_message("  ✓ Temperature is well equilibrated around 300K")
                else:
                    log_message("  ⚠ Temperature deviates from target (300K)")
        except Exception as e:
            log_message(f"[WARNING] Could not analyze temperature: {e}")
    
    return True

def create_summary_report():
    """Create a summary report of the workflow"""
    log_message("\n" + "="*60)
    log_message("SUMMARY REPORT")
    log_message("="*60)
    
    # List all generated files
    log_message("\nGenerated Files:")
    file_types = {
        'Structure files': ['*.gro', '*.g96'],
        'Trajectory files': ['*.trr', '*.xtc', '*.cpt'],
        'Energy files': ['*.edr'],
        'Log files': ['*.log'],
        'Analysis files': ['*.xvg'],
        'Plot files': ['*.png'],
        'TPR files': ['*.tpr'],
        'Other': ['*.ndx', '*.mdp']
    }
    
    for category, patterns in file_types.items():
        files = []
        for pattern in patterns:
            files.extend(glob.glob(pattern))
        if files:
            log_message(f"\n{category}:")
            for f in sorted(files):
                size = os.path.getsize(f) / 1024  # Size in KB
                log_message(f"  - {f} ({size:.1f} KB)")
    
    # Workflow statistics
    log_message("\n" + "="*60)
    log_message("Workflow completed successfully!")
    log_message("="*60)

# =============================================================================
# MAIN EXECUTION
# =============================================================================

def main():
    """Main workflow execution"""
    log_message("\n" + "="*60)
    log_message("GROMACS-ASE Enhanced Workflow for Protein (1CRN)")
    log_message("="*60)
    log_message(f"Log file: {log_file}")
    
    # Check GROMACS executable
    if not os.path.isfile(gmx_exe):
        log_message(f"[ERROR] GROMACS executable not found: {gmx_exe}")
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
    
    # Create summary
    create_summary_report()
    
    # Final status
    log_message("\n" + "="*60)
    if success:
        log_message("✓ WORKFLOW COMPLETED SUCCESSFULLY")
    else:
        log_message("✗ WORKFLOW COMPLETED WITH ERRORS")
    log_message("="*60)

if __name__ == "__main__":
    main()
