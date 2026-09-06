# =============================================================================
# FILE: calculator.py
# Quantum ESPRESSO calculator setup and management.
# =============================================================================

import os
from ase.calculators.espresso import Espresso, EspressoProfile
from utils import build_mpi_command

class QECalculatorSetup:
    """Setup and manage Quantum ESPRESSO calculators."""
    
    def __init__(self, config):
        """Initialize with configuration."""
        self.config = config
        self.qe_config = config.get('qe', {})
        self.pseudo_dir = self.qe_config.get('pseudo_dir', './pseudopotentials/')
        self.pseudopotentials = self.qe_config.get('pseudopotentials', {})
        
        # Build command with MPI
        parallel_config = self.qe_config.get('parallel', {})
        self.command = build_mpi_command(parallel_config)
        
        # Store input data
        self.main_input_data = None
        self.vib_input_data = None
        self.calc = None
        self.vib_calc = None
        
        self._setup_main_calculator()
        self._setup_vibration_calculator()
    
    def _create_profile(self):
        """Create EspressoProfile."""
        return EspressoProfile(
            command=self.command,
            pseudo_dir=self.pseudo_dir,
        )
    
    def _setup_main_calculator(self):
        """Setup main Quantum ESPRESSO calculator."""
        profile = self._create_profile()
        
        self.main_input_data = {
            'calculation': 'scf',
            'restart_mode': 'from_scratch',
            'outdir': './tmp/',
            'prefix': 'qe',
            'tprnfor': True,
            'tstress': True,
            'verbosity': 'low',
            
            'ecutwfc': self.qe_config.get('ecutwfc', 80.0),
            'ecutrho': self.qe_config.get('ecutrho', 320.0),
            'occupations': 'smearing',
            'smearing': self.qe_config.get('smearing', 'gaussian'),
            'degauss': self.qe_config.get('degauss', 0.01),
            'nspin': 1,
            'ntyp': 1,
            
            'conv_thr': self.qe_config.get('conv_thr', 1.0e-10),
            'mixing_beta': self.qe_config.get('mixing_beta', 0.7),
            'electron_maxstep': self.qe_config.get('electron_maxstep', 200),
        }
        
        self.calc = Espresso(
            profile=profile,
            pseudopotentials=self.pseudopotentials,
            input_data=self.main_input_data,
            kpts=self.qe_config.get('kpts', [1, 1, 1]),
        )
    
    def _setup_vibration_calculator(self):
        """Setup a separate calculator for vibrations."""
        profile = self._create_profile()
        
        self.vib_input_data = {
            'calculation': 'scf',
            'restart_mode': 'from_scratch',
            'outdir': './tmp/',
            'prefix': 'vib',
            'tprnfor': True,
            'tstress': True,
            'verbosity': 'low',
            
            'ecutwfc': max(40.0, self.qe_config.get('ecutwfc', 80.0) * 0.6),
            'ecutrho': max(160.0, self.qe_config.get('ecutrho', 320.0) * 0.6),
            'occupations': 'smearing',
            'smearing': self.qe_config.get('smearing', 'gaussian'),
            'degauss': self.qe_config.get('degauss', 0.01),
            'nspin': 1,
            'ntyp': 1,
            
            'conv_thr': 1.0e-8,
            'mixing_beta': self.qe_config.get('mixing_beta', 0.7),
            'electron_maxstep': 100,
        }
        
        self.vib_calc = Espresso(
            profile=profile,
            pseudopotentials=self.pseudopotentials,
            input_data=self.vib_input_data,
            kpts=self.qe_config.get('kpts', [1, 1, 1]),
        )
    
    def update_for_molecule(self, symbols):
        """Update calculators for specific molecule."""
        pseudo_dict = {sym: self.pseudopotentials.get(sym, f'{sym}.upf') 
                      for sym in set(symbols)}
        
        # Update main calculator
        self.main_input_data['ntyp'] = len(set(symbols))
        profile = self._create_profile()
        
        self.calc = Espresso(
            profile=profile,
            pseudopotentials=pseudo_dict,
            input_data=self.main_input_data,
            kpts=self.qe_config.get('kpts', [1, 1, 1]),
        )
        
        # Update vibration calculator
        self.vib_input_data['ntyp'] = len(set(symbols))
        
        self.vib_calc = Espresso(
            profile=profile,
            pseudopotentials=pseudo_dict,
            input_data=self.vib_input_data,
            kpts=self.qe_config.get('kpts', [1, 1, 1]),
        )
    
    def get_pseudopotential(self, symbol):
        """Get pseudopotential filename for given element."""
        return self.pseudopotentials.get(symbol, f'{symbol}.upf')
    
    def check_pseudopotential_exists(self, symbol):
        """Check if pseudopotential file exists."""
        pp_file = self.get_pseudopotential(symbol)
        pp_path = os.path.join(self.pseudo_dir, pp_file)
        exists = os.path.exists(pp_path)
        if not exists:
            print(f"  ✗ Pseudopotential {pp_path} not found!")
        return exists