# nmr_ethanol_fixed.py
import os
import subprocess
import glob
import re
from ase import Atoms
from ase.io import write

# Define the ethanol molecule
ethanol = Atoms(
    'C2H6O',
    positions=[
        [ 0.0000,  0.0000,  0.0000],  # C1
        [ 1.5000,  0.0000,  0.0000],  # C2
        [ 2.1000,  1.2000,  0.0000],  # O
        [-0.4000, -0.5000,  0.9000],  # H1
        [-0.4000, -0.5000, -0.9000],  # H2
        [-0.4000,  1.1000,  0.0000],  # H3
        [ 1.8000, -0.5000, -0.9000],  # H4
        [ 1.8000, -0.5000,  0.9000],  # H5
        [ 2.8000,  1.2000,  0.0000],  # H6
    ]
)

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

def parse_optimized_geometry():
    """Parse optimized geometry from NWChem output files"""
    output_files = glob.glob('ethanol_opt.out') + glob.glob('ethanol_opt.log')
    
    if not output_files:
        for f in os.listdir('.'):
            if f.startswith('ethanol_opt') and f.endswith('.zmat'):
                output_files = [f]
                break
    
    if not output_files:
        return None
    
    with open(output_files[0], 'r') as f:
        content = f.read()
    
    coords = []
    lines = content.split('\n')
    
    for i, line in enumerate(lines):
        if 'XYZ format geometry' in line:
            for j in range(i+3, len(lines)):
                if j >= len(lines) or '------' in lines[j] or lines[j].strip() == '':
                    break
                parts = lines[j].split()
                if len(parts) >= 4 and parts[0] in ['C', 'H', 'O']:
                    try:
                        x = float(parts[1])
                        y = float(parts[2])
                        z = float(parts[3])
                        coords.append([x, y, z])
                    except:
                        pass
    
    if coords:
        return coords
    
    for i, line in enumerate(lines):
        if 'Geometry "geometry"' in line:
            for j in range(i+5, len(lines)):
                if j >= len(lines) or '----' in lines[j] or lines[j].strip() == '':
                    break
                parts = lines[j].split()
                if len(parts) >= 5 and parts[1] in ['C', 'H', 'O']:
                    try:
                        x = float(parts[3])
                        y = float(parts[4])
                        z = float(parts[5])
                        coords.append([x, y, z])
                    except:
                        pass
    
    return coords if coords else None

def parse_nmr_shielding():
    """Parse NMR shielding constants from NWChem output"""
    output_files = glob.glob('ethanol_nmr.out') + glob.glob('ethanol_nmr.log')
    
    if not output_files:
        return None
    
    with open(output_files[0], 'r') as f:
        content = f.read()
    
    # Find all shielding values using regex
    # Look for "isotropic = XXX.XXXX" pattern
    pattern = r'isotropic\s*=\s*([0-9.]+)'
    matches = re.findall(pattern, content)
    
    if matches:
        shielding_values = [float(val) for val in matches]
        return shielding_values
    
    return None

# Clean up old files
print("Cleaning up old files...")
for f in glob.glob('ethanol_opt.*'):
    if not f.endswith('.py') and not f.endswith('.nwi'):
        try:
            os.remove(f)
        except:
            pass

# Step 1: Write input for geometry optimization
print("Step 1: Writing geometry optimization input...")
write_nwchem_input(ethanol, 'ethanol_opt.nwi', task='gradient')

# Step 2: Run geometry optimization
print("Step 2: Running geometry optimization...")
print("   This may take a few minutes...")
result = run_nwchem('ethanol_opt.nwi')

# Step 3: Check optimization results
print("Step 3: Checking optimization results...")

if result.stdout:
    with open('ethanol_opt.out', 'w') as f:
        f.write(result.stdout)
    print("   Saved output to ethanol_opt.out")
    
    if 'Total DFT energy' in result.stdout:
        print("✅ Geometry optimization completed successfully!")
        
        optimized_coords = parse_optimized_geometry()
        if optimized_coords:
            print(f"   Found {len(optimized_coords)} atoms in optimized geometry.")
            ethanol.set_positions(optimized_coords)
            write('ethanol_optimized.xyz', ethanol)
            print("   Optimized geometry saved to ethanol_optimized.xyz")
        else:
            print("   ⚠️  Could not parse optimized coordinates.")
            print("   Using initial coordinates for NMR calculation.")
    else:
        print("❌ Geometry optimization may have failed.")
        print("   Check ethanol_opt.out for details.")
        if result.stderr:
            print("   Error output:", result.stderr[:200])
else:
    print("❌ No output from NWChem.")
    print("   Check if 'nwchem' is working:")
    print("   nwchem --version")
    exit()

# Step 4: Write input for NMR property calculation
print("\nStep 4: Writing NMR calculation input...")
write_nwchem_input(ethanol, 'ethanol_nmr.nwi', task='property', properties=['shielding'])

# Clean up old NMR files
for f in glob.glob('ethanol_nmr.*'):
    if not f.endswith('.py') and not f.endswith('.nwi'):
        try:
            os.remove(f)
        except:
            pass

# Step 5: Run NMR calculation
print("Step 5: Running NMR calculation...")
print("   This may take a few minutes...")
nmr_result = run_nwchem('ethanol_nmr.nwi')

if nmr_result.stdout:
    with open('ethanol_nmr.out', 'w') as f:
        f.write(nmr_result.stdout)
    print("   Saved output to ethanol_nmr.out")

# Step 6: Parse and display results
print("\nStep 6: Parsing NMR results...")

if nmr_result.stdout:
    if 'ERROR' in nmr_result.stdout.upper():
        print("❌ NMR calculation had errors!")
        print("   Check ethanol_nmr.out for details.")
        lines = nmr_result.stdout.split('\n')
        print("\n   Last 20 lines of output:")
        for line in lines[-20:]:
            if line.strip():
                print(f"   {line.strip()}")
    elif 'Total DFT energy' in nmr_result.stdout:
        print("✅ NMR calculation completed successfully!")
        
        shielding_values = parse_nmr_shielding()
        
        if shielding_values:
            # Map atoms to their symbols
            atom_symbols = ethanol.get_chemical_symbols()
            
            print("\n📊 NMR Shielding Constants (Isotropic, ppm):")
            print("   (These are absolute shielding values, not chemical shifts)")
            print("   For chemical shifts, you need a reference (e.g., TMS)")
            print("")
            
            # Print each atom's shielding
            for i, (symbol, value) in enumerate(zip(atom_symbols, shielding_values)):
                print(f"  Atom {i:2d} ({symbol}): {value:10.4f} ppm")
            
            # Show carbon shielding values (C1 and C2)
            carbon_shieldings = []
            for i, (symbol, value) in enumerate(zip(atom_symbols, shielding_values)):
                if symbol == 'C':
                    carbon_shieldings.append((i, value))
            
            if carbon_shieldings:
                print("\n   Carbon shielding constants:")
                for i, value in carbon_shieldings:
                    print(f"      C{i+1}: {value:.4f} ppm")
            
            # Show oxygen shielding
            for i, (symbol, value) in enumerate(zip(atom_symbols, shielding_values)):
                if symbol == 'O':
                    print(f"\n   Oxygen shielding (O): {value:.4f} ppm")
            
            # Show hydrogen shielding values (excluding the OH proton)
            h_shieldings = []
            for i, (symbol, value) in enumerate(zip(atom_symbols, shielding_values)):
                if symbol == 'H':
                    h_shieldings.append((i, value))
            
            if h_shieldings:
                print(f"\n   Hydrogen shieldings ({len(h_shieldings)} protons):")
                for i, value in h_shieldings:
                    label = "OH" if i == 8 else "CH" 
                    print(f"      H{i+1} ({label}): {value:.4f} ppm")
            
            # Provide reference for chemical shifts
            print("\n   💡 To get chemical shifts (δ):")
            print("      δ = σ_ref - σ_sample")
            print("      For ¹³C and ¹H, use TMS as reference (σ_TMS needed)")
            print("      Common TMS shieldings: ¹³C ≈ 188 ppm, ¹H ≈ 31.8 ppm")
            
        else:
            print("⚠️  Could not parse shielding values from output.")
            print("   The output format may be different than expected.")
            
            print("\n   Searching for NMR-related output:")
            for line in nmr_result.stdout.split('\n'):
                if any(keyword in line.lower() for keyword in ['shielding', 'ppm', 'isotropic', 'tensor']):
                    print(f"   {line.strip()}")
    else:
        print("❌ NMR calculation may have failed.")
        print("   Check ethanol_nmr.out for details.")
else:
    print("❌ No output from NWChem.")

print("\n✅ Done!")
print("\n📁 Files created:")
print("   - ethanol_opt.nwi (optimization input)")
print("   - ethanol_opt.out (optimization output)")
print("   - ethanol_nmr.nwi (NMR input)")
print("   - ethanol_nmr.out (NMR output)")
if os.path.exists('ethanol_optimized.xyz'):
    print("   - ethanol_optimized.xyz (optimized geometry)")

# Optional: Show how to run a reference calculation
print("\n" + "="*60)
print("📝 To calculate chemical shifts, run a separate calculation for TMS:")
print("   python nmr_tms.py")
print("   Then: δ = σ_TMS - σ_ethanol")
print("="*60)
