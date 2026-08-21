#!/usr/bin/env python3

"""
Custom ASE script for GROMACS that handles histidine properly.
"""

import sys
import os
from ase.calculators.gromacs import Gromacs

class CustomGromacs(Gromacs):
    """Custom Gromacs calculator that adds -his flag for pdb2gmx."""
    
    def _generate_topology_and_g96file(self):
        """Override to add -his flag."""
        # Copy the PDB file
        import shutil
        shutil.copy2(self.init_structure_file, 'gromacs.pdb')
        
        # Build the command with -his flag
        cmd = (f'gmx pdb2gmx -f gromacs.pdb -o gromacs.g96 -p gromacs.top '
               f'-ff {self.force_field} -water {self.water_model} -his')
        
        # Redirect output to log file
        cmd += ' > gromacs.pdb2gmx.log 2>&1'
        
        # Execute the command
        import subprocess
        subprocess.check_call(cmd, shell=True)

# Use the custom calculator
def main():
    pdb_file = sys.argv[1] if len(sys.argv) > 1 else 'his_corrected.pdb'
    
    if not os.path.exists(pdb_file):
        print(f"Error: PDB file '{pdb_file}' not found.")
        sys.exit(1)
    
    print(f"Using PDB file: {pdb_file}")
    
    # Initialize the custom calculator
    calc = CustomGromacs(
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
        nsteps='1000',
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
    
    try:
        print("\nGenerating topology and G96 file...")
        calc._generate_topology_and_g96file()
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

if __name__ == "__main__":
    main()
