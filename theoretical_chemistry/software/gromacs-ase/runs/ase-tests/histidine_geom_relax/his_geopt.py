#!/usr/bin/env python3

"""
Compact ASE script for GROMACS geometry relaxation.
Based on the official ASE GROMACS calculator example.
"""

import sys
from ase.calculators.gromacs import Gromacs
from ase.io import read

# Read the initial structure from a PDB file (provided as a command-line argument)
infile_name = sys.argv[1]

# Initialize the GROMACS calculator
# The key parameters are set here for a minimization run [citation:2][citation:3]
calc = Gromacs(
    init_structure_file=infile_name,      # Input PDB file for pdb2gmx
    structure_file='gromacs_mm-relax.g96', # Output structure file
    force_field='oplsaa',                 # Force field to use [citation:1]
    water_model='tip3p',                  # Water model [citation:1]
    base_filename='gromacs_mm-relax',     # Base name for all files
    doing_qmmm=False,                     # Not doing a QM/MM calculation
    freeze_qm=True,                       # Freeze QM atoms if specified in index file
    index_filename='index.ndx',           # File for freeze groups
    extra_mdrun_parameters=' -nt 1 ',     # Run in serial (use one thread)
    define='-DFLEXIBLE',                  # Use flexible water model
    integrator='cg',                      # Conjugate gradient minimization [citation:3]
    nsteps='10000',                       # Maximum number of steps
    nstfout='10',                         # Print forces every 10 steps
    nstlog='10',
    nstenergy='10',
    nstlist='10',                         # Neighbor list update frequency
    ns_type='grid',                       # Grid search for neighbor list
    pbc='xyz',                            # Periodic boundary conditions
    rlist='1.15',                         # Cutoff for neighbor list (nm)
    coulombtype='PME-Switch',             # Electrostatics method
    rcoulomb='0.8',                       # Coulomb cutoff (nm)
    vdwtype='shift',                      # Van der Waals treatment
    rvdw='0.8',                           # VdW cutoff (nm)
    rvdw_switch='0.75',                   # Switch distance for VdW
    DispCorr='Ener'                       # Energy correction for dispersion
)

# Write the necessary input files and run the calculation
calc.generate_topology_and_g96file() # Creates .top and .gro from PDB
calc.generate_gromacs_run_file()     # Creates the .tpr run file
calc.run()                           # Runs mdrun to perform minimization

print("GROMACS minimization finished.")
