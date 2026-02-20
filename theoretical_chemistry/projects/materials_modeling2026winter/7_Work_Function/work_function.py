#!/usr/bin/env python
from ase import Atoms
from ase.calculators.espresso import Espresso, EspressoProfile
import numpy as np
import os
import subprocess
import shutil
import sys
sys.stdout.flush()  

# ==============================================
# ASE electrostatic potential calculation
# ==============================================
#
# ==============================================
# 1. Quantum Espresso Input Parameters
# ==============================================
pseudopotentials = {
    'C': 'C.upf'
}

base_input_data = {
    'control': {
        'prefix': 'graphene',
        'outdir': './tmp',
        'verbosity': 'low',
        'tstress': True,
        'tprnfor': True,
        'disk_io': 'high'
    },
    'system': {
        'ecutwfc': 100,
        'occupations': 'smearing',
        'smearing': 'gauss',
        'degauss': 0.01,
        'ibrav': 0,
        'nat': 2,
        'ntyp': 1,
        'assume_isolated': '2D'
    },
    'electrons': {
        'conv_thr': 1.0e-10
    }
}

# ==============================================
# 2. Atomic Structure
# ==============================================
atoms = Atoms(
    symbols=['C']*2,
    positions=[ # positions in Angstrom
        [0.0000000000000000, 0.0000000000000000, 7.5000000000000000],
        [0.0000000000000000, 1.4239328281445778, 7.5000000000000000]
    ],
    cell=[ # positions in Angstrom
        [2.4663240049633459, 0.0000000000000000, 0.0000000000000000],
        [-1.2331620024816730, 2.1358992422670768, 0.0000000000000000],
        [0.0000000000000000, 0.0000000000000000, 15.0000000000000000]
    ],
    pbc=[True, True, True]
)

# ==============================================
# 3. Calculator Configuration
# ==============================================
# Set QE bin directory
qe_bin = "/home/dsen/work/bin/qe-7.4.1"

# Main QE calculation 
pw_command = f'mpirun -np 4 {qe_bin}/bin/pw.x'

# Post-processing commands
pp_command = f"{qe_bin}/bin/pp.x < pp.in > pp.out 2>&1"
average_command = f"{qe_bin}/bin/average.x < average.in > average.out 2>&1"

profile = EspressoProfile(
    command=pw_command,
    pseudo_dir='./'
)

# Set k-grids
scf_kpts = (27,27,1)

# Potential plot settings
nz_points = 200  
smoothing_length = 3.8149 # in Bohr

# QE tool execution format
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
fermi_ev = atoms.calc.get_fermi_level()
print(f"  Fermi level: {fermi_ev:.6f} eV", flush=True)

# ==============================================
# 5. Extract electrostatic potential with pp.x
# ==============================================
print("\nExtracting electrostatic potential with pp.x...", flush=True)

# 5.1. Electrostatic potential calculation
print("\n1. Calculating electrostatic potential from SCF...", flush=True)
with open('pp.in', 'w') as f:
    f.write(f"""&INPUTPP
    prefix = '{base_input_data['control']['prefix']}',
    outdir = '{base_input_data['control']['outdir']}',
    filplot = 'electrostatic_potential',
    plot_num = 11
/
&PLOT
    iflag = 3,
    output_format = 6
/
""")
run_qe_tool(pp_command, 'pp.in', 'pp.x')

# ==============================================
# 6. Planar averaging with average.x
# ==============================================
print("\n2. Calculating planar average of electrostatic potential...", flush=True)

with open('average.in', 'w') as f:
    f.write(f"""1
electrostatic_potential
1.0
{nz_points}
3
{smoothing_length}
""")
run_qe_tool(average_command, 'average.in', 'average.x')

# ==============================================
# 7. Clean up and organize files
# ==============================================
print("\nCleaning up and organizing files...", flush=True)
os.makedirs('potential_results', exist_ok=True)

# Move all calculation files to results directory
for fname in os.listdir('.'):
    if (fname in ['espresso.pwi', 'espresso.pwo', 'espresso.err', 'pp.in', 'pp.out', 'average.in', 'average.out',
                 'electrostatic_potential', 'avg.dat'] or
        fname.startswith('electrostatic_potential.')):
        shutil.move(fname, os.path.join('potential_results', fname))

print("  Moved all potential-related files to potential_results directory", flush=True)

# ==============================================
# 8. Plot the averaged potential 
# ==============================================
print("\n3. Plotting the averaged potential...", flush=True)

z_length = atoms.cell[2, 2]  # in Angstroms

try:
    data = np.loadtxt('potential_results/avg.dat')
    x_angstrom = data[:, 0] * 0.529177
    planar_avg_ev = data[:, 1] * 13.6058
    macroscopic_avg_ev = data[:, 2] * 13.6058
    
    with open('plot_potential.gp', 'w') as f:
        f.write(f"""set terminal pngcairo enhanced size 1200,900 font "Arial,14"
set output 'potential_plot.png'
set title 'Electrostatic Potential Averaging (z-direction)'
set xlabel 'Position along z-axis (Å)'
set ylabel 'Electrostatic Potential (eV)'
set grid linecolor rgb '#dddddd' linewidth 1
set key top right box linecolor rgb '#000000' linewidth 1

# Style settings
set style line 1 linecolor rgb '#ff0000' linewidth 2 pointsize 0.5
set style line 2 linecolor rgb '#0000ff' linewidth 3 pointsize 0.5
set style line 3 linecolor rgb '#00cc00' linewidth 2 dashtype 2

# Set ranges
set xr [0:{z_length}]
set autoscale y

# Fermi level line
set arrow from graph 0, first {fermi_ev} to graph 1, first {fermi_ev} nohead linestyle 3

plot 'potential_results/avg.dat' using ($1*0.529177):($2*13.6058) with lines linestyle 1 title 'Planar Average', \\
     'potential_results/avg.dat' using ($1*0.529177):($3*13.6058) with lines linestyle 2 title 'Macroscopic Average', \\
     {fermi_ev} with lines linestyle 3 title 'Fermi Level ({fermi_ev:.3f} eV)'

# Add some annotations
set label "Cell length: {z_length:.1f} Å" at graph 0.05,0.95
set label "Fermi level: {fermi_ev:.3f} eV" at graph 0.05,0.88
set label "Data from avg.dat" at graph 0.05,0.81

set output
""")
    
    # Run gnuplot
    try:
        subprocess.run('gnuplot plot_potential.gp', shell=True, check=True)
        print("  Plot saved as 'potential_plot.png'", flush=True)
    except (subprocess.CalledProcessError, FileNotFoundError):
        print("  Gnuplot not available, skipping plotting", flush=True)
        
except Exception as e:
    print(f"  Error in plotting: {e}", flush=True)

print("\n=== Electrostatic Potential Calculation Complete ===", flush=True)
print("Generated files:", flush=True)
print("- SCF calculation files: tmp/", flush=True)
print("- Electrostatic potential data: potential_results/electrostatic_potential", flush=True)
print("- Planar averaged potential: potential_results/avg.dat", flush=True)
print("- Final plot: potential_plot.png", flush=True)