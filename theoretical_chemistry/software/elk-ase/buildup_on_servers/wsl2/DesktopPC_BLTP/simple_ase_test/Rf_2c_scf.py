import numpy as np
from ase import Atoms
from ase.calculators.elk import ELK, ElkProfile
from ase.spacegroup import crystal

# --- 1. Define the crystal structure for Rf ---
# Rutherfordium is predicted to have an hcp structure like other group 4 elements
# Estimated lattice parameters (these may need adjustment)
a = 3.8  # Approximate lattice parameter for Rf in Å
c = 6.2  # Approximate c/a ratio ~1.63 for ideal hcp

# Create an hcp crystal structure for Rutherfordium.
# hcp has two atoms per unit cell at (0,0,0) and (1/3, 2/3, 1/2)
Rf = crystal('Rf', basis=[(0, 0, 0), (2/3, 1/3, 1/2)], 
              spacegroup=194, cellpar=[a, a, c, 90, 90, 120])

print(f"Rutherfordium crystal structure:")
print(f"Space group: 194 (hcp)")
print(f"Lattice parameters: a = {a:.3f} Å, c = {c:.3f} Å")
print(f"Number of atoms in unit cell: {len(Rf)}")

# --- 2. Set up the Elk calculator ---
# Define the path to the Elk executable and species files
elk_exe = '/home/milias/work/software/elk/elk-11.0.2/src/elk'
species_path = '/home/milias/work/software/elk/elk-11.0.2/species/'

elk_profile = ElkProfile(command=elk_exe, sppath=species_path)

# Set up calculator with parameters for superheavy element
calc = ELK(profile=elk_profile,
           directory='./rf_scf',  # Directory for calculation files
           label='rf',            # Prefix for output files

           # --- Key Parameters for a Two-Component SO-SCF Run ---
           
           # Tasks: [0] is a ground-state SCF calculation
           tasks=[0], 
           
           # Enable spin-polarization and spin-orbit coupling.
           # Setting spinorb=True will automatically enable spinpol.
           spinpol=True, 
           spinorb=True, 
           
           # Dense k-point grid for heavy elements
           ngridk=[12, 12, 12], 
           
           # --- Important SCF settings for heavy elements ---
           
           # 'gmaxvr' controls the basis size. Higher value for better accuracy
           gmaxvr=12.0, 
           
           # 'rgkmax' controls muffin-tin radius times plane-wave cutoff
           rgkmax=8.0,
           
           # Smearing to help with convergence in metals
           swidth=0.01,
           
           # Number of empty bands (important for heavy elements)
           nempty=15,
           
           # SCF convergence parameters
           maxscl=150,
           epspot=1e-6,
           
           # Additional parameters for heavy elements
           # 'fsmtype' controls the Fermi smearing type (0=Gaussian)
           fsmtype=0,
           
           # 'stype' controls the spin type (0=non-collinear, 2=spin-orbit)
           stype=2,
           
           # 'nspins' = 4 for non-collinear spin-orbit calculations
           nspins=4,
           
           # 'chgmult' charge mixing multiplier for better convergence
           chgmult=0.3,
           
           # 'maxit' maximum number of iterations for the density mixing
           maxit=50,
           )

# Attach the calculator to the atoms object
Rf.set_calculator(calc)

# --- 3. Display calculation information ---
print("\n" + "="*60)
print("Starting two-component SO-SCF calculation for Rutherfordium (Rf)")
print("="*60)
print(f"Elk executable: {elk_exe}")
print(f"Species path: {species_path}")
print(f"Calculation directory: ./rf_scf")
print(f"k-point grid: 12x12x12")
print(f"Spin-orbit coupling: Enabled")
print("="*60 + "\n")

# --- 4. Run the SCF calculation and extract energy ---
try:
    # This triggers the SCF calculation.
    energy = Rf.get_potential_energy()
    print(f"✅ SCF calculation converged successfully!")
    print(f"Total energy per unit cell: {energy:.6f} eV")
    print(f"Total energy per atom: {energy/len(Rf):.6f} eV")
    
    # Optional: Access other properties
    # forces = Rf.get_forces()
    # print(f"Forces: {forces}")
    
    # Try to get magnetic moment if available
    try:
        magmom = Rf.get_magnetic_moment()
        print(f"Total magnetic moment: {magmom:.4f} μB")
    except:
        pass

except Exception as e:
    print(f"❌ An error occurred during the SCF calculation: {e}")
    print("\nPlease check the Elk output files in the './rf_scf' directory for details.")
    print("Common issues:")
    print("  - Check if Rf.in species file is valid")
    print("  - Adjust ngridk, gmaxvr, or rgkmax if convergence fails")
    print("  - Try increasing swidth if system is metallic")
