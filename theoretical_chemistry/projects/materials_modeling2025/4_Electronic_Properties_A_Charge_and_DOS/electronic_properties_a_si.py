#!/usr/bin/env python
from ase import Atoms
from ase.calculators.espresso import Espresso, EspressoProfile
from ase.io import write
import os
import numpy as np
import subprocess
import shutil
import sys
sys.stdout.flush()  

# ==============================================
# ASE electronic properties 
# ==============================================
#
# ==============================================
# 1. Quantum Espresso Input Parameters
# ==============================================
pseudopotentials = {
    'Si': 'Si.upf'
}

base_input_data = {
    'control': {
        'prefix': 'Si_Electronic_A',
        'outdir': './tmp',
        'verbosity': 'low',
        'tstress': True,
        'tprnfor': True,
        'wf_collect': True,
        'disk_io': 'high'
    },
    'system': {
        'ecutwfc': 65,
        'occupations': 'smearing',
        'smearing': 'gauss',
        'degauss': 0.01,
        'ibrav': 0,
        'nat': 2,
        'ntyp': 1
    },
    'electrons': {
        'conv_thr': 1.0e-10
    }
}

# ==============================================
# 2. Atomic Structure
# ==============================================
atoms = Atoms(
    symbols=['Si']*2,
    positions=[ # positions in Angstrom
        [1.3669840665567621, 4.1009521996702860, 4.1009521996702860],
        [0.0000000000000000, 0.0000000000000000, 0.0000000000000000]
    ],
    cell=[ # positions in Angstrom
        [-0.0000000000000000, 2.7339681331135242, 2.7339681331135242],
        [2.7339681331135242, 0.0000000000000000, 2.7339681331135242],
        [2.7339681331135242, 2.7339681331135242, 0.0000000000000000]
    ],
    pbc=[True, True, True]
)

# ==============================================
# 3. Calculator Configuration
# ==============================================
# Set QE bin directory
#qe_bin = "/home/dsen/work/bin/qe-7.4.1_serial"
qe_bin = "/home/dsen/work/bin/qe-7.4.1"

# Main QE calculation 
#pw_command = f'{qe_bin}/bin/pw.x'
pw_command = f'mpirun -np 4 {qe_bin}/bin/pw.x'

# Serial post-processing commands for fast execution
pp_command = f"{qe_bin}/bin/pp.x < pp.in > pp.out 2>&1"
dos_command = f"{qe_bin}/bin/dos.x < dos.in > dos.out 2>&1"

# Memory intensive Parallel post-processing commands (run in one node only)
#projwfc_command = f'{qe_bin}/bin/projwfc.x < projwfc.in > projwfc.out 2>&1'
projwfc_command = f'mpirun -np 4 {qe_bin}/bin/projwfc.x < projwfc.in > projwfc.out 2>&1'

profile = EspressoProfile(
    command=pw_command,
    pseudo_dir='./'
)

# K-point grids 
scf_kpts = (15,15,15)
nscf_kpts = (30, 30, 30)

# DOS energy parameters
EMIN = -20.0  # Minimum energy (eV)
EMAX = 20.0   # Maximum energy (eV)
DELTA_E = 0.01  # Energy step (eV)

# QE tool 
def run_qe_tool(command, input_file, tool_name):
    """Run QE tool with input file and redirect output to file"""
    try:
        with open(input_file, 'r') as fin:
            subprocess.run(command, shell=True, stdin=fin, check=True)
        print(f"  {tool_name} completed successfully", flush=True)
        return True
    except subprocess.CalledProcessError as e:
        print(f"Error running {tool_name}: {e}", flush=True)
        return False

# ==============================================
# 4. SCF Calculation 
# ==============================================
scf_input_data = base_input_data.copy()
scf_input_data['control']['calculation'] = 'scf'

scf_calc = Espresso(
    profile=profile,
    pseudopotentials=pseudopotentials,
    input_data=scf_input_data,
    kpts=scf_kpts  
)
atoms.calc = scf_calc

print("\nRunning SCF calculation...", flush=True)
os.makedirs('tmp', exist_ok=True)
total_energy = atoms.get_potential_energy()
print(f"  Total energy: {total_energy:.6f} eV", flush=True)

# ==============================================
# 5. Extract charge density and Löwdin charges from SCF
# ==============================================
print("\n[Phase A.] Extracting charge density and Löwdin charges from SCF calculation...", flush=True)

# 5.1. Charge density calculation
print("\n1. Calculating charge density from SCF...", flush=True)
with open('pp.in', 'w') as f:
    f.write(f"""&INPUTPP
    prefix = '{base_input_data['control']['prefix']}',
    outdir = '{base_input_data['control']['outdir']}',
    filplot = 'charge_density',
    plot_num = 0
/
&PLOT
    iflag = 3,
    output_format = 6,
    fileout = 'charge_density.cube'
/
""")
run_qe_tool(pp_command, 'pp.in', 'pp.x')

# 5.2. Run projwfc.x on SCF results 
print("\n2. Running projwfc.x on SCF...", flush=True)
with open('projwfc.in', 'w') as f:
    f.write(f"""&PROJWFC
    prefix = '{base_input_data['control']['prefix']}',
    outdir = '{base_input_data['control']['outdir']}',
    ngauss = 0,
    degauss = {base_input_data['system']['degauss']},
    DeltaE = {DELTA_E},
    Emin = {EMIN},
    Emax = {EMAX},
    filpdos = 'scf_pdos',
    filproj = 'scf_projections'
/
""")
run_qe_tool(projwfc_command, 'projwfc.in', 'projwfc.x')

# 5.3. Löwdin population analysis 
print("\n3. Extracting Löwdin charges from SCF (projwfc.out)...", flush=True)
lowdin_file = 'lowdin.out'
spilling = None

try:
    with open('projwfc.out', 'r') as f:
        lines = f.readlines()
    
    # Find and save Löwdin charges section
    with open(lowdin_file, 'w') as out_f:
        out_f.write("Löwdin Charges from SCF calculation (projwfc.out):\n")
        out_f.write("================================================\n")
        
        in_section = False
        for line in lines:
            if "Lowdin Charges:" in line:
                in_section = True
            elif "Spilling Parameter:" in line:
                spilling = float(line.split()[-1])
                out_f.write(f"\nSpilling Parameter: {spilling:.6f}\n")
                break
            
            if in_section:
                out_f.write(line)
    
    print(f"  Löwdin charges saved to {lowdin_file}", flush=True)
    if spilling is not None:
        print(f"  Spilling parameter value: {spilling:.6f}", flush=True)
        if spilling < 0.05:
            print("  Excellent (<0.05)", flush=True)
        else:
            print("  Warning: Spilling parameter >0.05 - check projections!", flush=True)
except Exception as e:
    print(f"Error extracting Löwdin charges: {str(e)}", flush=True)

# ==============================================
# 6. Clean up SCF files and prepare for NSCF
# ==============================================
print("\nCleaning up SCF files and preparing for NSCF calculation...", flush=True)
os.makedirs('scf_files', exist_ok=True)

# Move ALL SCF-related files (including PDOS files)
for fname in os.listdir('.'):
    if (fname.startswith('Si_Electronic_A.') or 
       fname in ['espresso.pwi', 'espresso.pwo', 'pp.in', 'pp.out', 'projwfc.in', 'projwfc.out'] or
       fname.startswith('scf_pdos.') or  # From SCF projwfc
       fname.startswith('scf_projections')):  # From SCF projwfc
        shutil.move(fname, os.path.join('scf_files', fname))

print("  Moved all SCF-related files to scf_files directory", flush=True)

# ==============================================
# 7. NSCF Calculation
# ==============================================
nscf_input_data = base_input_data.copy()
nscf_input_data['control']['calculation'] = 'nscf'

nscf_input_data['control'].pop('tstress', None)
nscf_input_data['control'].pop('tprnfor', None)

nscf_calc = Espresso(
    profile=profile,
    pseudopotentials=pseudopotentials,
    input_data=nscf_input_data,
    kpts=nscf_kpts
)
atoms.calc = nscf_calc

# Direct NSCF execution, because it does not have energy
print(f"\nRunning NSCF calculation for DOS with k-grid {nscf_kpts}...", flush=True)
nscf_calc.calculate(atoms=atoms, 
                   properties=[], 
                   system_changes=['positions', 'cell', 'numbers', 'pbc'])
print("  NSCF completed, wavefunctions generated for DOS", flush=True)

# ==============================================
# 8. Calculate DOS and PDOS from NSCF
# ==============================================
print("\n[Phase B.] Calculating DOS and PDOS from NSCF calculation...", flush=True)

# 8.1. TDOS calculation
print("\n4. Calculating TDOS from NSCF...", flush=True)
with open('dos.in', 'w') as f:
    f.write(f"""&DOS
    prefix = '{base_input_data['control']['prefix']}',
    outdir = '{base_input_data['control']['outdir']}',
    DeltaE = {DELTA_E},
    Emin = {EMIN},
    Emax = {EMAX},
    ngauss = 0,
    degauss = {base_input_data['system']['degauss']},
    fildos = 'total_dos.dat'
/
""")
run_qe_tool(dos_command, 'dos.in', 'dos.x')

# 8.2. PDOS calculation
print("\n5. Calculating PDOS from NSCF...", flush=True)
with open('projwfc.in', 'w') as f:
    f.write(f"""&PROJWFC
    prefix = '{base_input_data['control']['prefix']}',
    outdir = '{base_input_data['control']['outdir']}',
    ngauss = 0,
    degauss = {base_input_data['system']['degauss']},
    DeltaE = {DELTA_E},
    Emin = {EMIN},
    Emax = {EMAX},
    filpdos = 'pdos',
    filproj = 'projections'
/
""")
run_qe_tool(projwfc_command, 'projwfc.in', 'projwfc.x')

# 8.3. Organize and process PDOS files
print("\n6. Organizing PDOS files from NSCF...", flush=True)
os.makedirs('pdos_results', exist_ok=True)
for fname in os.listdir('.'):
    if fname.startswith('pdos.') or fname.startswith('projections'):
        shutil.move(fname, os.path.join('pdos_results', fname))
print("  PDOS files moved to pdos_results directory", flush=True)

# 8.4 PDOS sanity check 
print("\n7. Verifying TDOS vs summed PDOS (ONLY below Fermi level)...", flush=True)
try:
    # Get Fermi level from NSCF
    fermi_level = nscf_calc.get_fermi_level()
    print(f"  Fermi level from NSCF calculation: {fermi_level:.4f} eV", flush=True)
    
    # Read data files
    tdos_data = np.loadtxt('total_dos.dat')
    sum_pdos_data = np.loadtxt('pdos_results/pdos.pdos_tot')
    energy_tdos = tdos_data[:, 0]
    tdos = tdos_data[:, 1]
    energy_pdos = sum_pdos_data[:, 0]
    sum_pdos = sum_pdos_data[:, 2]  
    
    # Confine to below Fermi level
    mask_tdos = energy_tdos <= fermi_level
    mask_pdos = energy_pdos <= fermi_level
    
    # Interpolate summed PDOS to TDOS grid 
    interp_pdos = np.interp(energy_tdos[mask_tdos], 
                           energy_pdos[mask_pdos], 
                           sum_pdos[mask_pdos])
    
    # Calculate integrated DOS below Fermi
    def integrate_dos(energy, dos):
        """Simple trapezoidal integration of DOS using the recommended function"""
        return np.trapezoid(dos, energy)
    
    int_tdos = integrate_dos(energy_tdos[mask_tdos], tdos[mask_tdos])
    int_pdos = integrate_dos(energy_tdos[mask_tdos], interp_pdos)
    
    print(f"    Integrated TDOS: {int_tdos:.4f} states", flush=True)
    print(f"    Integrated sum of PDOS: {int_pdos:.4f} states", flush=True)
    
    # Calculate relative difference
    rel_diff = abs(int_tdos - int_pdos) / max(int_tdos, int_pdos)
    print(f"  Relative difference in integrated DOS: {rel_diff*100:.2f}%", flush=True)
    
    # Pointwise comparison 
    significant = tdos[mask_tdos] > 0.1 * np.max(tdos[mask_tdos])
    pointwise_diff = np.abs(
        (interp_pdos[significant] - tdos[mask_tdos][significant]) / 
        np.maximum(tdos[mask_tdos][significant], 1e-6)
    )
    max_point_diff = np.max(pointwise_diff) if np.any(significant) else 0
    print(f"  Maximum pointwise difference: {max_point_diff*100:.2f}%", flush=True)
    
    if rel_diff > 0.05 or max_point_diff > 0.1:  # 5% integral or 10% pointwise threshold
        print("  Warning: Significant mismatch detected - check projections!", flush=True)
    else:
        print("  Excellent agreement (<5% integral difference)", flush=True)

except Exception as e:
    print(f"  Verification failed: {str(e)}", flush=True)


print("\n=== Electronic Structure Analysis Complete ===", flush=True)
print("Generated files:", flush=True)
print("- Charge density (from SCF): charge_density.cube", flush=True)
print("- Löwdin Charges (from SCF): lowdin.out", flush=True)
print("- Total DOS (from NSCF): total_dos.dat", flush=True)
print("- PDOS files (from NSCF): pdos_results/", flush=True)

