# nmr_ethanol_with_shifts.py
import os
import glob
import re
from ase import Atoms

def get_shielding_values(output_pattern):
    """Get shielding values from NWChem output"""
    output_files = glob.glob(f'{output_pattern}.out') + glob.glob(f'{output_pattern}.log')
    
    if not output_files:
        return None
    
    with open(output_files[0], 'r') as f:
        content = f.read()
    
    pattern = r'isotropic\s*=\s*([0-9.]+)'
    matches = re.findall(pattern, content)
    
    if matches:
        return [float(val) for val in matches]
    return None

def get_tms_from_file():
    """Get TMS shielding values from saved file"""
    if os.path.exists('tms_shieldings.txt'):
        with open('tms_shieldings.txt', 'r') as f:
            content = f.read()
        
        c_avg = None
        h_avg = None
        
        for line in content.split('\n'):
            if 'C_avg' in line:
                c_avg = float(line.split('=')[1].strip())
            elif 'H_avg' in line:
                h_avg = float(line.split('=')[1].strip())
        
        if c_avg and h_avg:
            return {'C': c_avg, 'H': h_avg}
    
    # Try to import from Python file
    if os.path.exists('tms_values.py'):
        try:
            with open('tms_values.py', 'r') as f:
                content = f.read()
                # Extract values using regex
                c_match = re.search(r'C_TMS\s*=\s*([0-9.]+)', content)
                h_match = re.search(r'H_TMS\s*=\s*([0-9.]+)', content)
                if c_match and h_match:
                    return {'C': float(c_match.group(1)), 'H': float(h_match.group(1))}
        except:
            pass
    
    return None

print("📊 Calculating Chemical Shifts for Ethanol")
print("="*60)

# Load TMS values
tms_data = get_tms_from_file()

if tms_data and tms_data['C'] and tms_data['H']:
    sigma_TMS_C = tms_data['C']
    sigma_TMS_H = tms_data['H']
    print(f"✅ Using TMS shielding values from calculation:")
    print(f"   C_TMS = {sigma_TMS_C:.4f} ppm")
    print(f"   H_TMS = {sigma_TMS_H:.4f} ppm")
else:
    print("⚠️  TMS calculation not found!")
    print("   Run nmr_tms_calc.py first to get accurate TMS values.")
    print("   For now, using literature values...")
    sigma_TMS_C = 188.0
    sigma_TMS_H = 31.8

# Get ethanol shieldings
ethanol_shieldings = get_shielding_values('ethanol_nmr')

if not ethanol_shieldings:
    print("❌ Could not find ethanol shielding values")
    print("   Run ethanol_nmr_01.py first")
    exit()

# Define ethanol molecule for atom labeling
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

print(f"\n📊 Ethanol Chemical Shifts (δ = σ_TMS - σ_sample):")
print("   Atom  |  Type     |  σ_sample (ppm)  |  δ (ppm)")
print("-" * 65)

results = []

for i, (symbol, sigma) in enumerate(zip(atom_symbols, ethanol_shieldings)):
    if symbol == 'C':
        delta = sigma_TMS_C - sigma
        if i == 0:
            label = "C1"
            type_label = "CH₂OH"
        else:
            label = "C2"
            type_label = "CH₃"
        results.append(('C', label, type_label, sigma, delta))
    elif symbol == 'H':
        delta = sigma_TMS_H - sigma
        if i == 2:
            label = "H3"
            type_label = "OH"
        else:
            label = f"H{i+1}"
            type_label = "CH"
        results.append(('H', label, type_label, sigma, delta))
    else:  # Oxygen
        label = "O"
        type_label = "O"
        results.append(('O', label, type_label, sigma, None))

# Display results
c_results = []
h_ch_results = []
h_oh_result = None

for atom_type, label, type_label, sigma, delta in results:
    if delta is not None:
        print(f"  {label:4s}  |  {type_label:8s} |  {sigma:12.4f}     |  {delta:10.4f}")
        if atom_type == 'C':
            c_results.append((label, delta))
        elif atom_type == 'H':
            if type_label == 'OH':
                h_oh_result = delta
            else:
                h_ch_results.append(delta)

print("\n" + "="*65)

# Summary
print("\n📈 Summary of Chemical Shifts:")

if c_results:
    avg_c = sum(d[1] for d in c_results) / len(c_results)
    print(f"\n  ¹³C NMR:")
    for label, delta in c_results:
        print(f"    {label} ({'CH₂OH' if label == 'C1' else 'CH₃'}): {delta:.4f} ppm")
    print(f"    Average: {avg_c:.4f} ppm")

if h_ch_results:
    avg_h_ch = sum(h_ch_results) / len(h_ch_results)
    print(f"\n  ¹H NMR (CH protons):")
    for i, delta in enumerate(h_ch_results, start=4):
        print(f"    H{i}: {delta:.4f} ppm")
    print(f"    Average: {avg_h_ch:.4f} ppm")

if h_oh_result is not None:
    print(f"\n  ¹H NMR (OH proton):")
    print(f"    H3: {h_oh_result:.4f} ppm")

# Compare with experimental
print("\n" + "="*65)
print("📊 Comparison with Experimental Values (in D₂O):")
print("-" * 65)

if c_results:
    exp_c1 = 58.0  # CH₂OH experimental
    exp_c2 = 18.0  # CH₃ experimental
    for label, delta in c_results:
        if label == 'C1':
            print(f"  {label} (CH₂OH): calculated = {delta:.1f} ppm, experimental = {exp_c1:.1f} ppm")
            print(f"    Difference: {delta - exp_c1:.1f} ppm")
        elif label == 'C2':
            print(f"  {label} (CH₃):   calculated = {delta:.1f} ppm, experimental = {exp_c2:.1f} ppm")
            print(f"    Difference: {delta - exp_c2:.1f} ppm")

if h_ch_results:
    exp_h_ch = 1.0  # CH protons experimental
    avg_h_ch = sum(h_ch_results) / len(h_ch_results)
    print(f"\n  CH protons:   calculated = {avg_h_ch:.1f} ppm, experimental = {exp_h_ch:.1f} ppm")
    print(f"    Difference: {avg_h_ch - exp_h_ch:.1f} ppm")

if h_oh_result is not None:
    exp_h_oh = 5.5  # OH proton experimental
    print(f"  OH proton:    calculated = {h_oh_result:.1f} ppm, experimental = {exp_h_oh:.1f} ppm")
    print(f"    Difference: {h_oh_result - exp_h_oh:.1f} ppm")

print("\n" + "="*65)
print("💡 Note: Chemical shifts depend on solvent, concentration, and temperature.")
print("   Better agreement can be achieved with:")
print("   - Larger basis sets (cc-pVTZ, def2-TZVPP)")
print("   - Solvent effects (PCM)")
print("   - Empirical scaling/regression")
print("="*65)
