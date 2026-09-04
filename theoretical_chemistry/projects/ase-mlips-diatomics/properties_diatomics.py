import os
import yaml
import numpy as np
from ase import Atoms
from ase.calculators.emt import EMT
from ase.optimize import BFGS
from ase.vibrations import Vibrations
from ase.thermochemistry import IdealGasThermo
from ase.io import write, read
from ase.units import kB, mol
from datetime import datetime
import warnings
warnings.filterwarnings('ignore')

# Import MACE if available
MACE_AVAILABLE = False
try:
    from mace.calculators import MACECalculator
    MACE_AVAILABLE = True
except ImportError:
    pass

class DiatomicAnalyzer:
    def __init__(self, calculator_name='EMT', calculator_params=None):
        """Initialize with calculator type and parameters."""
        self.calculator_name = calculator_name
        self.calculator_params = calculator_params or {}
        self.calculator = None
        self.supported_elements = []
        self._initialize_calculator()
    
    def _initialize_calculator(self):
        """Initialize the calculator with proper error handling."""
        if self.calculator_name == 'EMT':
            try:
                self.calculator = EMT()
                # EMT supports a limited set of elements
                self.supported_elements = ['H', 'N', 'O', 'Cu', 'Ag', 'Au', 'Ni', 'Pd', 'Pt', 'Al']
                print(f"EMT calculator initialized. Supports: {self.supported_elements}")
            except Exception as e:
                print(f"Error initializing EMT: {e}")
                self.calculator = None
                
        elif self.calculator_name == 'MACE' and MACE_AVAILABLE:
            try:
                model = self.calculator_params.get('model', 'MACE')
                device = self.calculator_params.get('device', 'cpu')
                model_path = self.calculator_params.get('model_path', None)
                
                if model_path:
                    self.calculator = MACECalculator(model_path=model_path, device=device)
                else:
                    self.calculator = MACECalculator(model=model, device=device)
                
                # MACE supports many elements, but we'll check which ones
                self.supported_elements = ['H', 'He', 'Li', 'Be', 'B', 'C', 'N', 'O', 'F', 
                                          'Ne', 'Na', 'Mg', 'Al', 'Si', 'P', 'S', 'Cl', 
                                          'Ar', 'K', 'Ca', 'Sc', 'Ti', 'V', 'Cr', 'Mn', 
                                          'Fe', 'Co', 'Ni', 'Cu', 'Zn', 'Ga', 'Ge', 'As', 
                                          'Se', 'Br', 'Kr', 'Rb', 'Sr', 'Y', 'Zr', 'Nb', 
                                          'Mo', 'Tc', 'Ru', 'Rh', 'Pd', 'Ag', 'Cd', 'In', 
                                          'Sn', 'Sb', 'Te', 'I', 'Xe', 'Cs', 'Ba', 'La', 
                                          'Ce', 'Pr', 'Nd', 'Pm', 'Sm', 'Eu', 'Gd', 'Tb', 
                                          'Dy', 'Ho', 'Er', 'Tm', 'Yb', 'Lu', 'Hf', 'Ta', 
                                          'W', 'Re', 'Os', 'Ir', 'Pt', 'Au', 'Hg', 'Tl', 
                                          'Pb', 'Bi', 'Po', 'At', 'Rn']
                print(f"MACE calculator initialized with model: {model}")
                
            except Exception as e:
                print(f"Error initializing MACE: {e}")
                self.calculator = None
                self.supported_elements = []
        else:
            if self.calculator_name == 'MACE' and not MACE_AVAILABLE:
                print("MACE not available. Please install: pip install mace-torch")
            self.calculator = None
            self.supported_elements = []
    
    def supports_element(self, symbol):
        """Check if the calculator supports a given element."""
        if self.calculator is None:
            return False
        return symbol in self.supported_elements
    
    def create_diatomic(self, symbols, distance):
        """Create a diatomic molecule at the given distance."""
        atoms = Atoms(symbols, positions=[(0, 0, 0), (distance, 0, 0)])
        if self.calculator:
            atoms.set_calculator(self.calculator)
        return atoms
    
    def optimize_geometry(self, atoms, fmax=0.001, steps=100):
        """Optimize geometry using BFGS."""
        if self.calculator is None:
            print("No calculator available for optimization")
            return atoms
        
        opt = BFGS(atoms, trajectory=f'{self.calculator_name}_opt.traj', logfile=None)
        try:
            opt.run(fmax=fmax, steps=steps)
        except Exception as e:
            print(f"Optimization failed: {e}")
        return atoms
    
    def get_equilibrium_distance(self, symbols, initial_distance=1.2, fmax=0.001, steps=100):
        """Find equilibrium bond distance."""
        # Check if calculator supports the elements
        for symbol in symbols:
            if not self.supports_element(symbol):
                print(f"Warning: {self.calculator_name} does not support element {symbol}")
                return initial_distance, None
        
        atoms = self.create_diatomic(symbols, initial_distance)
        opt_atoms = self.optimize_geometry(atoms, fmax, steps)
        
        if opt_atoms:
            return opt_atoms.get_distance(0, 1), opt_atoms
        return initial_distance, None
    
    def calculate_dissociation_energy(self, atoms):
        """Calculate dissociation energy."""
        if atoms is None or self.calculator is None:
            return 0.0, 0.0
        
        try:
            # Energy of the molecule
            molecule_energy = atoms.get_potential_energy()
            
            # Energy of isolated atoms (far apart)
            symbols = atoms.get_chemical_symbols()
            far_distance = 10.0
            far_atoms = Atoms(symbols, positions=[(0, 0, 0), (far_distance, 0, 0)])
            far_atoms.set_calculator(self.calculator)
            atom_energy = far_atoms.get_potential_energy()
            
            # Dissociation energy (positive for bound molecule)
            diss_energy = atom_energy - molecule_energy
            diss_energy_eV = diss_energy
            diss_energy_kJmol = diss_energy * 96.485  # 1 eV = 96.485 kJ/mol
            
            return diss_energy_eV, diss_energy_kJmol
        except Exception as e:
            print(f"Error calculating dissociation energy: {e}")
            return 0.0, 0.0
    
    def calculate_vibrational_frequency(self, atoms):
        """Calculate vibrational frequency using finite differences."""
        if atoms is None or self.calculator is None:
            return 0.0
        
        try:
            # For diatomic, we need to use Vibrations
            vib = Vibrations(atoms, indices=[0, 1])
            vib.run()
            
            # Get frequencies in cm^-1
            frequencies = vib.get_frequencies()
            
            # For diatomic, take the first non-zero frequency
            valid_freqs = [f for f in frequencies if abs(f) > 1.0]
            
            if len(valid_freqs) > 0:
                freq_cm1 = abs(valid_freqs[0])
            else:
                freq_cm1 = 0.0
            
            # Clean up vibration files
            try:
                vib.clean()
            except:
                pass
                
            return freq_cm1
        except Exception as e:
            print(f"Error calculating vibrational frequency: {e}")
            return 0.0
    
    def calculate_thermochemistry(self, atoms, freq_cm1, geometry='linear', 
                                   spin=0, symmetry=2, temperature=298.15, 
                                   pressure=101325):
        """Calculate thermochemical properties using IdealGasThermo."""
        if atoms is None:
            return 0.0, 0.0, 0.0
        
        try:
            # Get vibrational energies in eV
            vib_energy_eV = freq_cm1 * 1.23984e-4
            
            # Get potential energy
            potential_energy = atoms.get_potential_energy()
            
            # Get vibrational energies as a list
            vib_energies = [vib_energy_eV] if vib_energy_eV > 0 else []
            
            # Create IdealGasThermo object
            thermo = IdealGasThermo(
                vib_energies=vib_energies,
                potentialenergy=potential_energy,
                atoms=atoms,
                geometry=geometry,
                symmetrynumber=symmetry,
                spin=spin,
                vib_selection='all'
            )
            
            # Calculate thermodynamic quantities
            enthalpy_eV = thermo.get_enthalpy(temperature)
            entropy_eVK = thermo.get_entropy(temperature, pressure)
            gibbs_eV = thermo.get_gibbs_energy(temperature, pressure)
            
            # Convert to more common units
            enthalpy_kJmol = enthalpy_eV * 96.485
            entropy_JmolK = entropy_eVK * 96.485
            gibbs_kJmol = gibbs_eV * 96.485
            
            return enthalpy_kJmol, entropy_JmolK, gibbs_kJmol
        except Exception as e:
            print(f"Error calculating thermochemistry: {e}")
            return 0.0, 0.0, 0.0
    
    def analyze_molecule(self, molecule_name, properties, config):
        """Complete analysis of a diatomic molecule."""
        print(f"\n{'='*60}")
        print(f"Analyzing {molecule_name} with {self.calculator_name}")
        print(f"{'='*60}")
        
        # Check if calculator supports the elements
        symbols = properties['symbols']
        for symbol in symbols:
            if not self.supports_element(symbol):
                print(f"✗ {self.calculator_name} does not support element {symbol}")
                print(f"  Skipping {molecule_name} analysis")
                return None, None
        
        # Get parameters from config
        temperature = config.get('temperature', 298.15)
        pressure = config.get('pressure', 101325)
        fmax = config.get('fmax', 0.001)
        max_steps = config.get('max_steps', 100)
        
        # Get equilibrium geometry
        initial_dist = properties['initial_distance']
        eq_dist, opt_atoms = self.get_equilibrium_distance(
            symbols, initial_dist, fmax, max_steps)
        
        if opt_atoms is None:
            print(f"✗ Optimization failed for {molecule_name}")
            return None, None
        
        print(f"✓ Equilibrium bond distance: {eq_dist:.4f} Å")
        
        # Calculate dissociation energy
        diss_eV, diss_kJmol = self.calculate_dissociation_energy(opt_atoms)
        if diss_eV > 0:
            print(f"✓ Dissociation energy: {diss_eV:.4f} eV ({diss_kJmol:.2f} kJ/mol)")
        else:
            print(f"⚠ Dissociation energy calculation may be incorrect: {diss_eV:.4f} eV")
        
        # Calculate vibrational frequency
        freq_cm1 = self.calculate_vibrational_frequency(opt_atoms)
        print(f"✓ Vibrational frequency: {freq_cm1:.2f} cm⁻¹")
        
        # Calculate thermochemistry
        geometry = properties.get('geometry', 'linear')
        spin = properties.get('spin', 0)
        symmetry = properties.get('symmetry', 2)
        
        enthalpy, entropy, gibbs = self.calculate_thermochemistry(
            opt_atoms, freq_cm1, geometry, spin, symmetry, temperature, pressure)
        
        print(f"✓ Enthalpy at {temperature:.2f} K: {enthalpy:.2f} kJ/mol")
        print(f"✓ Entropy at {temperature:.2f} K: {entropy:.2f} J/mol·K")
        print(f"✓ Gibbs free energy at {temperature:.2f} K: {gibbs:.2f} kJ/mol")
        
        # Store results
        results = {
            'molecule': molecule_name,
            'calculator': self.calculator_name,
            'equilibrium_distance': eq_dist,
            'dissociation_energy_eV': diss_eV,
            'dissociation_energy_kJmol': diss_kJmol,
            'vibrational_frequency_cm1': freq_cm1,
            'enthalpy_kJmol': enthalpy,
            'entropy_JmolK': entropy,
            'gibbs_kJmol': gibbs,
            'temperature': temperature,
            'pressure': pressure
        }
        
        return results, opt_atoms

def load_config(config_file='config.yaml'):
    """Load configuration from YAML file."""
    try:
        with open(config_file, 'r') as f:
            config = yaml.safe_load(f)
        print(f"Loaded configuration from {config_file}")
        return config
    except FileNotFoundError:
        print(f"Config file {config_file} not found. Using default settings.")
        return get_default_config()
    except Exception as e:
        print(f"Error loading config: {e}")
        return get_default_config()

def get_default_config():
    """Return default configuration."""
    return {
        'temperature': 298.15,
        'pressure': 101325,
        'fmax': 0.001,
        'max_steps': 100,
        'molecules': {
            'N2': {'symbols': ['N', 'N'], 'initial_distance': 1.2, 
                   'mass': 28.0134, 'spin': 0, 'symmetry': 2, 'geometry': 'linear'},
            'H2': {'symbols': ['H', 'H'], 'initial_distance': 0.8,
                   'mass': 2.01588, 'spin': 0, 'symmetry': 2, 'geometry': 'linear'},
            'F2': {'symbols': ['F', 'F'], 'initial_distance': 1.4,
                   'mass': 37.9968, 'spin': 0, 'symmetry': 2, 'geometry': 'linear'},
            'O2': {'symbols': ['O', 'O'], 'initial_distance': 1.3,
                   'mass': 31.9988, 'spin': 1, 'symmetry': 2, 'geometry': 'linear'}
        },
        'calculators': {
            'EMT': {'enabled': True},
            'MACE': {'enabled': False, 'model': 'MACE', 'device': 'cpu'}
        },
        'output': {
            'save_structures': True,
            'save_trajectories': True,
            'verbose': True,
            'output_dir': 'results'
        }
    }

def save_results(results, config):
    """Save results to files."""
    output_dir = config['output'].get('output_dir', 'results')
    os.makedirs(output_dir, exist_ok=True)
    
    # Save summary as CSV
    csv_file = os.path.join(output_dir, 'summary.csv')
    with open(csv_file, 'w') as f:
        # Write header
        f.write("Molecule,Calculator,d_eq(Å),D_e(eV),D_e(kJ/mol),freq(cm⁻¹),"
                "H(kJ/mol),S(J/mol·K),G(kJ/mol)\n")
        
        for calc_name, calc_results in results.items():
            for mol_name, mol_result in calc_results.items():
                if mol_result:
                    f.write(f"{mol_name},{calc_name},"
                           f"{mol_result['equilibrium_distance']:.4f},"
                           f"{mol_result['dissociation_energy_eV']:.4f},"
                           f"{mol_result['dissociation_energy_kJmol']:.2f},"
                           f"{mol_result['vibrational_frequency_cm1']:.2f},"
                           f"{mol_result['enthalpy_kJmol']:.2f},"
                           f"{mol_result['entropy_JmolK']:.4f},"
                           f"{mol_result['gibbs_kJmol']:.2f}\n")
    
    print(f"Results saved to {csv_file}")

def run_analysis(config):
    """Run the complete analysis based on configuration."""
    # Get enabled calculators
    enabled_calculators = []
    for calc_name, calc_config in config['calculators'].items():
        if calc_config.get('enabled', False):
            enabled_calculators.append(calc_name)
    
    if not enabled_calculators:
        print("No calculators enabled. Please enable at least one calculator in the config.")
        return {}
    
    print(f"\nEnabled calculators: {', '.join(enabled_calculators)}")
    
    all_results = {}
    molecules = config['molecules']
    
    for calc_name in enabled_calculators:
        print(f"\n{'#'*60}")
        print(f"Using {calc_name} calculator")
        print(f"{'#'*60}")
        
        # Get calculator parameters
        calc_params = config['calculators'].get(calc_name, {})
        analyzer = DiatomicAnalyzer(calc_name, calc_params)
        
        results = {}
        for mol_name, properties in molecules.items():
            result, atoms = analyzer.analyze_molecule(mol_name, properties, config)
            if result:
                results[mol_name] = result
                
                # Save optimized structure
                if config['output'].get('save_structures', True) and atoms:
                    output_dir = config['output'].get('output_dir', 'results')
                    os.makedirs(output_dir, exist_ok=True)
                    write(f"{output_dir}/{mol_name}_{calc_name}_opt.xyz", atoms)
        
        all_results[calc_name] = results
        
        # Print summary table
        if results:
            print(f"\n{'='*60}")
            print(f"Summary for {calc_name}")
            print(f"{'='*60}")
            print(f"{'Molecule':<8} {'d_eq (Å)':<10} {'D_e (eV)':<12} {'freq (cm⁻¹)':<12}")
            print("-"*45)
            for mol, res in results.items():
                print(f"{mol:<8} {res['equilibrium_distance']:<10.4f} "
                      f"{res['dissociation_energy_eV']:<12.4f} "
                      f"{res['vibrational_frequency_cm1']:<12.2f}")
        else:
            print(f"\nNo results obtained for {calc_name}")
    
    return all_results

def compare_with_reference(config):
    """Compare with reference values from NIST."""
    reference = {
        'N2': {'d_eq': 1.0977, 'D_e': 9.76, 'freq': 2358.6},
        'H2': {'d_eq': 0.7414, 'D_e': 4.52, 'freq': 4401.2},
        'F2': {'d_eq': 1.4119, 'D_e': 1.60, 'freq': 917.0},
        'O2': {'d_eq': 1.2075, 'D_e': 5.12, 'freq': 1580.2}
    }
    
    print("\n" + "="*80)
    print("Comparison with Reference Values (NIST)")
    print("="*80)
    print(f"{'Molecule':<8} {'Property':<15} {'Calculated':<12} {'Reference':<12} {'Error (%)':<10}")
    print("-"*80)
    
    # Try EMT first
    analyzer = DiatomicAnalyzer('EMT')
    
    for mol, ref in reference.items():
        if mol not in config['molecules']:
            continue
            
        props = config['molecules'][mol]
        
        # Check if EMT supports the elements
        supported = all(analyzer.supports_element(sym) for sym in props['symbols'])
        if not supported:
            print(f"{mol:<8} {'Skipped':<15} {'EMT does not support':<25}")
            print("-"*80)
            continue
        
        eq_dist, opt_atoms = analyzer.get_equilibrium_distance(
            props['symbols'], props['initial_distance'])
        
        if opt_atoms is None:
            print(f"{mol:<8} {'Failed':<15} {'Optimization failed':<25}")
            print("-"*80)
            continue
            
        diss_eV, _ = analyzer.calculate_dissociation_energy(opt_atoms)
        freq = analyzer.calculate_vibrational_frequency(opt_atoms)
        
        # Calculate errors
        dist_err = abs(eq_dist - ref['d_eq']) / ref['d_eq'] * 100
        diss_err = abs(diss_eV - ref['D_e']) / ref['D_e'] * 100 if ref['D_e'] > 0 else 0
        freq_err = abs(freq - ref['freq']) / ref['freq'] * 100 if ref['freq'] > 0 else 0
        
        print(f"{mol:<8} {'d_eq (Å)':<15} {eq_dist:<12.4f} {ref['d_eq']:<12.4f} {dist_err:<10.2f}")
        print(f"{mol:<8} {'D_e (eV)':<15} {diss_eV:<12.4f} {ref['D_e']:<12.4f} {diss_err:<10.2f}")
        print(f"{mol:<8} {'freq (cm⁻¹)':<15} {freq:<12.2f} {ref['freq']:<12.2f} {freq_err:<10.2f}")
        print("-"*80)

if __name__ == "__main__":
    # Load configuration
    config = load_config('config.yaml')
    
    # Print settings
    print("Diatomic Molecule Analysis with ASE")
    print("="*60)
    print(f"Temperature: {config['temperature']:.2f} K")
    print(f"Pressure: {config['pressure']:.0f} Pa")
    print(f"Convergence: fmax = {config['fmax']}")
    print("="*60)
    
    # Check MACE availability
    if MACE_AVAILABLE:
        print("✓ MACE is available")
    else:
        print("✗ MACE is not available (install with: pip install mace-torch)")
    
    # Run analysis
    all_results = run_analysis(config)
    
    # Save results
    if all_results:
        save_results(all_results, config)
    
    # Compare with reference values
    if config.get('compare_with_reference', True):
        compare_with_reference(config)
    
    print("\nAnalysis complete! Check the 'results' directory for output files.")
