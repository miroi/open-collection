# nmr_ethanol_with_shifts.py
import os
import glob
import re
from ase import Atoms
from ase.io import read, write

# Read the shielding values from the ethanol calculation
def get_ethanol_shieldings():
    """Get ethanol shielding values from the output"""
    output_files = glob.glob('ethanol_nmr.out') + glob.glob('ethanol_nmr.log')
    
    if not output_files:
        print("❌ No ethanol NMR output found!")
        print("   Run ethanol_nmr_01.py first")
        return None
    
    with open(output_files[0], 'r') as f:
        content = f.read()
    
    pattern = r'isotropic\s*=\s*([0-9.]+)'
    matches = re.findall(pattern, content)
    
    if matches:
        return [float(val) for val in matches]
    return None

# Read the TMS shielding values
def get_tms_shieldings():
    """Get TMS shielding values from the output"""
    output_files = glob.glob('tms_nmr.out') + glob.glob('tms_nmr.log')
    
    if not output_files:
        print("❌ No TMS NMR output found!")
        print("   Run nmr_tms.py first")
        return None
    
    with open(output_files[0], 'r') as f:
        content = f.read()
    
    pattern = r'isotropic\s*=\s*([0-9.]+)'
    matches = re.findall(pattern, content)
    
    if matches:
        return [float(val) for val in matches]
    return None

# Read the TMS shieldings from saved file
def get_tms_from_file():
    """Get TMS shielding values from saved file"""
    if not os.path.exists('tms_shieldings.txt'):
        return None
    
    with open('tms_shieldings.txt', 'r') as f:
        content = f.read()
    
    c_avg = None
    h_avg = None
    
    for line in content.split('\n'):
        if 'C_avg' in line:
            c_avg = float(line.split('=')[1].strip())
        elif 'H_avg' in line:
            h_avg = float(line.split('=')[1].strip())
    
    return {'C': c_avg, 'H': h_avg}

# Load the data
print("📊 Calculating Chemical Shifts for Ethanol")
print("="*60)

# Option 1: Use TMS file if available
tms_data = get_tms_from_file()
if tms_data and tms_data['C'] and tms_data['H']:
    print("✅ Using TMS shielding values from file")
    sigma_TMS_C = tms_data['C']
    sigma_TMS_H = tms_data['H']
else:
    # Option 2: Use common literature values
    print("⚠️  TMS file not found, using literature values")
    print("   (PBE0/6-311G** typically gives ~188 ppm for C, ~31.8 ppm for H)")
    sigma_TMS_C = 188.0  # Literature value for PBE0/6-311G**
    sigma_TMS_H = 31.8   # Literature value for PBE0/6-311G**

# Get ethanol shieldings
ethanol_shieldings = get_ethanol_shieldings()
if not ethanol_shieldings:
    print("❌ Could not find ethanol shielding values")
    print("   Run ethanol_nmr_01.py first")
    exit()

# Get atom symbols
ethanol = Atoms(
    'C2H6O',
    positions=[
        [ 0.0000,  0.0000,  0.0000],
        [ 1.5000,  0.0000,  0.0000],
        [ 2.1000,  1.2000,  0.0000],
        [-0.4000, -0.5000,  0.9000],
        [-0.4000, -0.5000, -0.9000],
        [-0.4000,  1.1000,  0.0000],
        [ 1.8000, -0.5000, -0.9000],
        [ 1.8000, -0.5000,  0.9000],
        [ 2.8000,  1.2000,  0.0000],
    ]
)

atom_symbols = ethanol.get_chemical_symbols()

print(f"\nTMS Reference Values:")
print(f"  ¹³C σ_TMS = {sigma_TMS_C:.4f} ppm")
print(f"  ¹H σ_TMS  = {sigma_TMS_H:.4f} ppm")
print("\n" + "="*60)

print("\n📊 Ethanol Chemical Shifts (δ = σ_TMS - σ_sample):")
print("   Atom Type  |  σ_sample (ppm)  |  δ (ppm)")
print("-" * 50)

for i, (symbol, sigma) in enumerate(zip(atom_symbols, ethanol_shieldings)):
    if symbol == 'C':
        delta = sigma_TMS_C - sigma
        label = f"C{i+1}"
        if i == 0:
            type_label = "CH₂OH"
        else:
            type_label = "CH₃"
    elif symbol == 'H':
        delta = sigma_TMS_H - sigma
        if i == 2:
            label = "H3"
            type_label = "OH"
        else:
            label = f"H{i+1}"
            type_label = "CH"
    else:  # Oxygen
        delta = None
        label = "O"
        type_label = "Oxygen"
    
    if delta is not None:
        print(f"  {label:4s} ({type_label:6s}) | {sigma:12.4f}     | {delta:8.4f}")

print("\n" + "="*60)

# Calculate average chemical shifts
c_shifts = []
h_ch_shifts = []
h_oh_shift = None

for i, (symbol, sigma) in enumerate(zip(atom_symbols, ethanol_shieldings)):
    if symbol == 'C':
        c_shifts.append(sigma_TMS_C - sigma)
    elif symbol == 'H':
        if i == 2:  # OH proton
            h_oh_shift = sigma_TMS_H - sigma
        else:
            h_ch_shifts.append(sigma_TMS_H - sigma)

if c_shifts:
    print(f"\n📈 Summary:")
    print(f"  Average ¹³C chemical shift: {sum(c_shifts)/len(c_shifts):.4f} ppm")
    print(f"  C1 (CH₂OH): {c_shifts[0]:.4f} ppm")
    print(f"  C2 (CH₃):   {c_shifts[1]:.4f} ppm")
    
    # Compare to experimental values
    exp_c1 = 58.0  # CH₂OH experimental
    exp_c2 = 18.0  # CH₃ experimental
    print(f"\n  Experimental ¹³C shifts:")
    print(f"    CH₂OH: {exp_c1:.1f} ppm (calc: {c_shifts[0]:.1f} ppm)")
    print(f"    CH₃:   {exp_c2:.1f} ppm (calc: {c_shifts[1]:.1f} ppm)")

if h_ch_shifts:
    print(f"\n  Average ¹H (CH) chemical shift: {sum(h_ch_shifts)/len(h_ch_shifts):.4f} ppm")
    if h_oh_shift:
        print(f"  OH proton: {h_oh_shift:.4f} ppm")
    
    # Compare to experimental values
    exp_ch = 1.0  # CH protons experimental
    exp_oh = 5.5  # OH proton experimental
    print(f"\n  Experimental ¹H shifts:")
    print(f"    CH protons: ~{exp_ch:.1f} ppm (calc: {sum(h_ch_shifts)/len(h_ch_shifts):.1f} ppm)")
    if h_oh_shift:
        print(f"    OH proton:  ~{exp_oh:.1f} ppm (calc: {h_oh_shift:.1f} ppm)")

print("\n" + "="*60)
print("✅ Chemical shift analysis complete!")
