#!/usr/bin/env python3
"""
MACE Model Analyzer
Reads and analyzes all MACE models in the models directory
"""

import os
import sys
import time
import json
import warnings
from pathlib import Path
from datetime import datetime
import numpy as np

# ============================================================
# SUPPRESS ALL WARNINGS - MUST BE BEFORE ANY OTHER IMPORTS
# ============================================================
# Suppress Python warnings
warnings.filterwarnings('ignore')

# Suppress all logging
import logging
logging.getLogger().setLevel(logging.ERROR)
logging.getLogger('mace').setLevel(logging.ERROR)
logging.getLogger('ase').setLevel(logging.ERROR)
logging.getLogger('torch').setLevel(logging.ERROR)
logging.getLogger('e3nn').setLevel(logging.ERROR)

# Suppress specific environment warnings
os.environ['TORCH_FORCE_NO_WEIGHTS_ONLY_LOAD'] = '1'
os.environ['PYTHONWARNINGS'] = 'ignore'
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'

# Suppress all root logger handlers
for handler in logging.root.handlers[:]:
    logging.root.removeHandler(handler)

# Disable warnings from specific modules
import sys
if not sys.warnoptions:
    import warnings
    warnings.simplefilter("ignore")

# ============================================================
# IMPORT MODULES AFTER SUPPRESSING WARNINGS
# ============================================================
from mace.calculators import MACECalculator
from ase.build import molecule
from ase import Atoms
from ase.data import chemical_symbols

# Color codes for terminal output
class Colors:
    GREEN = '\033[0;32m'
    RED = '\033[0;31m'
    YELLOW = '\033[1;33m'
    BLUE = '\033[0;34m'
    CYAN = '\033[0;36m'
    MAGENTA = '\033[0;35m'
    NC = '\033[0m'
    BOLD = '\033[1m'

# ============================================================
# DEFINE MOLECULES TO TEST
# ============================================================
MOLECULES_TO_TEST = [
    'H2O',      # Water - H, O
    'CH4',      # Methane - C, H
    'NH3',      # Ammonia - N, H
    'CO2',      # Carbon dioxide - C, O
    'CH3CH2OH', # Ethanol - C, H, O
    'C6H6',     # Benzene - C, H
]

# Additional molecules to test for element coverage
ADDITIONAL_MOLECULES = [
    'NaCl',     # Sodium chloride - Na, Cl
    'MgO',      # Magnesium oxide - Mg, O
    'Fe',       # Iron - Fe
    'Cu',       # Copper - Cu
    'Au',       # Gold - Au
    'Pt',       # Platinum - Pt
    'Si',       # Silicon - Si
    'Al',       # Aluminum - Al
]

# Combine molecules
ALL_MOLECULES = MOLECULES_TO_TEST + ADDITIONAL_MOLECULES

def read_config(config_file='mace_config.txt'):
    """Read configuration from file"""
    config = {
        'models_path': '~/.cache/mace',
        'default_device': 'cpu'
    }
    
    if Path(config_file).exists():
        try:
            with open(config_file, 'r') as f:
                for line in f:
                    line = line.strip()
                    if not line or line.startswith('#'):
                        continue
                    if '=' in line:
                        key, value = line.split('=', 1)
                        key = key.strip()
                        value = value.strip()
                        if key == 'MACE_MODELS_PATH':
                            config['models_path'] = value
                        elif key == 'DEFAULT_DEVICE':
                            config['default_device'] = value.lower()
            # Silent mode - don't print config loading
        except Exception:
            pass
    return config

def get_model_info(model_path):
    """Get information about a model file"""
    info = {
        'name': model_path.name,
        'path': str(model_path),
        'size_mb': model_path.stat().st_size / (1024 * 1024),
        'modified': datetime.fromtimestamp(model_path.stat().st_mtime).strftime('%Y-%m-%d %H:%M:%S'),
        'extension': model_path.suffix,
        'elements': [],
        'element_count': 0,
    }
    
    # Try to parse model name for architecture info
    name_lower = model_path.name.lower()
    if '128' in name_lower:
        info['architecture'] = '128'
    elif '256' in name_lower:
        info['architecture'] = '256'
    else:
        info['architecture'] = 'unknown'
    
    if 'l0' in name_lower:
        info['layers'] = 'L0'
    elif 'l1' in name_lower:
        info['layers'] = 'L1'
    elif 'l2' in name_lower:
        info['layers'] = 'L2'
    else:
        info['layers'] = 'unknown'
    
    if 'mp' in name_lower or 'medium' in name_lower:
        info['type'] = 'MPA (Materials Project)'
    elif 'energy' in name_lower:
        info['type'] = 'Energy trained'
    elif 'force' in name_lower:
        info['type'] = 'Force trained'
    else:
        info['type'] = 'General'
    
    return info

def create_silent_calculator(model_path, device='cpu'):
    """Create a calculator with all warnings suppressed"""
    # Temporarily redirect stderr
    import contextlib
    import io
    
    with contextlib.redirect_stderr(io.StringIO()):
        with warnings.catch_warnings():
            warnings.simplefilter("ignore")
            # Suppress all logging during calculator creation
            logging.getLogger().setLevel(logging.ERROR)
            try:
                calc = MACECalculator(model_path=str(model_path), device=device)
                return calc
            except Exception:
                return None

def detect_elements_in_model(model_path, test_molecules=ALL_MOLECULES, device='cpu'):
    """Detect which elements a model can handle by testing molecules"""
    elements = set()
    element_count = {}
    tested_elements = {}
    
    calc = create_silent_calculator(model_path, device)
    if calc is None:
        return {'error': 'Failed to load model'}
    
    for mol_name in test_molecules:
        try:
            atoms = molecule(mol_name)
            atoms.calc = calc
            energy = atoms.get_potential_energy()
            
            # Get elements in this molecule
            mol_elements = list(set(atoms.get_chemical_symbols()))
            for elem in mol_elements:
                elements.add(elem)
                element_count[elem] = element_count.get(elem, 0) + 1
                tested_elements[elem] = tested_elements.get(elem, []) + [mol_name]
                
        except Exception:
            # This element might not be supported
            pass
    
    return {
        'elements': sorted(list(elements)),
        'element_count': len(elements),
        'element_frequency': element_count,
        'tested_elements': tested_elements,
        'total_tested': len(test_molecules)
    }

def test_model_on_molecules(model_path, molecules, device='cpu', verbose=True):
    """Test a model on a list of molecules"""
    results = {
        'model': model_path.name,
        'device': device,
        'molecules': [],
        'total_time': 0,
        'success': 0,
        'failed': 0
    }
    
    calc = create_silent_calculator(model_path, device)
    if calc is None:
        if verbose:
            print(f"  {Colors.RED}✗ Failed to load model{Colors.NC}")
        results['error'] = 'Failed to load model'
        return results
    
    if verbose:
        print(f"  {Colors.GREEN}✓ Model loaded successfully{Colors.NC}")
    
    for mol_name in molecules:
        try:
            atoms = molecule(mol_name)
            atoms.calc = calc
            
            start = time.time()
            energy = atoms.get_potential_energy()
            forces = atoms.get_forces()
            elapsed = time.time() - start
            
            result = {
                'molecule': mol_name,
                'atoms': len(atoms),
                'elements': list(set(atoms.get_chemical_symbols())),
                'energy_ev': energy,
                'energy_kjmol': energy * 96.485,
                'energy_kcalmol': energy * 23.0605,
                'time_s': elapsed,
                'forces': forces.tolist(),
                'force_magnitudes': [np.linalg.norm(f) for f in forces],
                'success': True
            }
            results['molecules'].append(result)
            results['success'] += 1
            results['total_time'] += elapsed
            
            if verbose:
                elements_str = ', '.join(result['elements'])
                print(f"    {mol_name:>10}: {energy:10.6f} eV ({elapsed:>5.3f}s) [{elements_str}]")
                
        except Exception as e:
            if verbose:
                print(f"    {mol_name:>10}: {Colors.RED}Error: {e}{Colors.NC}")
            result = {
                'molecule': mol_name,
                'success': False,
                'error': str(e)
            }
            results['molecules'].append(result)
            results['failed'] += 1
    
    return results

def analyze_models(models_path, device='cpu'):
    """Analyze all models in the directory"""
    
    model_dir = Path(models_path).expanduser()
    
    print(f"\n{Colors.BOLD}{'='*80}{Colors.NC}")
    print(f"{Colors.BOLD}   MACE Model Analyzer   {Colors.NC}")
    print(f"{Colors.BOLD}{'='*80}{Colors.NC}")
    print(f"\n{Colors.BLUE}Models directory:{Colors.NC} {model_dir}")
    print(f"{Colors.BLUE}Device:{Colors.NC} {device}")
    print(f"{Colors.BLUE}Test molecules:{Colors.NC} {', '.join(MOLECULES_TO_TEST)}\n")
    
    # Get all models
    models = list(model_dir.glob('*model'))
    if not models:
        print(f"{Colors.RED}✗ No models found in {model_dir}{Colors.NC}")
        return
    
    print(f"{Colors.BOLD}Found {len(models)} models{Colors.NC}\n")
    print("="*80)
    
    # Analyze each model
    all_results = []
    model_info_list = []
    all_elements = set()
    
    for i, model_path in enumerate(models, 1):
        print(f"\n{Colors.CYAN}{'─'*80}{Colors.NC}")
        print(f"{Colors.BOLD}[{i}/{len(models)}] Analyzing: {model_path.name}{Colors.NC}")
        print(f"{Colors.CYAN}{'─'*80}{Colors.NC}")
        
        # Get model info
        info = get_model_info(model_path)
        
        # Detect elements
        element_info = detect_elements_in_model(model_path, ALL_MOLECULES, device)
        if 'error' not in element_info:
            info['elements'] = element_info['elements']
            info['element_count'] = element_info['element_count']
            info['element_frequency'] = element_info['element_frequency']
            all_elements.update(info['elements'])
        
        model_info_list.append(info)
        
        print(f"  {Colors.BLUE}Size:{Colors.NC} {info['size_mb']:.1f} MB")
        print(f"  {Colors.BLUE}Modified:{Colors.NC} {info['modified']}")
        print(f"  {Colors.BLUE}Architecture:{Colors.NC} {info['architecture']}")
        print(f"  {Colors.BLUE}Layers:{Colors.NC} {info['layers']}")
        print(f"  {Colors.BLUE}Type:{Colors.NC} {info['type']}")
        print(f"  {Colors.BLUE}Elements supported:{Colors.NC} {', '.join(info['elements']) if info['elements'] else 'Unknown'}")
        print(f"  {Colors.BLUE}Element count:{Colors.NC} {info['element_count']}")
        print(f"  {Colors.BLUE}Testing on {len(MOLECULES_TO_TEST)} molecules:{Colors.NC}")
        
        # Test model on main molecules
        results = test_model_on_molecules(model_path, MOLECULES_TO_TEST, device, verbose=True)
        results['info'] = info
        all_results.append(results)
        
        # Summary for this model
        if results['success'] > 0:
            energies = [r['energy_ev'] for r in results['molecules'] if r.get('success')]
            if energies:
                print(f"\n  {Colors.GREEN}✓ Model summary:{Colors.NC}")
                print(f"    Success: {results['success']}/{len(MOLECULES_TO_TEST)} molecules")
                print(f"    Total time: {results['total_time']:.3f}s")
                print(f"    Energy range: {min(energies):.6f} to {max(energies):.6f} eV")
                print(f"    Avg time per molecule: {results['total_time']/results['success']:.3f}s")
                print(f"    Elements detected: {', '.join(info['elements'])}")
    
    # Generate comprehensive report
    generate_report(all_results, model_info_list, all_elements)

def generate_report(all_results, model_info_list, all_elements):
    """Generate a comprehensive analysis report"""
    
    print(f"\n{Colors.BOLD}{'='*80}{Colors.NC}")
    print(f"{Colors.BOLD}   ANALYSIS REPORT   {Colors.NC}")
    print(f"{Colors.BOLD}{'='*80}{Colors.NC}")
    
    # 1. Model overview with elements
    print(f"\n{Colors.CYAN}1. Model Overview:{Colors.NC}")
    print(f"{'Model Name':<30} {'Size':>8} {'Type':>18} {'Elements':>15} {'Arch':>8} {'Layers':>8}")
    print("-" * 95)
    
    for info in model_info_list:
        elem_str = ', '.join(info.get('elements', ['unknown'])[:5])
        if len(info.get('elements', [])) > 5:
            elem_str += f" (+{len(info['elements'])-5})"
        print(f"{info['name'][:28]:<30} {info['size_mb']:>7.1f}MB {info['type'][:18]:>18} {elem_str:>15} {info['architecture']:>8} {info['layers']:>8}")
    
    # 2. Element coverage
    print(f"\n{Colors.CYAN}2. Element Coverage Summary:{Colors.NC}")
    print(f"{'Element':<10} {'Frequency':>12} {'Tested in':>15} {'Models supporting':>20}")
    print("-" * 60)
    
    # Count element frequencies across all models
    element_model_count = {}
    for info in model_info_list:
        for elem in info.get('elements', []):
            element_model_count[elem] = element_model_count.get(elem, 0) + 1
    
    # Get all elements from all models
    all_elements_list = sorted(list(all_elements))
    
    for elem in all_elements_list:
        count = element_model_count.get(elem, 0)
        # Find which molecules contain this element
        molecules_with_elem = []
        for mol in MOLECULES_TO_TEST:
            try:
                atoms = molecule(mol)
                if elem in atoms.get_chemical_symbols():
                    molecules_with_elem.append(mol)
            except:
                pass
        mol_str = ', '.join(molecules_with_elem[:3])
        if len(molecules_with_elem) > 3:
            mol_str += f" (+{len(molecules_with_elem)-3})"
        print(f"{elem:<10} {count:>12} {mol_str:>15} {count:>20}/{len(model_info_list)}")
    
    # 3. Performance comparison
    print(f"\n{Colors.CYAN}3. Performance Comparison:{Colors.NC}")
    print(f"{'Model':<30} {'Success':>10} {'Total Time (s)':>15} {'Avg Time (s)':>15} {'Elements':>15}")
    print("-" * 90)
    
    for result in all_results:
        if result['success'] > 0:
            avg_time = result['total_time'] / result['success']
            elem_count = len(result['info'].get('elements', []))
            print(f"{result['model'][:28]:<30} {result['success']:>10}/{len(MOLECULES_TO_TEST)} {result['total_time']:>15.3f} {avg_time:>15.3f} {elem_count:>15}")
    
    # 4. Energy comparison for each molecule
    print(f"\n{Colors.CYAN}4. Energy Comparison (eV):{Colors.NC}")
    
    # Print header - truncate long model names
    header = f"{'Molecule':>12}"
    for result in all_results:
        short_name = result['model'][:20] + '...' if len(result['model']) > 22 else result['model']
        header += f" {short_name:>22}"
    print(header)
    print("-" * (12 + 22 * len(all_results)))
    
    # Print energies for each molecule
    for mol_name in MOLECULES_TO_TEST:
        line = f"{mol_name:>12}"
        for result in all_results:
            energy = None
            for mol_result in result['molecules']:
                if mol_result.get('molecule') == mol_name and mol_result.get('success'):
                    energy = mol_result['energy_ev']
                    break
            if energy is not None:
                line += f" {energy:>22.6f}"
            else:
                line += f" {'N/A':>22}"
        print(line)
    
    # 5. Fastest model
    print(f"\n{Colors.CYAN}5. Performance Summary:{Colors.NC}")
    
    if all_results:
        # Fastest model (lowest avg time)
        valid_results = [r for r in all_results if r['success'] > 0]
        if valid_results:
            fastest = min(valid_results, key=lambda x: x['total_time'] / x['success'])
            print(f"  {Colors.GREEN}Fastest model:{Colors.NC} {fastest['model']} ({fastest['total_time']/fastest['success']:.3f}s per molecule)")
            
            # Most element coverage
            most_elements = max(model_info_list, key=lambda x: len(x.get('elements', [])))
            print(f"  {Colors.GREEN}Most elements supported:{Colors.NC} {most_elements['name']} ({len(most_elements.get('elements', []))} elements)")
            
            # Smallest model
            smallest = min(model_info_list, key=lambda x: x['size_mb'])
            print(f"  {Colors.GREEN}Smallest model:{Colors.NC} {smallest['name']} ({smallest['size_mb']:.1f} MB)")
            
            # Largest model
            largest = max(model_info_list, key=lambda x: x['size_mb'])
            print(f"  {Colors.GREEN}Largest model:{Colors.NC} {largest['name']} ({largest['size_mb']:.1f} MB)")
    
    # 6. Recommendations
    print(f"\n{Colors.CYAN}6. Recommendations:{Colors.NC}")
    
    if valid_results:
        # Fastest model for quick calculations
        fastest = min(valid_results, key=lambda x: x['total_time'] / x['success'])
        print(f"  • For quick calculations: {fastest['model']}")
        
        # Model with most elements
        if model_info_list:
            most_elements = max(model_info_list, key=lambda x: len(x.get('elements', [])))
            print(f"  • For broad element coverage: {most_elements['name']} ({len(most_elements.get('elements', []))} elements)")
        
        # Largest model for accuracy (usually)
        largest_model = max(model_info_list, key=lambda x: x['size_mb'])
        print(f"  • For maximum accuracy: {largest_model['name']} (largest model)")
    
    print(f"\n{Colors.CYAN}7. Detailed Results:{Colors.NC}")
    print(f"  • Run 'python mace_calc.py --list' to see all models")
    print(f"  • Run 'python mace_calc.py [molecule] [model]' for specific calculations")
    print(f"  • Element coverage detected by testing molecules")
    
    print(f"\n{Colors.GREEN}{'='*80}{Colors.NC}")
    print(f"{Colors.GREEN}✓ Analysis complete!{Colors.NC}")
    print(f"{Colors.GREEN}{'='*80}{Colors.NC}")

def main():
    """Main entry point"""
    import argparse
    
    parser = argparse.ArgumentParser(description='Analyze MACE models')
    parser.add_argument('--config', type=str, default='mace_config.txt',
                       help='Configuration file path')
    parser.add_argument('--device', type=str, choices=['cpu', 'cuda'],
                       help='Device to use (overrides config)')
    parser.add_argument('--export', action='store_true',
                       help='Export results to JSON')
    parser.add_argument('--silent', action='store_true',
                       help='Run in silent mode (no output)')
    
    args = parser.parse_args()
    
    # Read configuration
    config = read_config(args.config)
    
    models_path = config['models_path']
    device = args.device if args.device else config['default_device']
    
    # Run analysis
    analyze_models(models_path, device)
    
    # Show help
    print(f"\n{Colors.CYAN}Usage examples:{Colors.NC}")
    print("  python model_analyzer.py")
    print("  python model_analyzer.py --device cuda")
    print("  python model_analyzer.py --export")
    print("  python model_analyzer.py --silent")
    print("  python model_analyzer.py --config my_config.txt")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n{Colors.YELLOW}Analysis interrupted by user{Colors.NC}")
        sys.exit(130)
    except Exception as e:
        print(f"\n{Colors.RED}Fatal error: {e}{Colors.NC}")
        sys.exit(1)
