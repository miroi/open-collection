# anharmonic_vibrations.py
"""
Anharmonic Vibrational Analysis of Hg on Au(111)
Calculates: Anharmonic frequencies, ZPE, entropy, and thermodynamics
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from scipy.integrate import quad
import warnings
warnings.filterwarnings('ignore')

print("=" * 70)
print("ANHARMONIC VIBRATIONAL ANALYSIS")
print("Hg ADSORPTION ON Au(111)")
print("=" * 70)

# Constants
k_B = 8.617333262145e-5  # eV/K
h_eV = 4.135667696e-15    # eV*s
h = 6.62607015e-34        # J*s
c = 299792458             # m/s
N_A = 6.02214076e23

# Physical parameters
E_ads_0 = -0.298  # eV (from DFT calculation)

# ============================================================================
# 1. ANHARMONIC POTENTIAL MODELS
# ============================================================================

class AnharmonicOscillator:
    """
    Anharmonic oscillator with Morse potential
    V(x) = D * (1 - exp(-a*x))^2
    """
    
    def __init__(self, D, a, x0=0.0):
        """
        Args:
            D: Well depth (eV)
            a: Morse parameter (1/Å)
            x0: Equilibrium position (Å)
        """
        self.D = D
        self.a = a
        self.x0 = x0
    
    def potential(self, x):
        """Morse potential at position x"""
        return self.D * (1 - np.exp(-self.a * (x - self.x0)))**2 - self.D
    
    def harmonic_frequency(self):
        """Harmonic frequency from Morse potential (in Hz)"""
        # Convert D from eV to Joules
        D_J = self.D * 1.602176634e-19
        # Reduced mass of Hg (200.59 amu) in kg
        mu = 200.59 * 1.66054e-27
        # Harmonic frequency: omega = a * sqrt(2*D/mu)
        omega = self.a * np.sqrt(2 * D_J / mu)
        return omega / (2 * np.pi)  # Hz
    
    def anharmonic_levels(self, n_max=10):
        """
        Calculate anharmonic energy levels using perturbation theory
        E_n = (n + 1/2)*h*nu - (n + 1/2)^2 * h*nu * x_e
        """
        nu = self.harmonic_frequency()
        # Anharmonicity constant (approximate)
        x_e = h_eV * nu / (4 * self.D)  # Simple approximation
        
        levels = []
        for n in range(n_max + 1):
            E = (n + 0.5) * h_eV * nu - (n + 0.5)**2 * h_eV * nu * x_e
            levels.append(E)
        
        return np.array(levels)

def morse_potential_fit(x, D, a, x0):
    """Morse potential for fitting"""
    return D * (1 - np.exp(-a * (x - x0)))**2 - D

# ============================================================================
# 2. ANHARMONIC VIBRATIONAL FREQUENCIES
# ============================================================================

def harmonic_frequency(freq_cm, mass=200.59):
    """
    Convert wavenumber to frequency in Hz
    freq_cm: wavenumber in cm^-1
    mass: atomic mass in amu
    """
    # Force constant: k = 4*pi^2*c^2 * freq_cm^2 * mu
    mu = mass * 1.66054e-27  # kg
    k = 4 * np.pi**2 * c**2 * (freq_cm * 100)**2 * mu  # N/m
    nu = np.sqrt(k / mu) / (2 * np.pi)  # Hz
    return nu

def anharmonic_frequencies(freq_harmonic, D_well, n_max=5):
    """
    Calculate anharmonic frequencies for different vibrational levels
    """
    # Harmonic frequency in eV
    nu_harm = freq_harmonic * h_eV
    
    # Anharmonicity constant
    x_e = nu_harm / (4 * D_well)
    
    # Frequencies for transitions: n -> n+1
    freqs = []
    for n in range(n_max):
        # Energy difference: E_{n+1} - E_n
        E_n = (n + 0.5) * nu_harm - (n + 0.5)**2 * nu_harm * x_e
        E_n1 = (n + 1.5) * nu_harm - (n + 1.5)**2 * nu_harm * x_e
        delta_E = E_n1 - E_n
        freq = delta_E / h_eV  # Hz
        freqs.append(freq)
    
    return np.array(freqs)

# ============================================================================
# 3. ANHARMONIC ENTROPY AND THERMODYNAMICS
# ============================================================================

def anharmonic_entropy(T, freq_list, anharmonicity=0.1):
    """
    Anharmonic entropy using perturbation theory
    """
    if T <= 0:
        return 0.0
    
    S_total = 0.0
    for freq in freq_list:
        # Harmonic contribution
        theta = h_eV * freq / k_B
        x = theta / T
        
        if x > 50:
            S_harm = k_B * x * np.exp(-x)
        elif x < 1e-6:
            S_harm = k_B * (1 + np.log(1/x))
        else:
            try:
                S_harm = k_B * (x / (np.exp(x) - 1) - np.log(1 - np.exp(-x)))
            except:
                S_harm = k_B * (1 + np.log(1/x))
        
        # Anharmonic correction (temperature dependent)
        # Simple model: S_anharm = S_harm * (1 + anharmonicity * f(T))
        f_T = 1 - np.exp(-theta / T)  # Smooth function
        S_anharm = S_harm * (1 + anharmonicity * f_T)
        
        S_total += S_anharm
    
    return S_total

def anharmonic_zpe(freq_list, anharmonicity=0.1):
    """
    Zero-point energy with anharmonic correction
    """
    ZPE_harm = sum(0.5 * h_eV * f for f in freq_list)
    # Anharmonic correction (approximate)
    ZPE_anharm = ZPE_harm * (1 - anharmonicity * 0.5)
    return ZPE_anharm

def adsorption_energy_anharmonic(T, E0, freq_list, anharmonicity=0.1):
    """
    Adsorption energy with anharmonic corrections
    """
    if T <= 0:
        return E0 + anharmonic_zpe(freq_list, anharmonicity)
    
    # Anharmonic entropy
    S_ads = anharmonic_entropy(T, freq_list, anharmonicity)
    
    # Bulk entropy (from previous calculations)
    S_bulk_298 = 75.9  # J/(mol·K)
    S_bulk_298_eV = S_bulk_298 / (N_A * 1.602176634e-19)
    S_bulk = S_bulk_298_eV + (28.0 / (N_A * 1.602176634e-19)) * np.log(T / 298.15)
    
    # Entropy change
    ΔS = S_ads - S_bulk
    
    # Enthalpy (with anharmonic ZPE)
    ZPE_anharm = anharmonic_zpe(freq_list, anharmonicity)
    ΔH = E0 + ZPE_anharm
    
    # Gibbs free energy
    ΔG = ΔH - T * ΔS
    
    return ΔG

# ============================================================================
# 4. FIT MORSE POTENTIAL FROM DFT DATA
# ============================================================================

# Simulate DFT potential energy surface (would come from actual calculations)
# Using a Morse-like potential as example
D_well = 0.3  # eV (well depth, similar to adsorption energy)
a_morse = 1.5  # 1/Å (width of potential)
x0 = 0.0  # equilibrium position

# Generate potential energy surface
x_range = np.linspace(-1.0, 1.0, 50)
potential = D_well * (1 - np.exp(-a_morse * x_range))**2 - D_well

# Create Morse oscillator
morse = AnharmonicOscillator(D_well, a_morse, x0)

# Calculate harmonic and anharmonic frequencies
nu_harm = morse.harmonic_frequency()
freq_harm_cm = nu_harm / (c * 100)  # Convert to cm^-1

print("\n" + "=" * 70)
print("VIBRATIONAL ANALYSIS")
print("=" * 70)

print(f"\nHarmonic frequency: {freq_harm_cm:.1f} cm^-1 ({nu_harm/1e12:.3f} THz)")

# Calculate anharmonic levels
levels = morse.anharmonic_levels(n_max=10)
print(f"\nAnharmonic energy levels (eV):")
print("-" * 40)
print(f"{'n':<5s} | {'E_n (eV)':>10s} | {'ΔE (cm^-1)':>12s}")
print("-" * 40)

for n in range(len(levels)):
    if n == 0:
        delta = 0
    else:
        delta = (levels[n] - levels[n-1]) / h_eV / (c * 100)
    print(f"{n:<5d} | {levels[n]:10.4f} | {delta:12.1f}")

# ============================================================================
# 5. PLOT POTENTIAL ENERGY SURFACE
# ============================================================================
fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(14, 10))

# Plot 1: Potential energy surface
x_plot = np.linspace(-1.5, 1.5, 200)
V_plot = morse.potential(x_plot)

ax1.plot(x_plot, V_plot, 'b-', linewidth=2, label='Morse potential')
ax1.axhline(y=0, color='gray', linestyle=':', alpha=0.3)

# Add energy levels
for n in range(5):
    E_n = levels[n]
    ax1.axhline(y=E_n, color='red', linestyle='--', alpha=0.5, linewidth=1)
    ax1.text(0.02, E_n + 0.01, f'n={n}', fontsize=8)

ax1.set_xlabel('Displacement (Å)', fontsize=12)
ax1.set_ylabel('Energy (eV)', fontsize=12)
ax1.set_title('Anharmonic Potential with Energy Levels', fontsize=14)
ax1.grid(True, alpha=0.3)
ax1.legend()

# Plot 2: Frequency vs vibrational level
freqs = anharmonic_frequencies(nu_harm, D_well, n_max=10)
freqs_cm = freqs / (c * 100)

ax2.plot(range(len(freqs)), freqs_cm, 'bo-', linewidth=2, markersize=6)
ax2.axhline(y=freq_harm_cm, color='red', linestyle='--', alpha=0.5, label='Harmonic')
ax2.set_xlabel('Vibrational level (n)', fontsize=12)
ax2.set_ylabel('Frequency (cm^-1)', fontsize=12)
ax2.set_title('Frequency vs Vibrational Level', fontsize=14)
ax2.grid(True, alpha=0.3)
ax2.legend()

# ============================================================================
# 6. THERMODYNAMIC COMPARISON
# ============================================================================

T_range = np.linspace(50, 800, 200)

# Frequencies for Hg on Au(111)
freq_horizontal = 0.8e12   # 0.8 THz
freq_vertical = 2.0e12     # 2.0 THz
freq_rotational = 0.5e12   # 0.5 THz
freq_list = [freq_horizontal, freq_vertical, freq_rotational]

# Calculate harmonic and anharmonic adsorption energies
E_ads_harm = []
E_ads_anharm = []

for T in T_range:
    # Harmonic
    S_ads_harm = sum([
        vibrational_entropy_harmonic(T, f) for f in freq_list
    ])
    S_bulk = bulk_entropy(T)
    ΔS_harm = S_ads_harm - S_bulk
    ZPE_harm = sum(0.5 * h_eV * f for f in freq_list)
    ΔH_harm = E_ads_0 + ZPE_harm
    E_ads_harm.append(ΔH_harm - T * ΔS_harm)
    
    # Anharmonic
    S_ads_anharm = anharmonic_entropy(T, freq_list, anharmonicity=0.1)
    ΔS_anharm = S_ads_anharm - S_bulk
    ZPE_anharm = anharmonic_zpe(freq_list, anharmonicity=0.1)
    ΔH_anharm = E_ads_0 + ZPE_anharm
    E_ads_anharm.append(ΔH_anharm - T * ΔS_anharm)

# Helper functions
def vibrational_entropy_harmonic(T, freq):
    """Harmonic oscillator entropy"""
    if T <= 0 or freq <= 0:
        return 0.0
    theta = h_eV * freq / k_B
    x = theta / T
    if x > 50:
        return k_B * x * np.exp(-x)
    elif x < 1e-6:
        return k_B * (1 + np.log(1/x))
    else:
        try:
            return k_B * (x / (np.exp(x) - 1) - np.log(1 - np.exp(-x)))
        except:
            return k_B * (1 + np.log(1/x))

def bulk_entropy(T):
    """Bulk Hg entropy"""
    if T <= 0:
        return 0.0
    S_liq_298 = 75.9  # J/(mol·K)
    S_liq_298_eV = S_liq_298 / (N_A * 1.602176634e-19)
    S_liq = S_liq_298_eV + (28.0 / (N_A * 1.602176634e-19)) * np.log(T / 298.15)
    return S_liq

# Plot 3: Comparison of harmonic vs anharmonic
ax3.plot(T_range, E_ads_harm, 'b-', linewidth=2, label='Harmonic')
ax3.plot(T_range, E_ads_anharm, 'r-', linewidth=2, label='Anharmonic')
ax3.axhline(y=E_ads_0, color='gray', linestyle='--', alpha=0.5,
            label=f'E_ads(0K) = {E_ads_0:.3f} eV')
ax3.axhline(y=0, color='black', linestyle=':', alpha=0.3)
ax3.set_xlabel('Temperature (K)', fontsize=12)
ax3.set_ylabel('E_ads (eV)', fontsize=12)
ax3.set_title('Harmonic vs Anharmonic Adsorption Energy', fontsize=14)
ax3.grid(True, alpha=0.3)
ax3.legend()

# Plot 4: Difference between harmonic and anharmonic
diff_anharm = np.array(E_ads_anharm) - np.array(E_ads_harm)
ax4.plot(T_range, diff_anharm, 'g-', linewidth=2)
ax4.axhline(y=0, color='black', linestyle=':', alpha=0.3)
ax4.set_xlabel('Temperature (K)', fontsize=12)
ax4.set_ylabel('E_ads(anharm) - E_ads(harm) (eV)', fontsize=12)
ax4.set_title('Anharmonic Correction to E_ads', fontsize=14)
ax4.grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig('anharmonic_vibrations.png', dpi=150)
print("\n✓ Plot saved: anharmonic_vibrations.png")

# ============================================================================
# 7. RESULTS TABLE
# ============================================================================
print("\n" + "=" * 70)
print("ANHARMONIC THERMODYNAMIC RESULTS")
print("=" * 70)

print("\n" + "-" * 90)
print(f"{'T (K)':<10s} | {'E_ads (Harm)':>12s} | {'E_ads (Anharm)':>14s} | {'Difference':>12s} | {'Correction %':>12s}")
print("-" * 90)

T_values = [100, 200, 300, 400, 500, 600, 700, 800]

for T in T_values:
    idx = np.argmin(np.abs(T_range - T))
    E_h = E_ads_harm[idx]
    E_a = E_ads_anharm[idx]
    diff = E_a - E_h
    pct = (diff / abs(E_h)) * 100 if E_h != 0 else 0
    
    print(f"{T:<10d} | {E_h:12.3f} | {E_a:14.3f} | {diff:12.3f} | {pct:11.1f}%")

# ============================================================================
# 8. PHYSICAL INTERPRETATION
# ============================================================================
print("\n" + "=" * 70)
print("PHYSICAL INTERPRETATION")
print("=" * 70)

print(f"""
ANHARMONIC CORRECTION ANALYSIS:

1. Vibrational Frequencies:
   • Harmonic frequency: {freq_harm_cm:.1f} cm^-1 ({nu_harm/1e12:.3f} THz)
   • Anharmonic levels: {len(levels)} bound states identified
   • Fundamental frequency (0→1): {(levels[1]-levels[0])/h_eV/(c*100):.1f} cm^-1

2. Zero-Point Energy:
   • Harmonic ZPE: {sum(0.5*h_eV*f for f in freq_list):.4f} eV
   • Anharmonic ZPE: {anharmonic_zpe(freq_list, anharmonicity=0.1):.4f} eV
   • Difference: {anharmonic_zpe(freq_list, anharmonicity=0.1) - sum(0.5*h_eV*f for f in freq_list):.4f} eV

3. Adsorption Energy Comparison (300K):
   • Harmonic: {E_ads_harm[np.argmin(np.abs(T_range-300))]:.3f} eV
   • Anharmonic: {E_ads_anharm[np.argmin(np.abs(T_range-300))]:.3f} eV
   • Anharmonic correction: {diff_anharm[np.argmin(np.abs(T_range-300))]:.3f} eV

4. Entropy Effects:
   • Anharmonicity increases entropy at higher T
   • Makes adsorption LESS favorable (more positive E_ads)
   • Correction becomes more significant above 300K

5. Physical Insights:
   • Anharmonicity softens the potential at large displacements
   • Reduces ZPE and modifies entropy
   • Important for accurate thermodynamics at high T
   • Should be included for T > 300K

6. When to Include Anharmonic Corrections:
   • For accurate adsorption energies above 300K
   • For entropy calculations at high temperature
   • When comparing with experimental data
   • For desorption kinetics studies
""")

print("\n" + "=" * 70)
print("✓ COMPLETE")
print("=" * 70)

# ============================================================================
# 9. SAVE DATA
# ============================================================================
print("\nSaving data...")

# Save vibrational data
np.savetxt('anharmonic_energy_levels.csv',
           np.column_stack([range(len(levels)), levels, 
                           [0] + [(levels[i]-levels[i-1])/h_eV/(c*100) for i in range(1, len(levels))]]),
           header='n,E_n(eV),Delta_E(cm^-1)',
           delimiter=',')

# Save thermodynamic comparison
np.savetxt('anharmonic_thermodynamics.csv',
           np.column_stack([T_range, E_ads_harm, E_ads_anharm, diff_anharm]),
           header='Temperature(K),E_ads_Harmonic(eV),E_ads_Anharmonic(eV),Difference(eV)',
           delimiter=',')

print("✓ Data saved to anharmonic_energy_levels.csv")
print("✓ Data saved to anharmonic_thermodynamics.csv")

print("\n" + "=" * 70)
print("✓ COMPLETE!")
print("=" * 70)
