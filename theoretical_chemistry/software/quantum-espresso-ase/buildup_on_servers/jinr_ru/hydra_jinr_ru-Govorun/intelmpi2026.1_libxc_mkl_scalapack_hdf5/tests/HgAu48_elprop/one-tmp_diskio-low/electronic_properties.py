#!/usr/bin/env python
from ase import Atoms
from ase.calculators.espresso import Espresso, EspressoProfile
from dftd4.ase import DFTD4
from ase.io import read, write
from ase.calculators.mixing import SumCalculator
from dftd4.interface import DampingParam
from dftd4.parameters import get_damping_param
import os
import numpy as np
import subprocess
import shutil
import sys
sys.stdout.flush()


# ==============================================
# 1. Quantum Espresso input parameters
# ==============================================
pseudopotentials = {
    'Au': 'Au_fr_pbesol.upf',
    'Hg': 'Hg_fr_pbesol.upf',
}

base_input_data = {
    'control': {
        'prefix': 'El_Hg',
        'outdir': './tmp',
        'verbosity': 'low',
        'tstress': True,
        'tprnfor': True,
        'disk_io': 'low'
    },
    'system': {
        'input_dft': 'XC-000I-000I-116L-133L-000I-000I',
        'ecutwfc': 120,
        'occupations': 'smearing',
        'smearing': 'gauss',
        'degauss': 0.01,
#       'assume_isolated': '2D',
        'nosym': True,
        'noinv': True,
        'ibrav': 0,
        'nat': 49,
        'ntyp': 2,
        'noncolin': True,
        'lspinorb': True
    },
    'electrons': {
        'mixing_beta': 0.2,
        'electron_maxstep': 100,
        'diagonalization': 'david',
        'diago_full_acc': True,
        'startingpot': 'atomic',
        'startingwfc': 'atomic+random',
        'conv_thr': 1.0e-9
#       'diago_thr_init': 1.0e-6,
    }
}

# ==============================================
# 2. Import atomic structure
# ==============================================
vasp_file = 'final_relaxed_structure_15062026.vasp'  

try:
    atoms = read(vasp_file, format='vasp')
    print(f"Successfully read {len(atoms)} atoms from {vasp_file}")
except FileNotFoundError:
    print(f"Error: {vasp_file} not found!")
    sys.exit(1)
except Exception as e:
    print(f"Error reading {vasp_file}: {e}")
    sys.exit(1)

# ==============================================
# 3. Calculator configuration
# ==============================================
# Main QE calculation with full parallelization
pw_command = f'srun -v   --mpi=pmi2    {os.environ["QE"]}/bin/pw.x '

# Serial post-processing commands for fast execution
pp_command = f'{os.environ["QE"]}/bin/pp.x < pp.in > pp.out 2>&1'
dos_command = f'{os.environ["QE"]}/bin/dos.x < dos.in > dos.out 2>&1'

# Parallel post-processing commands (one node only)
projwfc_command = f'srun -v --mpi=pmi2 -N 1 -n 32 {os.environ["QE"]}/bin/projwfc.x < projwfc.in > projwfc.out 2>&1'

profile = EspressoProfile(
    command=pw_command,
    pseudo_dir='./'
)

# DFT-D4 parameters
custom_params = {
    's6': 1.0,  # Two-body dispersion scaling
    's9': 1.0,  # Higher-order dispersion scaling 
    'alp': 16.0,  # Damping attenuation steepness   
    's8': 0.95948085,  # Three-body dispersion scaling
    'a1': 0.38574991,  # Damping function parameter 1
    'a2': 4.80688534,  # Damping function parameter 2
}

# K-point grids
scf_kpts = (3, 3, 1)
nscf_kpts = (5, 5, 1)
k_offset = (1, 1, 0)

# DOS energy parameters
EMIN = -20.0  # Minimum energy (eV)
EMAX = 20.0   # Maximum energy (eV)
DELTA_E = 0.01  # Energy step (eV)

# Define QE tool
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
print("\nPBE default DFT-D4 parameters :", get_damping_param("pbe"), flush=True)
print("Custom DFT-D4 parameters      :", custom_params, flush=True)

scf_input_data = base_input_data.copy()
scf_input_data['control']['calculation'] = 'scf'
scf_calc = Espresso(
    profile=profile,
    pseudopotentials=pseudopotentials,
    input_data=scf_input_data,
    kpts=scf_kpts,
    koffset=k_offset
)
dftd4_calc = DFTD4(verbose=True, params_tweaks=custom_params)
combined_calc = SumCalculator([scf_calc, dftd4_calc])

print("\n[Phase A.] Running SCF calculation...", flush=True)
os.makedirs('tmp', exist_ok=True)

atoms.calc = combined_calc
total_energy = atoms.get_potential_energy()

#4.1 Get energies
qe_energy = scf_calc.get_potential_energy(atoms)
d4_energy = dftd4_calc.get_potential_energy(atoms)
total_energy = combined_calc.get_potential_energy(atoms)

print("\n1. SCF Energy Results", flush=True)
print(f"  QE Electronic Energy:    {qe_energy:>12.6f} eV", flush=True)
print(f"  DFT-D4 Dispersion:       {d4_energy:>12.6f} eV", flush=True)
print(f"  Total Energy (QE + D4):  {total_energy:>12.6f} eV", flush=True)

energy_diff = abs(total_energy - (qe_energy + d4_energy))
if energy_diff <= 0.001:
    print(f"    Energy check: consistent", flush=True)
else:
    print(f"    Energy check: inconsistent (Δ={energy_diff:.6f} eV)", flush=True)

#4.2 Get forces and stress
forces = atoms.get_forces()
stress = atoms.get_stress()

force_norms = np.linalg.norm(forces, axis=1)
max_force = np.max(force_norms)
pressure = -np.sum(stress[:3]) * 1602.1766208 / 3  # kbar

print("\n2. SCF forces and stress", flush=True)
print(f"  Max force (norm): {max_force:>8.6f} eV/Å", flush=True)
print(f"  Pressure: {pressure:>8.6f} kbar", flush=True)

# ==============================================
# 5. Extract charge density and Löwdin charges from SCF
# ==============================================
print("\n[Phase B.] Extracting charge density and Löwdin charges from SCF calculation.", flush=True)

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
# 6. Cleaning up SCF files and running NSCF calculation
# ==============================================
# 6.1. Cleaning up SCF files
print("\n[Phase C.]  Cleaning up SCF files and running NSCF calculation...", flush=True)
os.makedirs('scf_files', exist_ok=True)

qe_prefix = base_input_data['control']['prefix']

# Move ALL SCF-related files (including PDOS files)
for fname in os.listdir('.'):
    if (fname.startswith(f'{qe_prefix}.') or 
       fname in ['espresso.pwi', 'espresso.pwo', 'pp.in', 'pp.out', 'projwfc.in', 'projwfc.out'] or
       fname.startswith('scf_pdos.') or  # From SCF projwfc
       fname.startswith('scf_projections')):  # From SCF projwfc
        shutil.move(fname, os.path.join('scf_files', fname))

print("\n1. Moved all SCF-related files to scf_files directory", flush=True)

## Restart NSCF from scratch ##

# 6.2 Running NSCF calculation (No forces, stress, DFT-D4)
nscf_input_data = base_input_data.copy()
nscf_input_data['control']['calculation'] = 'nscf'
nscf_input_data['control'].pop('tstress', None)
nscf_input_data['control'].pop('tprnfor', None)

## define NSCF run parameters
nscf_calc = Espresso(
    profile=profile,
    pseudopotentials=pseudopotentials,
    input_data=nscf_input_data,
    kpts=nscf_kpts,
    koffset=k_offset
)

atoms.calc = nscf_calc

# Directly running since NSCF does not have energies
print(f"\n2. Running NSCF calculation for DOS with k-grid {nscf_kpts}...", flush=True)
nscf_calc.calculate(atoms=atoms, 
                   properties=[], 
                   system_changes=['positions', 'cell', 'numbers', 'pbc'])
print("  NSCF completed, wavefunctions generated for DOS", flush=True)

# ==============================================
# 7. Calculate DOS and PDOS from NSCF
# ==============================================
print("\n[Phase D.] Calculating DOS and PDOS from NSCF calculation...", flush=True)

# 7.1. TDOS calculation
print("\n1. Calculating TDOS from NSCF...", flush=True)
with open('dos.in', 'w') as f:
    f.write(f"""&DOS
    prefix = '{nscf_input_data['control']['prefix']}',
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

# 7.2. PDOS calculation
print("\n2. Calculating PDOS from NSCF...", flush=True)
with open('projwfc.in', 'w') as f:
    f.write(f"""&PROJWFC
    prefix = '{nscf_input_data['control']['prefix']}',
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

# 7.3. Organize and process PDOS files
print("\n3. Organizing PDOS files from NSCF...", flush=True)
os.makedirs('pdos_results', exist_ok=True)
for fname in os.listdir('.'):
    if fname.startswith('pdos.') or fname.startswith('projections'):
        shutil.move(fname, os.path.join('pdos_results', fname))
print("  PDOS files moved to pdos_results directory", flush=True)

# 7.4 PDOS sanity check 
print("\n4. Verifying TDOS vs summed PDOS (ONLY below Fermi level)...", flush=True)
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
    
    # Calculate integrated DOS below Fermi level
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
