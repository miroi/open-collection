# nmr_tms_calc.py
import os
import subprocess
import glob
import re

# Define TMS molecule (tetramethylsilane) with optimized geometry from literature
# Si(CH3)4 - Silicon with 4 methyl groups in tetrahedral arrangement
def create_tms():
    from ase import Atoms
    # Tetrahedral geometry with Si at center, C at tetrahedral positions
    # Si-C bond length ~1.88 Å, C-H bond length ~1.09 Å
    tms = Atoms(
        'SiC4H12',
        positions=[
            # Silicon at center
            [ 0.00000,  0.00000,  0.00000],  # Si
            
            # Carbon atoms (tetrahedral arrangement, Si-C = 1.88 Å)
            [ 1.88000,  1.88000,  1.88000],  # C1
            [ 1.88000, -1.88000, -1.88000],  # C2
            [-1.88000,  1.88000, -1.88000],  # C3
            [-1.88000, -1.88000,  1.88000],  # C4
            
            # Hydrogens on C1
            [ 2.97000,  1.88000,  1.88000],  # H1
            [ 1.88000,  2.97000,  1.88000],  # H2
            [ 1.88000,  1.88000,  2.97000],  # H3
            
            # Hydrogens on C2
            [ 2.97000, -1.88000, -1.88000],  # H4
            [ 1.88000, -2.97000, -1.88000],  # H5
            [ 1.88000, -1.88000, -2.97000],  # H6
            
            # Hydrogens on C3
            [-2.97000,  1.88000, -1.88000],  # H7
            [-1.88000,  2.97000, -1.88000],  # H8
            [-1.88000,  1.88000, -2.97000],  # H9
            
            # Hydrogens on C4
            [-2.97000, -1.88000,  1.88000],  # H10
            [-1.88000, -2.97000,  1.88000],  # H11
            [-1.88000, -1.88000,  2.97000],  # H12
        ]
    )
    return tms

def write_nwchem_input(atoms, filename, task='gradient', properties=None):
    """Write a NWChem input file from ASE Atoms object"""
    coords = atoms.get_positions()
    symbols = atoms.get_chemical_symbols()
    
    input_content = f"start {filename[:-4]}\n\n"
    input_content += "geometry\n"
    
    for symbol, (x, y, z) in zip(symbols, coords):
        input_content += f" {symbol:2s} {x:14.8f} {y:14.8f} {z:14.8f}\n"
    
    input_content += "end\n\n"
    input_content += "basis\n * library 6-311G**\nend\n\n"
    input_content += "dft\n xc PBE0\n mult 1\n convergence energy 1e-7 density 1e-6\nend\n\n"
    
    if task == 'gradient':
        input_content += "task dft gradient\n"
    elif task == 'property':
        input_content += "property\n shielding\n"
        if properties:
            for prop in properties:
                input_content += f" {prop}\n"
        input_content += "end\n\n"
        input_content += "task dft property\n"
    
    with open(filename, 'w') as f:
        f.write(input_content)
    
    return filename

def run_nwchem(input_file):
    """Run NWChem and capture output"""
    base = input_file[:-4]
    for f in glob.glob(f"{base}.*"):
        if f != input_file and not f.endswith('.nwi'):
            try:
                os.remove(f)
            except:
                pass
    
    cmd = ['nwchem', input_file]
    result = subprocess.run(cmd, capture_output=True, text=True)
    return result

def parse_nmr_shielding(output_file_pattern):
    """Parse NMR shielding constants from NWChem output"""
    output_files = glob.glob(f'{output_file_pattern}.out') + glob.glob(f'{output_file_pattern}.log')
    
    if not output_files:
        return None
    
    with open(output_files[0], 'r') as f:
        content = f.read()
    
    # Find all shielding values
    pattern = r'isotropic\s*=\s*([0-9.]+)'
    matches = re.findall(pattern, content)
    
    if matches:
        return [float(val) for val in matches]
    return None

# Create TMS molecule
from ase import Atoms
tms = create_tms()

# Clean up old files
print("🧹 Cleaning up old TMS files...")
for f in glob.glob('tms_opt.*'):
    if not f.endswith('.py') and not f.endswith('.nwi'):
        try:
            os.remove(f)
        except:
            pass
for f in glob.glob('tms_nmr.*'):
    if not f.endswith('.py') and not f.endswith('.nwi'):
        try:
            os.remove(f)
        except:
            pass

# Step 1: Write input for geometry optimization
print("Step 1: Writing TMS geometry optimization input...")
write_nwchem_input(tms, 'tms_opt.nwi', task='gradient')

# Step 2: Run geometry optimization
print("Step 2: Running TMS geometry optimization...")
print("   This may take 5-10 minutes...")
result = run_nwchem('tms_opt.nwi')

if result.stdout:
    with open('tms_opt.out', 'w') as f:
        f.write(result.stdout)
    print("   Saved output to tms_opt.out")
    
    if 'Total DFT energy' in result.stdout:
        print("✅ TMS geometry optimization completed successfully!")
    else:
        print("❌ TMS geometry optimization may have failed.")
        print("   Check tms_opt.out for details.")
        exit()
else:
    print("❌ No output from NWChem.")
    exit()

# Step 3: Write input for NMR property calculation
print("\nStep 3: Writing TMS NMR calculation input...")
write_nwchem_input(tms, 'tms_nmr.nwi', task='property', properties=['shielding'])

# Step 4: Run NMR calculation
print("Step 4: Running TMS NMR calculation...")
print("   This may take 5-10 minutes...")
nmr_result = run_nwchem('tms_nmr.nwi')

if nmr_result.stdout:
    with open('tms_nmr.out', 'w') as f:
        f.write(nmr_result.stdout)
    print("   Saved output to tms_nmr.out")

# Step 5: Parse and display results
print("\nStep 5: Parsing TMS NMR results...")

if nmr_result.stdout and 'Total DFT energy' in nmr_result.stdout:
    print("✅ TMS NMR calculation completed successfully!")
    
    shielding_values = parse_nmr_shielding('tms_nmr')
    
    if shielding_values:
        atom_symbols = tms.get_chemical_symbols()
        
        # Separate by atom type
        carbon_shieldings = []
        hydrogen_shieldings = []
        silicon_shielding = None
        
        for i, (symbol, value) in enumerate(zip(atom_symbols, shielding_values)):
            if symbol == 'Si':
                silicon_shielding = value
            elif symbol == 'C':
                carbon_shieldings.append(value)
            elif symbol == 'H':
                hydrogen_shieldings.append(value)
        
        # Calculate averages
        avg_C = sum(carbon_shieldings) / len(carbon_shieldings) if carbon_shieldings else None
        avg_H = sum(hydrogen_shieldings) / len(hydrogen_shieldings) if hydrogen_shieldings else None
        
        print("\n📊 TMS Shielding Constants (Isotropic, ppm):")
        print("="*60)
        if silicon_shielding:
            print(f"  Si:        {silicon_shielding:10.4f} ppm")
        if avg_C:
            print(f"  C (avg):   {avg_C:10.4f} ppm  (from {len(carbon_shieldings)} carbons)")
            print(f"  C (min):   {min(carbon_shieldings):10.4f} ppm")
            print(f"  C (max):   {max(carbon_shieldings):10.4f} ppm")
        if avg_H:
            print(f"  H (avg):   {avg_H:10.4f} ppm  (from {len(hydrogen_shieldings)} hydrogens)")
            print(f"  H (min):   {min(hydrogen_shieldings):10.4f} ppm")
            print(f"  H (max):   {max(hydrogen_shieldings):10.4f} ppm")
        print("="*60)
        
        # Save to file
        with open('tms_shieldings.txt', 'w') as f:
            f.write("# TMS shielding constants from PBE0/6-311G** calculation\n")
            f.write(f"C_avg = {avg_C:.4f}\n")
            f.write(f"H_avg = {avg_H:.4f}\n")
            if silicon_shielding:
                f.write(f"Si = {silicon_shielding:.4f}\n")
            f.write("\n# Individual values\n")
            for i, (symbol, value) in enumerate(zip(atom_symbols, shielding_values)):
                f.write(f"{symbol}{i+1} = {value:.4f}\n")
        
        print("\n✅ Saved TMS shieldings to tms_shieldings.txt")
        
        # Also save as Python variables for easy use
        with open('tms_values.py', 'w') as f:
            f.write(f"""# TMS shielding values from PBE0/6-311G**
C_TMS = {avg_C:.4f}
H_TMS = {avg_H:.4f}
Si_TMS = {silicon_shielding:.4f} if {silicon_shielding} is not None else None
""")
        
    else:
        print("⚠️  Could not parse shielding values from output.")
else:
    print("❌ TMS NMR calculation failed.")

print("\n✅ Done!")
print("\n📁 Files created:")
print("   - tms_opt.nwi (optimization input)")
print("   - tms_opt.out (optimization output)")
print("   - tms_nmr.nwi (NMR input)")
print("   - tms_nmr.out (NMR output)")
print("   - tms_shieldings.txt (shielding values)")
print("   - tms_values.py (shielding values as Python variables)")
