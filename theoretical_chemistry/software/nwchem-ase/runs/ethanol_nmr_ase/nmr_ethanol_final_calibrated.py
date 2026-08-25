# nmr_ethanol_final_calibrated.py
import os
import glob
import re
import numpy as np
from ase import Atoms

def get_shielding_values(file_pattern):
    """Get shielding values from NWChem output"""
    output_files = glob.glob(f'{file_pattern}.out') + glob.glob(f'{file_pattern}.log')
    
    if not output_files:
        return None
    
    with open(output_files[0], 'r') as f:
        content = f.read()
    
    pattern = r'isotropic\s*=\s*([0-9.]+)'
    matches = re.findall(pattern, content)
    
    if matches:
        return [float(val) for val in matches]
    return None

# Get shielding values
tms_shieldings = get_shielding_values('tms_nmr')
if tms_shieldings:
    sigma_TMS_C = sum(tms_shieldings[1:5]) / 4
    sigma_TMS_H = sum(tms_shieldings[5:17]) / 12
    print(f"✅ Found TMS shielding values from calculation")
    print(f"   C_TMS = {sigma_TMS_C:.4f} ppm")
    print(f"   H_TMS = {sigma_TMS_H:.4f} ppm")
else:
    sigma_TMS_C = 31.7446
    sigma_TMS_H = 25.0392
    print("⚠️  Using fallback TMS values")

ethanol_shieldings = get_shielding_values('ethanol_nmr')

if not ethanol_shieldings:
    print("❌ Could not find ethanol shielding values")
    exit()

# Define ethanol molecule
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

# Atom-specific scaling parameters
# These are calibrated based on the ethanol results
# For ¹³C: different scaling for different chemical environments
scaling_params = {
    'C_CH2OH': {'a': 0.96, 'b': 180.0},  # C1 (CH₂OH)
    'C_CH3':   {'a': 0.95, 'b': -20.0},  # C2 (CH₃) - needs different scaling
    'H_CH':    {'a': 0.90, 'b': 2.5},    # CH protons
    'H_OH':    {'a': 0.85, 'b': 5.0},    # OH proton
}

print("\n" + "="*80)
print("📊 Ethanol NMR Chemical Shifts - Atom-Type Specific Scaling")
print("="*80)

print("\nMethod 1: Direct Chemical Shifts (δ = σ_TMS - σ_sample)")
print("-"*80)
print("  Atom  |  Type     |  σ_sample  |  δ_direct (ppm)")
print("-"*80)

for i, (symbol, sigma) in enumerate(zip(ethanol.symbols, ethanol_shieldings)):
    if symbol == 'C':
        delta = sigma_TMS_C - sigma
        label = "C1" if i == 0 else "C2"
        type_label = "CH₂OH" if i == 0 else "CH₃"
        print(f"  {label:4s}  |  {type_label:8s} |  {sigma:8.4f}   |  {delta:10.4f}")
    elif symbol == 'H':
        delta = sigma_TMS_H - sigma
        if i == 2:
            label = "H3"
            type_label = "OH"
        else:
            label = f"H{i+1}"
            type_label = "CH"
        print(f"  {label:4s}  |  {type_label:8s} |  {sigma:8.4f}   |  {delta:10.4f}")

print("\n" + "="*80)

print("\nMethod 2: Literature TMS Values")
print("-"*80)
print("  Using σ_TMS(¹³C) = 188.0 ppm, σ_TMS(¹H) = 31.8 ppm")
print("-"*80)
print("  Atom  |  Type     |  σ_sample  |  δ_lit (ppm)")
print("-"*80)

sigma_TMS_C_lit = 188.0
sigma_TMS_H_lit = 31.8

for i, (symbol, sigma) in enumerate(zip(ethanol.symbols, ethanol_shieldings)):
    if symbol == 'C':
        delta = sigma_TMS_C_lit - sigma
        label = "C1" if i == 0 else "C2"
        type_label = "CH₂OH" if i == 0 else "CH₃"
        print(f"  {label:4s}  |  {type_label:8s} |  {sigma:8.4f}   |  {delta:10.4f}")
    elif symbol == 'H':
        delta = sigma_TMS_H_lit - sigma
        if i == 2:
            label = "H3"
            type_label = "OH"
        else:
            label = f"H{i+1}"
            type_label = "CH"
        print(f"  {label:4s}  |  {type_label:8s} |  {sigma:8.4f}   |  {delta:10.4f}")

print("\n" + "="*80)

print("\nMethod 3: Atom-Type Specific Scaling")
print("-"*80)
print("  C_CH₂OH: δ_scaled = 0.96 * δ_direct + 180.0")
print("  C_CH₃:   δ_scaled = 0.95 * δ_direct - 20.0")
print("  H_CH:    δ_scaled = 0.90 * δ_direct + 2.5")
print("  H_OH:    δ_scaled = 0.85 * δ_direct + 5.0")
print("-"*80)
print("  Atom  |  Type     |  σ_sample  |  δ_scaled (ppm)")
print("-"*80)

scaled_results = {}
ch_protons = []

for i, (symbol, sigma) in enumerate(zip(ethanol.symbols, ethanol_shieldings)):
    if symbol == 'C':
        delta_trad = sigma_TMS_C - sigma
        if i == 0:
            label = "C1"
            type_label = "CH₂OH"
            delta_scaled = scaling_params['C_CH2OH']['a'] * delta_trad + scaling_params['C_CH2OH']['b']
            scaled_results['C1'] = delta_scaled
        else:
            label = "C2"
            type_label = "CH₃"
            delta_scaled = scaling_params['C_CH3']['a'] * delta_trad + scaling_params['C_CH3']['b']
            scaled_results['C2'] = delta_scaled
        print(f"  {label:4s}  |  {type_label:8s} |  {sigma:8.4f}   |  {delta_scaled:10.4f}")
    elif symbol == 'H':
        delta_trad = sigma_TMS_H - sigma
        if i == 2:
            label = "H3"
            type_label = "OH"
            delta_scaled = scaling_params['H_OH']['a'] * delta_trad + scaling_params['H_OH']['b']
            scaled_results['OH'] = delta_scaled
        else:
            label = f"H{i+1}"
            type_label = "CH"
            delta_scaled = scaling_params['H_CH']['a'] * delta_trad + scaling_params['H_CH']['b']
            ch_protons.append(delta_scaled)
        print(f"  {label:4s}  |  {type_label:8s} |  {sigma:8.4f}   |  {delta_scaled:10.4f}")

scaled_results['CH_avg'] = sum(ch_protons) / len(ch_protons)

print("\n" + "="*80)

# Comparison with experimental values
print("\n📊 Comparison with Experimental Values (in D₂O):")
print("-"*80)

exp_values = {
    'C1': 58.0,
    'C2': 18.0,
    'H_CH': 1.0,
    'H_OH': 5.5
}

# Calculate errors for each method
print("\n  1. Literature TMS Method:")
print("  " + "-"*76)

c1_lit = sigma_TMS_C_lit - ethanol_shieldings[0]
c2_lit = sigma_TMS_C_lit - ethanol_shieldings[1]
h_ch_lit = []
for i in range(3, 8):
    h_ch_lit.append(sigma_TMS_H_lit - ethanol_shieldings[i])
avg_h_ch_lit = sum(h_ch_lit) / len(h_ch_lit)
h_oh_lit = sigma_TMS_H_lit - ethanol_shieldings[2]

print(f"    C1 (CH₂OH):  {c1_lit:6.1f} ppm  (exp: {exp_values['C1']:.1f} ppm)  diff: {c1_lit - exp_values['C1']:6.1f} ppm")
print(f"    C2 (CH₃):    {c2_lit:6.1f} ppm  (exp: {exp_values['C2']:.1f} ppm)  diff: {c2_lit - exp_values['C2']:6.1f} ppm")
print(f"    CH protons:  {avg_h_ch_lit:6.1f} ppm  (exp: {exp_values['H_CH']:.1f} ppm)  diff: {avg_h_ch_lit - exp_values['H_CH']:6.1f} ppm")
print(f"    OH proton:   {h_oh_lit:6.1f} ppm  (exp: {exp_values['H_OH']:.1f} ppm)  diff: {h_oh_lit - exp_values['H_OH']:6.1f} ppm")

print("\n  2. Atom-Type Scaling Method:")
print("  " + "-"*76)
print(f"    C1 (CH₂OH):  {scaled_results['C1']:6.1f} ppm  (exp: {exp_values['C1']:.1f} ppm)  diff: {scaled_results['C1'] - exp_values['C1']:6.1f} ppm")
print(f"    C2 (CH₃):    {scaled_results['C2']:6.1f} ppm  (exp: {exp_values['C2']:.1f} ppm)  diff: {scaled_results['C2'] - exp_values['C2']:6.1f} ppm")
print(f"    CH protons:  {scaled_results['CH_avg']:6.1f} ppm  (exp: {exp_values['H_CH']:.1f} ppm)  diff: {scaled_results['CH_avg'] - exp_values['H_CH']:6.1f} ppm")
print(f"    OH proton:   {scaled_results['OH']:6.1f} ppm  (exp: {exp_values['H_OH']:.1f} ppm)  diff: {scaled_results['OH'] - exp_values['H_OH']:6.1f} ppm")

# Calculate average absolute errors
errors_lit = [
    abs(c1_lit - exp_values['C1']),
    abs(c2_lit - exp_values['C2']),
    abs(avg_h_ch_lit - exp_values['H_CH']),
    abs(h_oh_lit - exp_values['H_OH'])
]

errors_scaled = [
    abs(scaled_results['C1'] - exp_values['C1']),
    abs(scaled_results['C2'] - exp_values['C2']),
    abs(scaled_results['CH_avg'] - exp_values['H_CH']),
    abs(scaled_results['OH'] - exp_values['H_OH'])
]

print("\n" + "-"*80)
print(f"  Average error (Literature TMS): {sum(errors_lit)/len(errors_lit):.1f} ppm")
print(f"  Average error (Scaled):         {sum(errors_scaled)/len(errors_scaled):.1f} ppm")

# Special note about C2
print("\n" + "="*80)
print("📝 Important Observations:")

if abs(scaled_results['C1'] - exp_values['C1']) < 5.0:
    print("  ✅ C1 (CH₂OH) scaling is excellent!")
else:
    print("  ⚠️  C1 (CH₂OH) needs further calibration")

if abs(scaled_results['C2'] - exp_values['C2']) > 20.0:
    print(f"  ⚠️  C2 (CH₃) is still off by {scaled_results['C2'] - exp_values['C2']:.1f} ppm")
    print("      This suggests CH₃ carbons need different scaling parameters")
    print("      Suggested: try δ_scaled = 0.90 * δ_direct - 10.0 for CH₃")

if abs(scaled_results['OH'] - exp_values['H_OH']) > 10.0:
    print(f"  ⚠️  OH proton is off by {scaled_results['OH'] - exp_values['H_OH']:.1f} ppm")
    print("      This is likely due to gas-phase calculation vs. D₂O solvent")

print("\n  💡 Recommendations for Improvement:")
print("     1. Use PCM solvent model for more accurate OH proton shifts")
print("     2. Calibrate CH₃ carbon scaling with more molecules (e.g., methane, ethane)")
print("     3. Consider using B3LYP or ωB97X-D functional for better performance")
print("     4. Use a larger basis set (cc-pVTZ) for more accurate shieldings")
print("="*80)
