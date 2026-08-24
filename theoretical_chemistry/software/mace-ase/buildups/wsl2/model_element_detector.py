#!/usr/bin/env python3
"""
MACE Model Element Detector
Reads model file and extracts element information directly from the model
"""

import os
import sys
import json
import pickle
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

def get_model_info(model_path):
    """Get file information about the model"""
    info = {
        'name': model_path.name,
        'path': str(model_path),
        'size_mb': model_path.stat().st_size / (1024 * 1024),
        'modified': datetime.fromtimestamp(model_path.stat().st_mtime).strftime('%Y-%m-%d %H:%M:%S'),
        'extension': model_path.suffix,
    }
    return info

def extract_elements_from_model(model_path):
    """
    Extract element information directly from the MACE model file
    """
    elements = []
    element_mapping = {}
    model_data = {}
    
    try:
        # Load the model
        model_data = torch.load(model_path, map_location='cpu', weights_only=False)
        
        # Store the full structure for analysis
        if isinstance(model_data, dict):
            model_data = model_data
        elif hasattr(model_data, '__dict__'):
            model_data = model_data.__dict__
        
        # Try different ways to extract elements
        
        # Method 1: Look for 'elements' key
        if 'elements' in model_data:
            elements = model_data['elements']
            if isinstance(elements, list):
                return {
                    'method': 'elements_key',
                    'elements': sorted(elements),
                    'count': len(elements),
                    'model_data': model_data
                }
        
        # Method 2: Look for 'node_attrs' or atomic numbers
        if 'node_attrs' in model_data:
            # Try to get atomic numbers from node_attrs
            node_attrs = model_data['node_attrs']
            if hasattr(node_attrs, 'shape'):
                # This might contain atomic numbers
                pass
        
        # Method 3: Look for 'atomic_numbers' or 'z'
        if 'atomic_numbers' in model_data:
            atomic_numbers = model_data['atomic_numbers']
            if isinstance(atomic_numbers, (list, np.ndarray)):
                # Convert atomic numbers to element symbols
                from ase.data import chemical_symbols
                elements = [chemical_symbols[int(z)] for z in atomic_numbers]
                return {
                    'method': 'atomic_numbers',
                    'elements': sorted(set(elements)),
                    'count': len(set(elements)),
                    'model_data': model_data
                }
        
        # Method 4: Look for 'z' (common in some models)
        if 'z' in model_data:
            z_values = model_data['z']
            if isinstance(z_values, (list, np.ndarray)):
                from ase.data import chemical_symbols
                elements = [chemical_symbols[int(z)] for z in z_values]
                return {
                    'method': 'z_values',
                    'elements': sorted(set(elements)),
                    'count': len(set(elements)),
                    'model_data': model_data
                }
        
        # Method 5: Look for 'species' or 'types'
        if 'species' in model_data:
            species = model_data['species']
            if isinstance(species, list):
                return {
                    'method': 'species',
                    'elements': sorted(species),
                    'count': len(species),
                    'model_data': model_data
                }
        
        # Method 6: Search through all keys for element-related data
        element_keys = ['elements', 'element_types', 'atomic_types', 'atom_types', 
                       'species_set', 'unique_species', 'z_list']
        
        for key in element_keys:
            if key in model_data:
                data = model_data[key]
                if isinstance(data, (list, np.ndarray)):
                    if len(data) > 0:
                        # Check if it's strings or numbers
                        if isinstance(data[0], str):
                            elements = sorted(set(data))
                            return {
                                'method': key,
                                'elements': elements,
                                'count': len(elements),
                                'model_data': model_data
                            }
                        elif isinstance(data[0], (int, float, np.integer, np.floating)):
                            from ase.data import chemical_symbols
                            elements = [chemical_symbols[int(d)] for d in data]
                            return {
                                'method': key,
                                'elements': sorted(set(elements)),
                                'count': len(set(elements)),
                                'model_data': model_data
                            }
        
        # Method 7: Check if model has atomic numbers in the config
        if 'config' in model_data:
            config = model_data['config']
            if isinstance(config, dict):
                if 'atomic_numbers' in config:
                    from ase.data import chemical_symbols
                    elements = [chemical_symbols[int(z)] for z in config['atomic_numbers']]
                    return {
                        'method': 'config_atomic_numbers',
                        'elements': sorted(set(elements)),
                        'count': len(set(elements)),
                        'model_data': model_data
                    }
                elif 'elements' in config:
                    return {
                        'method': 'config_elements',
                        'elements': sorted(config['elements']),
                        'count': len(config['elements']),
                        'model_data': model_data
                    }
        
        # Method 8: Try to inspect the model's internal structure
        # Look for anything that might contain element information
        for key in model_data.keys():
            if isinstance(model_data[key], dict):
                sub_data = model_data[key]
                for sub_key in element_keys:
                    if sub_key in sub_data:
                        data = sub_data[sub_key]
                        if isinstance(data, (list, np.ndarray)) and len(data) > 0:
                            if isinstance(data[0], str):
                                elements = sorted(set(data))
                                return {
                                    'method': f'{key}.{sub_key}',
                                    'elements': elements,
                                    'count': len(elements),
                                    'model_data': model_data
                                }
        
        # Method 9: Search for any list of strings that look like elements
        for key, value in model_data.items():
            if isinstance(value, list) and len(value) > 0:
                if all(isinstance(v, str) for v in value):
                    # Check if strings are element symbols (1-2 chars, first letter capital)
                    import re
                    element_pattern = re.compile(r'^[A-Z][a-z]?$')
                    if all(element_pattern.match(v) for v in value):
                        elements = sorted(set(value))
                        return {
                            'method': f'{key}_strings',
                            'elements': elements,
                            'count': len(elements),
                            'model_data': model_data
                        }
        
        # Method 10: Check for atomic number arrays in model parameters
        if hasattr(model_data, 'state_dict'):
            state_dict = model_data.state_dict()
            for key in state_dict:
                if 'atomic' in key.lower() or 'z' in key.lower():
                    data = state_dict[key]
                    if isinstance(data, torch.Tensor) and len(data.shape) == 1:
                        atomic_numbers = data.tolist()
                        from ase.data import chemical_symbols
                        try:
                            elements = [chemical_symbols[int(z)] for z in atomic_numbers]
                            return {
                                'method': 'state_dict',
                                'elements': sorted(set(elements)),
                                'count': len(set(elements)),
                                'model_data': model_data
                            }
                        except:
                            pass
        
        # If no elements found, return empty
        return {
            'method': 'none',
            'elements': [],
            'count': 0,
            'model_data': model_data
        }
        
    except Exception as e:
        return {
            'method': 'error',
            'elements': [],
            'count': 0,
            'error': str(e),
            'model_data': {}
        }

def analyze_model_structure(model_path):
    """
    Analyze the model structure and print useful information
    """
    try:
        # Try loading with different methods
        model_data = None
        methods_tried = []
        
        # Method 1: Standard torch.load
        try:
            model_data = torch.load(model_path, map_location='cpu', weights_only=False)
            methods_tried.append('torch.load')
        except:
            pass
        
        # Method 2: With pickle
        if model_data is None:
            try:
                with open(model_path, 'rb') as f:
                    model_data = pickle.load(f)
                methods_tried.append('pickle')
            except:
                pass
        
        # Method 3: Try different torch versions
        if model_data is None:
            try:
                model_data = torch.load(model_path, map_location='cpu', weights_only=True)
                methods_tried.append('torch.load_weights_only')
            except:
                pass
        
        if model_data is None:
            return {'error': 'Could not load model with any method'}
        
        # Analyze structure
        structure = {
            'type': type(model_data).__name__,
            'keys': [],
            'has_state_dict': False,
            'has_metadata': False,
        }
        
        if isinstance(model_data, dict):
            structure['keys'] = list(model_data.keys())
            structure['is_dict'] = True
        elif hasattr(model_data, '__dict__'):
            structure['keys'] = list(model_data.__dict__.keys())
            structure['is_dict'] = False
        elif hasattr(model_data, 'state_dict'):
            structure['keys'] = list(model_data.state_dict().keys())
            structure['has_state_dict'] = True
        
        # Check for metadata
        if hasattr(model_data, 'metadata'):
            structure['has_metadata'] = True
            structure['metadata'] = model_data.metadata
        
        return {
            'structure': structure,
            'model_data': model_data,
            'methods_tried': methods_tried
        }
        
    except Exception as e:
        return {'error': str(e)}

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
        info = get_model_info(model_path)
        print(f"  {Colors.BLUE}Size:{Colors.NC} {info['size_mb']:.1f} MB")
        print(f"  {Colors.BLUE}Modified:{Colors.NC} {info['modified']}")
        
        # Analyze model structure
        structure_info = analyze_model_structure(model_path)
        
        if 'error' in structure_info:
            print(f"  {Colors.RED}✗ Error analyzing structure: {structure_info['error']}{Colors.NC}")
            continue
        
        # Extract elements
        result = extract_elements_from_model(model_path)
        
        print(f"  {Colors.BLUE}Detection method:{Colors.NC} {result['method']}")
        
        if result['elements']:
            print(f"  {Colors.GREEN}✓ Found {result['count']} elements:{Colors.NC}")
            # Print elements in rows of 10
            for j in range(0, len(result['elements']), 10):
                row = result['elements'][j:j+10]
                print(f"    {', '.join(row)}")
            
            all_elements.update(result['elements'])
            element_summary[model_path.name] = result['elements']
        else:
            print(f"  {Colors.YELLOW}⚠ No elements found in model file{Colors.NC}")
            print(f"  {Colors.YELLOW}  The model might store elements differently or use atomic numbers{Colors.NC}")
            
            # Show what's inside the model
            if 'structure' in structure_info:
                struct = structure_info['structure']
                print(f"\n  {Colors.BLUE}Model structure:{Colors.NC}")
                print(f"    Type: {struct['type']}")
                if struct.get('keys'):
                    print(f"    Keys: {', '.join(struct['keys'][:10])}")
                    if len(struct.get('keys', [])) > 10:
                        print(f"    ... and {len(struct['keys']) - 10} more")
                if struct.get('has_state_dict'):
                    print("    Has state_dict")
                if struct.get('has_metadata'):
                    print("    Has metadata")
    
    # Summary
    print(f"\n{Colors.BOLD}{'='*80}{Colors.NC}")
    print(f"{Colors.BOLD}   SUMMARY   {Colors.NC}")
    print(f"{Colors.BOLD}{'='*80}{Colors.NC}")
    
    if all_elements:
        print(f"\n{Colors.GREEN}Total unique elements found: {len(all_elements)}{Colors.NC}")
        print(f"{Colors.BLUE}All elements:{Colors.NC}")
        sorted_elements = sorted(list(all_elements))
        for i in range(0, len(sorted_elements), 10):
            row = sorted_elements[i:i+10]
            print(f"  {', '.join(row)}")
    else:
        print(f"\n{Colors.YELLOW}⚠ No elements could be detected from any model{Colors.NC}")
        print(f"{Colors.YELLOW}  This is because MACE models store atomic numbers internally,{Colors.NC}")
        print(f"{Colors.YELLOW}  not element symbols. The detection method needs to be enhanced.{Colors.NC}")
    
    # Print element summary per model
    print(f"\n{Colors.BLUE}Elements found per model:{Colors.NC}")
    for model_name, elements in element_summary.items():
        if elements:
            print(f"  {model_name}: {', '.join(elements)}")
        else:
            print(f"  {model_name}: {Colors.YELLOW}No elements detected{Colors.NC}")
    
    print(f"\n{Colors.CYAN}Note:{Colors.NC} This script detects elements by reading the model file directly.")
    print(f"  The elements shown are those that the model was trained on.")
    print(f"  If no elements are shown, the model may store atomic numbers instead.")
    
    # Show model structure info for debugging
    print(f"\n{Colors.CYAN}Debug info:{Colors.NC} To see what's inside your models, run:")
    print(f"  python -c \"import torch; data = torch.load('model_path'); print(data.keys() if isinstance(data, dict) else dir(data))\"")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n{Colors.YELLOW}Analysis interrupted by user{Colors.NC}")
        sys.exit(130)
    except Exception as e:
        print(f"\n{Colors.RED}Fatal error: {e}{Colors.NC}")
        sys.exit(1)
