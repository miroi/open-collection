#!/usr/bin/env python3

"""
Simple GROMACS minimization script with proper box size.
Fixed energy extraction.
"""

import os
import sys
import subprocess

def run_minimization(pdb_file):
    """Run GROMACS energy minimization."""
    
    print("=" * 60)
    print(f"Running GROMACS minimization on: {pdb_file}")
    print("=" * 60)
    
    # Step 1: Generate topology
    print("\n[1/5] Generating topology with pdb2gmx...")
    cmd = f"echo '1' | gmx pdb2gmx -f {pdb_file} -o conf.gro -p topol.top -ff oplsaa -water tip3p -his"
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    
    if result.returncode != 0:
        print("❌ pdb2gmx failed!")
        print(result.stderr)
        return False
    print("✅ Topology generated")
    
    # Step 2: Create a box (large enough for vacuum simulation)
    print("\n[2/5] Creating simulation box...")
    cmd = "gmx editconf -f conf.gro -o box.gro -c -d 2.0 -bt cubic"
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    if result.returncode != 0:
        print("❌ editconf failed!")
        print(result.stderr)
        return False
    print("✅ Box created (2 nm padding)")
    
    # Step 3: Create minimization MDP with no PBC
    print("\n[3/5] Creating minimization parameters...")
    with open('minim.mdp', 'w') as f:
        f.write("""; Energy minimization parameters for vacuum
integrator          = steep
nsteps              = 50000
emtol               = 1000.0
nstxout             = 0
nstlog              = 0
nstenergy           = 100
nstlist             = 10
ns_type             = grid
pbc                 = xyz          ; Still use PBC but with large box
rlist               = 1.0
coulombtype         = cut-off
rcoulomb            = 1.0
vdw-type            = cut-off
rvdw                = 1.0
; For vacuum, we use a large box so cutoffs don't matter
""")
    print("✅ Created minim.mdp")
    
    # Step 4: Run grompp with the boxed structure
    print("\n[4/5] Preparing run input with grompp...")
    cmd = "gmx grompp -f minim.mdp -c box.gro -p topol.top -o minim.tpr -maxwarn 100"
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    
    if result.returncode != 0:
        print("❌ grompp failed!")
        print(result.stderr)
        return False
    print("✅ Run input prepared")
    
    # Step 5: Run minimization
    print("\n[5/5] Running energy minimization...")
    cmd = "gmx mdrun -nt 1 -v -deffnm minim"
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    
    if result.returncode != 0:
        print("❌ mdrun failed!")
        print(result.stderr)
        return False
    print("✅ Minimization complete")
    
    # Convert to PDB for visualization
    print("\nConverting to PDB format...")
    subprocess.run("gmx editconf -f minim.gro -o minimized.pdb", shell=True)
    if os.path.exists('minimized.pdb'):
        print("✅ Created minimized.pdb")
    
    # Extract energy - FIXED
    print("\nExtracting energy data...")
    # Use a different approach - write input to a temporary file
    with open('energy_input.txt', 'w') as f:
        f.write('Potential\n')  # Select potential energy
        f.write('\n')           # Press Enter to finish
    
    with open('energy_input.txt', 'r') as f:
        cmd = "gmx energy -f minim.edr -o potential.xvg"
        result = subprocess.run(cmd, shell=True, stdin=f, capture_output=True, text=True)
    
    if result.returncode == 0 and os.path.exists('potential.xvg'):
        print("✅ Energy data extracted (potential.xvg)")
        # Try to read the final energy from the log
        try:
            with open('minim.log', 'r') as f:
                for line in f:
                    if 'Potential Energy' in line:
                        print(f"   {line.strip()}")
                        break
        except:
            pass
    else:
        print("⚠️ Could not extract energy data")
    
    return True

def main():
    # Check for input file
    if len(sys.argv) > 1:
        pdb_file = sys.argv[1]
    else:
        pdb_files = [f for f in os.listdir('.') if f.endswith('.pdb')]
        if pdb_files:
            pdb_file = pdb_files[0]
            print(f"Using found PDB file: {pdb_file}")
        else:
            print("Error: No PDB file provided.")
            print("Usage: python gromacs_minim.py <input.pdb>")
            sys.exit(1)
    
    if not os.path.exists(pdb_file):
        print(f"Error: File '{pdb_file}' not found.")
        sys.exit(1)
    
    # Clean up previous files (optional)
    # Uncomment if you want to clean
    # for f in ['conf.gro', 'box.gro', 'topol.top', 'minim.*', 'gromacs.*']:
    #     if os.path.exists(f):
    #         os.remove(f)
    
    # Run the minimization
    success = run_minimization(pdb_file)
    
    if success:
        print("\n" + "=" * 60)
        print("🎉 Minimization completed successfully!")
        print("\nOutput files:")
        print("  📄 minim.gro        - Minimized structure (GROMACS format)")
        print("  📄 minimized.pdb    - Minimized structure (PDB format)")
        print("  📄 minim.edr        - Energy data")
        print("  📄 minim.log        - Log file")
        print("  📄 potential.xvg    - Energy vs step (if extracted)")
        print("  📄 conf.gro         - Initial structure")
        print("  📄 box.gro          - Structure in box")
        print("  📄 topol.top        - Topology file")
        
        print("\nTo visualize the result:")
        print("  vmd minimized.pdb")
        print("  pymol minimized.pdb")
        
        print("\nTo check the final energy:")
        print("  grep 'Potential Energy' minim.log")
        print("  gmx energy -f minim.edr")
    else:
        print("\n❌ Minimization failed.")
        sys.exit(1)

if __name__ == "__main__":
    main()
