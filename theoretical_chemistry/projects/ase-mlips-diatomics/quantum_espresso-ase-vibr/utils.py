# =============================================================================
# FILE: utils.py
# Utility functions for the Quantum ESPRESSO calculator.
# =============================================================================

import os
import numpy as np
from ase import Atoms

def get_atomic_masses(symbols):
    """Get atomic masses in amu."""
    masses = {
        'H': 1.008, 'He': 4.0026, 'Li': 6.941, 'Be': 9.0122,
        'B': 10.81, 'C': 12.011, 'N': 14.007, 'O': 15.999,
        'F': 18.998, 'Ne': 20.180, 'Na': 22.990, 'Mg': 24.305,
        'Al': 26.982, 'Si': 28.086, 'P': 30.974, 'S': 32.065,
        'Cl': 35.453, 'Ar': 39.948, 'K': 39.098, 'Ca': 40.078,
        'Fe': 55.845, 'Ni': 58.693, 'Cu': 63.546, 'Ag': 107.868,
        'Au': 196.967, 'Pt': 195.084, 'Pd': 106.42
    }
    return [masses.get(s, 0.0) for s in symbols]

def setup_directories(pseudo_dir, output_dir):
    """Create necessary directories."""
    os.makedirs(pseudo_dir, exist_ok=True)
    os.makedirs('./tmp/', exist_ok=True)
    os.makedirs('./vib/', exist_ok=True)
    os.makedirs(output_dir, exist_ok=True)

def create_diatomic(symbols, distance, cell_size=15.0):
    """Create a diatomic molecule with vacuum cell."""
    atoms = Atoms(symbols, positions=[(0, 0, 0), (distance, 0, 0)])
    atoms.center(vacuum=cell_size/2)
    cell = np.eye(3) * (distance + cell_size)
    atoms.set_cell(cell)
    atoms.set_pbc(True)
    return atoms

def parse_vibration_methods(vib_method):
    """
    Parse the vibration method string and return a list of methods to run.
    """
    method_map = {
        '1d': ['1d'],
        'xonly': ['xonly'],
        'full': ['full'],
        '1d+xonly': ['1d', 'xonly'],
        '1d+full': ['1d', 'full'],
        'xonly+full': ['xonly', 'full'],
        'all': ['1d', 'xonly', 'full']
    }
    return method_map.get(vib_method, ['1d'])

def build_mpi_command(parallel_config):
    """Build the MPI command string."""
    use_mpi = parallel_config.get('use_mpi', True)
    nprocs = parallel_config.get('nprocs', 4)
    mpi_command = parallel_config.get('mpi_command', 'mpirun')
    
    if use_mpi and nprocs > 1:
        if 'SLURM_NTASKS' in os.environ:
            return f'srun -n {nprocs} pw.x'
        else:
            return f'{mpi_command} -np {nprocs} pw.x'
    else:
        return 'pw.x'