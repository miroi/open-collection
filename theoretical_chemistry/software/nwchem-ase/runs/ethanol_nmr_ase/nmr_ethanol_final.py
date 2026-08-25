# nmr_ethanol_final.py
import os
import glob
import re
from ase import Atoms

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

print("📊 Calculating Chemical Shifts for Ethanol")
print("="*60)

# TMS reference values from the calculation
sigma_TMS_C = 33.2208  # Average of 4 carbons in TMS
sigma_TMS_H = 27.3155  # Average of 12 hydrogens in TMS

print(f"✅ Using TMS shielding values from calculation:")
print(f"   C_TMS = {sigma_TMS_C:.4f} ppm")
print(f"   H_TMS = {sigma_TMS_H:.4f} ppm")
print("")

# Get ethanol shieldings
ethanol_shieldings = get_ethanol_shieldings()

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

print("📊 Ethanol Chemical Shifts (δ = σ_TMS - σ_sample):")
print("   Atom  |  Type     |  σ_sample (ppm)  |  δ_calc (ppm)")
print("-" * 65)

results = []
c_results = []
h_ch_results = []
h_oh_result = None

for i, (symbol, sigma) in enumerate(zip(atom_symbols, ethanol_shieldings)):
    if symbol == 'C':
        delta = sigma_TMS_C - sigma
        if i == 0:
            label = "C1"
            type_label = "CH₂OH"
            c_results.append(('C1', delta))
        else:
            label = "C2"
            type_label = "CH₃"
            c_results.append(('C2', delta))
        print(f"  {label:4s}  |  {type_label:8s} |  {sigma:12.4f}     |  {delta:10.4f}")
    elif symbol == 'H':
        delta = sigma_TMS_H - sigma
        if i == 2:
            label = "H3"
            type_label = "OH"
            h_oh_result = delta
        else:
            label = f"H{i+1}"
            type_label = "CH"
            h_ch_results.append((label, delta))
        print(f"  {label:4s}  |  {type_label:8s} |  {sigma:12.4f}     |  {delta:10.4f}")
    else:  # Oxygen
        print(f"  O    |  Oxygen    |  {sigma:12.4f}     |  -")

print("\n" + "="*65)

# Summary
print("\n📈 Summary of Chemical Shifts:")

if c_results:
    print(f"\n  ¹³C NMR (δ = {sigma_TMS_C:.2f} - σ_sample):")
    for label, delta in c_results:
        print(f"    {label}: {delta:.4f} ppm")
    avg_c = sum(d for _, d in c_results) / len(c_results)
    print(f"    Average: {avg_c:.4f} ppm")

if h_ch_results:
    print(f"\n  ¹H NMR (CH protons, δ = {sigma_TMS_H:.2f} - σ_sample):")
    for label, delta in h_ch_results:
        print(f"    {label}: {delta:.4f} ppm")
    avg_h_ch = sum(d for _, d in h_ch_results) / len(h_ch_results)
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
            print(f"  C1 (CH₂OH): calculated = {delta:.1f} ppm, experimental = {exp_c1:.1f} ppm")
            print(f"    Difference: {delta - exp_c1:.1f} ppm")
        elif label == 'C2':
            print(f"  C2 (CH₃):   calculated = {delta:.1f} ppm, experimental = {exp_c2:.1f} ppm")
            print(f"    Difference: {delta - exp_c2:.1f} ppm")

if h_ch_results:
    exp_h_ch = 1.0  # CH protons experimental
    avg_h_ch = sum(d for _, d in h_ch_results) / len(h_ch_results)
    print(f"\n  CH protons:   calculated = {avg_h_ch:.1f} ppm, experimental = {exp_h_ch:.1f} ppm")
    print(f"    Difference: {avg_h_ch - exp_h_ch:.1f} ppm")

if h_oh_result is not None:
    exp_h_oh = 5.5  # OH proton experimental
    print(f"  OH proton:    calculated = {h_oh_result:.1f} ppm, experimental = {exp_h_oh:.1f} ppm")
    print(f"    Difference: {h_oh_result - exp_h_oh:.1f} ppm")

print("\n" + "="*65)
print("💡 Note: Chemical shifts depend on solvent, concentration, and temperature.")
print("   The PBE0/6-311G** method is in gas phase; experimental values are in D₂O.")
print("   Better agreement can be achieved with:")
print("   - Larger basis sets (cc-pVTZ, def2-TZVPP)")
print("   - Solvent effects (PCM or COSMO)")
print("   - Empirical scaling/regression")
print("="*65)
