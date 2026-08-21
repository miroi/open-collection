#!/usr/bin/env python3

"""
Simplified ASE script for GROMACS geometry relaxation.
"""

import sys
import os
from ase.calculators.gromacs import Gromacs

# Use the corrected PDB file
pdb_file = sys.argv[1] if len(sys.argv) > 1 else 'his_corrected.pdb'

if not os.path.exists(pdb_file):
    print(f"Error: PDB file '{pdb_file}' not found.")
    sys.exit(1)

print(f"Using PDB file: {pdb_file}")

# Initialize the GROMACS calculator
calc = Gromacs(
    command='gmx',
    init_structure_file=pdb_file,
    structure_file='gromacs_mm-relax.g96',
    force_field='oplsaa',
    water_model='tip3p',
    base_filename='gromacs_mm-relax',
    doing_qmmm=False,
    index_filename='index.ndx',
    extra_mdrun_parameters=' -nt 1 ',
    define='-DFLEXIBLE',
    integrator='cg',
    nsteps='1000',  # Reduced for faster testing
    nstfout='10',
    nstlog='10',
    nstenergy='10',
    nstlist='10',
    ns_type='grid',
    pbc='xyz',
    rlist='1.15',
    coulombtype='PME-Switch',
    rcoulomb='0.8',
    vdwtype='shift',
    rvdw='0.8',
    rvdw_switch='0.75',
    DispCorr='Ener'
)

# Write the necessary input files and run the calculation
try:
    print("\nGenerating topology and G96 file...")
    calc.generate_topology_and_g96file()
    print("✅ Topology generation complete!")
    
    print("Generating GROMACS run file...")
    calc.generate_gromacs_run_file()
    print("✅ Run file generation complete!")
    
    print("Running GROMACS minimization...")
    calc.run()
    print("✅ GROMACS minimization finished successfully!")
    
except Exception as e:
    print(f"\n❌ Error during GROMACS run: {e}")
    sys.exit(1)
