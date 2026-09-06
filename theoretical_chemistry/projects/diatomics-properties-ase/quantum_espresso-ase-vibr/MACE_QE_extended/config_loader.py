# =============================================================================
# FILE: config_loader.py
# Configuration loading and management.
# =============================================================================

import os
import sys
import yaml

def load_config(config_file='config_qe.yaml'):
    """Load configuration from YAML file."""
    if not os.path.exists(config_file):
        print(f"Error: Config file {config_file} not found!")
        sys.exit(1)
    
    try:
        with open(config_file, 'r') as f:
            config = yaml.safe_load(f)
        print(f"✓ Loaded configuration from {config_file}")
        return config
    except Exception as e:
        print(f"Error loading config: {e}")
        sys.exit(1)

def get_default_config():
    """Return default configuration."""
    return {
        'general': {
            'temperature': 298.15,
            'pressure': 101325,
            'fmax': 0.001,
            'max_steps': 100,
            'compare_with_reference': True,
            'verbose': True
        },
        'molecules': {
            'N2': {'symbols': ['N', 'N'], 'initial_distance': 1.2, 
                   'mass': 28.0134, 'spin': 0, 'symmetry': 2, 'geometry': 'linear'},
            'H2': {'symbols': ['H', 'H'], 'initial_distance': 0.8,
                   'mass': 2.01588, 'spin': 0, 'symmetry': 2, 'geometry': 'linear'},
            'O2': {'symbols': ['O', 'O'], 'initial_distance': 1.3,
                   'mass': 31.9988, 'spin': 1, 'symmetry': 2, 'geometry': 'linear'},
            'F2': {'symbols': ['F', 'F'], 'initial_distance': 1.4,
                   'mass': 37.9968, 'spin': 0, 'symmetry': 2, 'geometry': 'linear'},
            'Cl2': {'symbols': ['Cl', 'Cl'], 'initial_distance': 2.0,
                   'mass': 70.906, 'spin': 0, 'symmetry': 2, 'geometry': 'linear'}
        },
        'calculators': {
            'EMT': {'enabled': True},
            'MACE': {'enabled': False, 'model': 'MACE', 'device': 'cpu'}
        },
        'output': {
            'save_structures': True,
            'save_trajectories': True,
            'verbose': True,
            'output_dir': 'results_qe'
        },
        'advanced': {
            'vibrations': {
                'delta': 0.005,
                'nfree': 4,
                'method': 'polyfit'
            },
            'optimization': {
                'algorithm': 'BFGS',
                'max_steps': 100,
                'fmax': 0.0005
            }
        }
    }