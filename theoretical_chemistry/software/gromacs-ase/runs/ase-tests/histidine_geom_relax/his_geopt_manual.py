#!/usr/bin/env python3

"""
Manual GROMACS workflow with custom MDP file.
"""

import os
import sys
import shutil
import subprocess
from ase.calculators.gromacs import Gromacs

class ManualGromacs(Gromacs):
    """Custom Gromacs calculator with manual MDP creation."""
    
    def generate_gromacs_run_file(self):
        """Override to create a proper MDP file."""
        # Create a proper minimization MDP file
        mdp_content = """; GROMACS minimization MDP
integrator          = steep
nsteps              = 50000
emtol               = 1000.0
nstxout             = 0
nstlog              = 0
nstenergy           = 100
nstlist             = 10
ns_type             = grid
pbc                 = xyz
rlist               = 1.0
coulombtype         = cut-off
rcoulomb            = 1.0
vdw-type            = cut-off
rvdw                = 1.0
"""
        with open('gromacs.mdp', 'w') as f:
            f.write(mdp_content)
        print("✅ Created gromacs.mdp")
        
        # Run grompp
        cmd = 'gmx grompp -f gromacs.mdp -c gromacs.g96 -p gromacs.top -o gromacs.tpr -maxwarn 100'
        cmd += ' > gromacs.grompp.log 2>&1'
        print(f"Running: {cmd}")
        result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
        if result.returncode != 0:
            print("❌ grompp failed. Check gromacs.grompp.log")
            with open('gromacs.grompp.log', 'r') as f:
                print(f.read())
            raise subprocess.CalledProcessError(result.returncode, cmd)
        print("✅ grompp completed successfully")

def main():
    pdb_file = sys.argv[1] if len(sys.argv) > 1 else 'his_corrected.pdb'
    
    if not os.path.exists(pdb_file):
        print(f"Error: PDB file '{pdb_file}' not found.")
        sys.exit(1)
    
    print(f"Using PDB file: {pdb_file}")
    
    # Initialize the custom calculator
    calc = ManualGromacs(
        command='gmx',
        init_structure_file=pdb_file,
        structure_file='gromacs_mm-relax.g96',
        force_field='oplsaa',
        water_model='tip3p',
        base_filename='gromacs_mm-relax',
        doing_qmmm=False,
        index_filename='index.ndx',
        extra_mdrun_parameters=' -nt 1 '
    )
    
    try:
        print("\n[1/3] Generating topology and G96 file...")
        calc._generate_topology_and_g96file()
        print("✅ Topology generation complete!")
        
        print("\n[2/3] Generating GROMACS run file...")
        calc.generate_gromacs_run_file()
        print("✅ Run file generation complete!")
        
        print("\n[3/3] Running GROMACS minimization...")
        calc.run()
        print("✅ GROMACS minimization finished successfully!")
        
        # Convert output to PDB for visualization
        if os.path.exists('gromacs_mm-relax.g96'):
            print("\nConverting output to PDB format...")
            subprocess.run("gmx editconf -f gromacs_mm-relax.g96 -o minimized.pdb", shell=True)
            print("✅ Created minimized.pdb")
        
    except Exception as e:
        print(f"\n❌ Error during GROMACS run: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
