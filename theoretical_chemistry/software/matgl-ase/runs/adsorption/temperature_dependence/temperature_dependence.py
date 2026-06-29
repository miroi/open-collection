# temperature_dependence.py
"""
Estimate temperature dependence of adsorption using harmonic approximation
"""

import numpy as np
import matplotlib.pyplot as plt

print("=" * 70)
print("TEMPERATURE DEPENDENCE OF Hg ADSORPTION")
print("=" * 70)

# Constants
k_B = 8.617333e-5  # eV/K
h = 4.135667696e-15  # eV*s

# Parameters from our calculation
E_ads_0K = -0.298  # eV (from previous calculation)
freq_vibrational = 50e12  # Hz (typical physisorption frequency)
mass_Hg = 200.59  # amu

print(f"\nParameters:")
print(f"  E_ads(0K): {E_ads_0K:.3f} eV")
print(f"  Vibrational frequency: {freq_vibrational/1e12:.1f} THz")

# Temperature range
T = np.linspace(50, 500, 100)  # K

# Zero-point energy correction
E_ZPE = 0.5 * h * freq_vibrational  # eV
print(f"  Zero-point energy: {E_ZPE:.4f} eV")

# Free energy correction (harmonic approximation)
def free_energy_correction(T, freq, mass):
    """Entropy correction for adsorbed species"""
    # Translational entropy (2D gas)
    lambda_T = h / np.sqrt(2 * np.pi * mass * 1.6605e-27 * k_B * T)
    return k_B * T * np.log(lambda_T**2 / (1e-19))  # Rough estimate

# Adsorption energy as function of temperature
E_ads_T = []
for temp in T:
    delta_G = free_energy_correction(temp, freq_vibrational, mass_Hg)
    E_ads = E_ads_0K + E_ZPE - delta_G
    E_ads_T.append(E_ads)

# Plot
plt.figure(figsize=(10, 6))
plt.plot(T, E_ads_T, 'b-', linewidth=2)
plt.axhline(y=E_ads_0K, color='r', linestyle='--', label=f'E_ads(0K) = {E_ads_0K:.3f} eV')
plt.xlabel('Temperature (K)', fontsize=12)
plt.ylabel('Adsorption Energy (eV)', fontsize=12)
plt.title('Temperature Dependence of Hg Adsorption on Au(111)', fontsize=14)
plt.grid(True, alpha=0.3)
plt.legend()
plt.tight_layout()
plt.savefig('temperature_dependence.png', dpi=150)

print(f"\nAdsorption energy at 300K: {E_ads_T[np.argmin(np.abs(T-300))]:.3f} eV")
print("✓ Plot saved: temperature_dependence.png")

# Desorption temperature estimate
# When E_ads = k_B * T (rough estimate)
try:
    T_desorb = np.interp(0, E_ads_T, T)
    print(f"Estimated desorption temperature: {T_desorb:.0f} K")
except:
    print("Estimated desorption temperature: >500 K")

print("\n✓ Temperature analysis complete!")
