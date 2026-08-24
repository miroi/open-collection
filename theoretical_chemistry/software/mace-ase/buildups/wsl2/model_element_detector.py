#!/usr/bin/env python3
"""
MACE Model Element Detector
Extracts elements directly from MACE model files
"""

import os
import sys
import torch
import warnings
from pathlib import Path
from datetime import datetime
import numpy as np

# ============================================================
# SUPPRESS WARNINGS
# ============================================================
warnings.filterwarnings('ignore')
os.environ['TORCH_FORCE_NO_WEIGHTS_ONLY_LOAD'] = '1'
os.environ['PYTHONWARNINGS'] = 'ignore'

import logging
logging.getLogger().setLevel(logging.ERROR)
logging.getLogger('mace').setLevel(logging.ERROR)

# ============================================================
# COLOR CODES
# ============================================================
class Colors:
    GREEN = '\033[0;32m'
    RED = '\033[0;31m'
    YELLOW = '\033[1;33m'
    BLUE = '\033[0;34m'
    CYAN = '\033[0;36m'
    MAGENTA = '\033[0;35m'
    NC = '\033[0m'
    BOLD = '\033[1m'

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
        except Exception as e:
            print(f"{Colors.YELLOW}⚠ Error reading config: {e}{Colors.NC}")
    return config

def get_element_symbol(atomic_number):
    """Convert atomic number to element symbol"""
    elements = {
        1: 'H', 2: 'He', 3: 'Li', 4: 'Be', 5: 'B', 6: 'C', 7: 'N', 8: 'O',
        9: 'F', 10: 'Ne', 11: 'Na', 12: 'Mg', 13: 'Al', 14: 'Si', 15: 'P',
        16: 'S', 17: 'Cl', 18: 'Ar', 19: 'K', 20: 'Ca', 21: 'Sc', 22: 'Ti',
        23: 'V', 24: 'Cr', 25: 'Mn', 26: 'Fe', 27: 'Co', 28: 'Ni', 29: 'Cu',
        30: 'Zn', 31: 'Ga', 32: 'Ge', 33: 'As', 34: 'Se', 35: 'Br', 36: 'Kr',
        37: 'Rb', 38: 'Sr', 39: 'Y', 40: 'Zr', 41: 'Nb', 42: 'Mo', 43: 'Tc',
        44: 'Ru', 45: 'Rh', 46: 'Pd', 47: 'Ag', 48: 'Cd', 49: 'In', 50: 'Sn',
        51: 'Sb', 52: 'Te', 53: 'I', 54: 'Xe', 55: 'Cs', 56: 'Ba', 57: 'La',
        58: 'Ce', 59: 'Pr', 60: 'Nd', 61: 'Pm', 62: 'Sm', 63: 'Eu', 64: 'Gd',
        65: 'Tb', 66: 'Dy', 67: 'Ho', 68: 'Er', 69: 'Tm', 70: 'Yb', 71: 'Lu',
        72: 'Hf', 73: 'Ta', 74: 'W', 75: 'Re', 76: 'Os', 77: 'Ir', 78: 'Pt',
        79: 'Au', 80: 'Hg', 81: 'Tl', 82: 'Pb', 83: 'Bi', 84: 'Po', 85: 'At',
        86: 'Rn', 87: 'Fr', 88: 'Ra', 89: 'Ac', 90: 'Th', 91: 'Pa', 92: 'U',
        93: 'Np', 94: 'Pu', 95: 'Am', 96: 'Cm', 97: 'Bk', 98: 'Cf', 99: 'Es',
        100: 'Fm', 101: 'Md', 102: 'No', 103: 'Lr'
    }
    return elements.get(int(atomic_number), f"Z{atomic_number}")

def extract_elements_from_mace_model(model_path):
    """
    Extract elements from MACE model by examining its internal structure
    """
    try:
        # Load the model
        model = torch.load(model_path, map_location='cpu', weights_only=False)
        
        elements_info = {
            'method': 'none',
            'elements': [],
            'atomic_numbers': [],
            'count': 0
        }
        
        # Method 1: Check if model has 'atomic_numbers' attribute
        if hasattr(model, 'atomic_numbers'):
            atomic_numbers = model.atomic_numbers
            if isinstance(atomic_numbers, (list, np.ndarray, torch.Tensor)):
                if isinstance(atomic_numbers, torch.Tensor):
                    atomic_numbers = atomic_numbers.tolist()
                elements = [get_element_symbol(z) for z in atomic_numbers]
                elements_info = {
                    'method': 'model.atomic_numbers',
                    'elements': sorted(set(elements)),
                    'atomic_numbers': sorted(set(atomic_numbers)),
                    'count': len(set(elements))
                }
                return elements_info
        
        # Method 2: Check if model has 'atomic_numbers' as attribute of a submodule
        if hasattr(model, 'node_encoder'):
            node_encoder = model.node_encoder
            if hasattr(node_encoder, 'atomic_numbers'):
                atomic_numbers = node_encoder.atomic_numbers
                if isinstance(atomic_numbers, (list, np.ndarray, torch.Tensor)):
                    if isinstance(atomic_numbers, torch.Tensor):
                        atomic_numbers = atomic_numbers.tolist()
                    elements = [get_element_symbol(z) for z in atomic_numbers]
                    elements_info = {
                        'method': 'node_encoder.atomic_numbers',
                        'elements': sorted(set(elements)),
                        'atomic_numbers': sorted(set(atomic_numbers)),
                        'count': len(set(elements))
                    }
                    return elements_info
        
        # Method 3: Search through all attributes for atomic numbers
        for attr_name in dir(model):
            if 'atomic' in attr_name.lower() or 'z' in attr_name.lower():
                try:
                    attr = getattr(model, attr_name)
                    if isinstance(attr, (list, np.ndarray, torch.Tensor)):
                        if len(attr) > 0 and len(attr) <= 118:  # Reasonable number of elements
                            if isinstance(attr, torch.Tensor):
                                attr = attr.tolist()
                            # Check if it contains integers that look like atomic numbers
                            if all(isinstance(x, (int, float)) and 1 <= x <= 118 for x in attr):
                                elements = [get_element_symbol(z) for z in attr]
                                elements_info = {
                                    'method': f'model.{attr_name}',
                                    'elements': sorted(set(elements)),
                                    'atomic_numbers': sorted(set(attr)),
                                    'count': len(set(elements))
                                }
                                return elements_info
                except:
                    continue
        
        # Method 4: Check state_dict for atomic numbers
        if hasattr(model, 'state_dict'):
            state_dict = model.state_dict()
            for key in state_dict.keys():
                if 'atomic' in key.lower() or 'z' in key.lower():
                    tensor = state_dict[key]
                    if isinstance(tensor, torch.Tensor) and len(tensor.shape) == 1:
                        atomic_numbers = tensor.tolist()
                        if all(isinstance(x, (int, float)) and 1 <= x <= 118 for x in atomic_numbers):
                            elements = [get_element_symbol(z) for z in atomic_numbers]
                            elements_info = {
                                'method': f'state_dict.{key}',
                                'elements': sorted(set(elements)),
                                'atomic_numbers': sorted(set(atomic_numbers)),
                                'count': len(set(elements))
                            }
                            return elements_info
        
        # Method 5: Check if model has 'species' attribute
        if hasattr(model, 'species'):
            species = model.species
            if isinstance(species, (list, np.ndarray)):
                if isinstance(species, np.ndarray):
                    species = species.tolist()
                if all(isinstance(x, str) for x in species):
                    elements_info = {
                        'method': 'model.species',
                        'elements': sorted(set(species)),
                        'count': len(set(species))
                    }
                    return elements_info
        
        # Method 6: Check if model has 'elements' attribute
        if hasattr(model, 'elements'):
            elements = model.elements
            if isinstance(elements, (list, np.ndarray)):
                if isinstance(elements, np.ndarray):
                    elements = elements.tolist()
                if all(isinstance(x, str) for x in elements):
                    elements_info = {
                        'method': 'model.elements',
                        'elements': sorted(set(elements)),
                        'count': len(set(elements))
                    }
                    return elements_info
        
        # Method 7: Try to find atomic numbers in the model's config
        if hasattr(model, 'config'):
            config = model.config
            if isinstance(config, dict):
                for key in ['atomic_numbers', 'z', 'atomic_numbers_list']:
                    if key in config:
                        atomic_numbers = config[key]
                        if isinstance(atomic_numbers, (list, np.ndarray, torch.Tensor)):
                            if isinstance(atomic_numbers, torch.Tensor):
                                atomic_numbers = atomic_numbers.tolist()
                            if all(isinstance(x, (int, float)) and 1 <= x <= 118 for x in atomic_numbers):
                                elements = [get_element_symbol(z) for z in atomic_numbers]
                                elements_info = {
                                    'method': f'config.{key}',
                                    'elements': sorted(set(elements)),
                                    'atomic_numbers': sorted(set(atomic_numbers)),
                                    'count': len(set(elements))
                                }
                                return elements_info
        
        # Method 8: Check if the model has a 'get_atomic_numbers' method
        if hasattr(model, 'get_atomic_numbers'):
            try:
                atomic_numbers = model.get_atomic_numbers()
                if isinstance(atomic_numbers, (list, np.ndarray, torch.Tensor)):
                    if isinstance(atomic_numbers, torch.Tensor):
                        atomic_numbers = atomic_numbers.tolist()
                    elements = [get_element_symbol(z) for z in atomic_numbers]
                    elements_info = {
                        'method': 'model.get_atomic_numbers()',
                        'elements': sorted(set(elements)),
                        'atomic_numbers': sorted(set(atomic_numbers)),
                        'count': len(set(elements))
                    }
                    return elements_info
            except:
                pass
        
        return elements_info
        
    except Exception as e:
        return {
            'method': 'error',
            'elements': [],
            'count': 0,
            'error': str(e)
        }

def print_model_structure(model):
    """Print useful information about the model structure"""
    print(f"    Type: {type(model).__name__}")
    
    # Show attributes
    attrs = [attr for attr in dir(model) if not attr.startswith('_')]
    important_attrs = ['atomic_numbers', 'elements', 'species', 'node_encoder', 
                       'config', 'training', 'interaction', 'readout']
    
    found_attrs = []
    for attr in important_attrs:
        if hasattr(model, attr):
            found_attrs.append(attr)
    
    if found_attrs:
        print(f"    Found attributes: {', '.join(found_attrs)}")
        
        # Show values of important attributes
        for attr in found_attrs:
            try:
                value = getattr(model, attr)
                if isinstance(value, (list, np.ndarray, torch.Tensor)):
                    if isinstance(value, torch.Tensor):
                        value_shape = value.shape
                        print(f"    {attr}: Tensor shape {value_shape}")
                    else:
                        print(f"    {attr}: {type(value).__name__} length {len(value)}")
            except:
                pass

def main():
    """Main entry point"""
    print(f"\n{Colors.BOLD}{'='*80}{Colors.NC}")
    print(f"{Colors.BOLD}   MACE Model Element Detector   {Colors.NC}")
    print(f"{Colors.BOLD}{'='*80}{Colors.NC}")
    
    # Read configuration
    config = read_config('mace_config.txt')
    models_path = Path(config['models_path']).expanduser()
    
    print(f"\n{Colors.BLUE}Models directory:{Colors.NC} {models_path}")
    
    # Get all models
    models = list(models_path.glob('*model'))
    if not models:
        print(f"{Colors.RED}✗ No models found in {models_path}{Colors.NC}")
        return
    
    print(f"{Colors.BLUE}Found {len(models)} models{Colors.NC}\n")
    
    # Analyze each model
    all_elements = set()
    element_summary = {}
    
    for i, model_path in enumerate(models, 1):
        print(f"\n{Colors.CYAN}{'─'*80}{Colors.NC}")
        print(f"{Colors.BOLD}[{i}/{len(models)}] Analyzing: {model_path.name}{Colors.NC}")
        print(f"{Colors.CYAN}{'─'*80}{Colors.NC}")
        
        # Get file info
        size_mb = model_path.stat().st_size / (1024 * 1024)
        modified = datetime.fromtimestamp(model_path.stat().st_mtime).strftime('%Y-%m-%d %H:%M:%S')
        print(f"  {Colors.BLUE}Size:{Colors.NC} {size_mb:.1f} MB")
        print(f"  {Colors.BLUE}Modified:{Colors.NC} {modified}")
        
        # Load and analyze the model
        try:
            model = torch.load(model_path, map_location='cpu', weights_only=False)
            
            # Print model structure
            print(f"  {Colors.BLUE}Model type:{Colors.NC} {type(model).__name__}")
            
            # Extract elements
            elements_info = extract_elements_from_mace_model(model_path)
            
            if elements_info['method'] != 'none' and elements_info['count'] > 0:
                print(f"  {Colors.GREEN}✓ Found {elements_info['count']} elements:{Colors.NC}")
                print(f"    Method: {elements_info['method']}")
                
                # Print elements in rows
                elements = elements_info['elements']
                for j in range(0, len(elements), 10):
                    row = elements[j:j+10]
                    print(f"    {', '.join(row)}")
                
                if 'atomic_numbers' in elements_info:
                    print(f"  {Colors.BLUE}Atomic numbers:{Colors.NC} {elements_info['atomic_numbers']}")
                
                all_elements.update(elements)
                element_summary[model_path.name] = elements
            else:
                print(f"  {Colors.YELLOW}⚠ No elements found with standard methods{Colors.NC}")
                print(f"  {Colors.YELLOW}  Showing model structure for debugging:{Colors.NC}")
                print_model_structure(model)
                
                # Try to find atomic numbers in the model's submodules
                print(f"\n  {Colors.BLUE}Searching submodules for element information...{Colors.NC}")
                found_in_submodule = False
                
                for attr_name in dir(model):
                    if attr_name.startswith('_'):
                        continue
                    try:
                        attr = getattr(model, attr_name)
                        if hasattr(attr, 'atomic_numbers'):
                            atomic_numbers = attr.atomic_numbers
                            if isinstance(atomic_numbers, (list, np.ndarray, torch.Tensor)):
                                if isinstance(atomic_numbers, torch.Tensor):
                                    atomic_numbers = atomic_numbers.tolist()
                                elements = [get_element_symbol(z) for z in atomic_numbers]
                                print(f"    Found in {attr_name}.atomic_numbers: {elements}")
                                all_elements.update(elements)
                                element_summary[model_path.name] = elements
                                found_in_submodule = True
                    except:
                        continue
                
                if not found_in_submodule:
                    print(f"    {Colors.YELLOW}No element information found in submodules{Colors.NC}")
                    
        except Exception as e:
            print(f"  {Colors.RED}✗ Error loading model: {e}{Colors.NC}")
    
    # Summary
    print(f"\n{Colors.BOLD}{'='*80}{Colors.NC}")
    print(f"{Colors.BOLD}   SUMMARY   {Colors.NC}")
    print(f"{Colors.BOLD}{'='*80}{Colors.NC}")
    
    if all_elements:
        print(f"\n{Colors.GREEN}Total unique elements found across all models: {len(all_elements)}{Colors.NC}")
        print(f"{Colors.BLUE}All elements:{Colors.NC}")
        sorted_elements = sorted(list(all_elements))
        for i in range(0, len(sorted_elements), 10):
            row = sorted_elements[i:i+10]
            print(f"  {', '.join(row)}")
    else:
        print(f"\n{Colors.YELLOW}⚠ No elements could be detected from any model{Colors.NC}")
        print(f"{Colors.YELLOW}  This might be because the models store element information differently.{Colors.NC}")
        print(f"{Colors.YELLOW}  Try checking the model documentation for element support.{Colors.NC}")
    
    # Print element summary per model
    print(f"\n{Colors.BLUE}Elements found per model:{Colors.NC}")
    for model_name, elements in element_summary.items():
        if elements:
            print(f"  {Colors.GREEN}{model_name}:{Colors.NC} {', '.join(elements)}")
        else:
            print(f"  {Colors.YELLOW}{model_name}:{Colors.NC} No elements detected")
    
    print(f"\n{Colors.CYAN}Note:{Colors.NC}")
    print(f"  - This script extracts element information from the model file directly.")
    print(f"  - Elements are converted from atomic numbers to element symbols.")
    print(f"  - If no elements are shown, the model may need to be loaded differently.")
    print(f"  - For MACE models, try: model.node_encoder.atomic_numbers")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n{Colors.YELLOW}Analysis interrupted by user{Colors.NC}")
        sys.exit(130)
    except Exception as e:
        print(f"\n{Colors.RED}Fatal error: {e}{Colors.NC}")
        sys.exit(1)
