#!/usr/bin/env python3
#===============================================================================
# FILE: check_mace_ml_installation.py
# DESCRIPTION: Check MACE-ML (Machine Learning Force Field) installation
#              in the current conda environment
#===============================================================================

import os
import sys
import subprocess
import importlib
import torch
from pathlib import Path
import logging
from datetime import datetime
from typing import Dict, List, Tuple, Optional
import json
import platform
import pkgutil

# Color codes for terminal output
class Colors:
    RED = '\033[0;31m'
    GREEN = '\033[0;32m'
    YELLOW = '\033[1;33m'
    BLUE = '\033[0;34m'
    CYAN = '\033[0;36m'
    NC = '\033[0m'
    BOLD = '\033[1m'
    MAGENTA = '\033[0;35m'

class MACEMLChecker:
    """Check MACE-ML installation and environment"""
    
    def __init__(self):
        self.conda_env = os.environ.get('CONDA_DEFAULT_ENV', 'unknown')
        self.conda_prefix = os.environ.get('CONDA_PREFIX', '')
        self.log_file = f"/tmp/mace_ml_check_{datetime.now().strftime('%Y%m%d_%H%M%S')}.log"
        
        self.setup_logging()
        
        self.results = {
            'passed': 0,
            'failed': 0,
            'warnings': 0,
            'checks': []
        }
        
        # MACE-ML packages to check
        self.mace_packages = [
            'mace',  # The actual import name (not mace_torch)
            'ase',
            'torch',
            'e3nn',
            'numpy',
            'scipy',
            'matscipy'
        ]
        
    def setup_logging(self):
        """Setup logging configuration"""
        logging.basicConfig(
            level=logging.INFO,
            format='[%(asctime)s] %(levelname)s: %(message)s',
            handlers=[
                logging.FileHandler(self.log_file),
                logging.StreamHandler()
            ]
        )
        self.logger = logging.getLogger(__name__)
    
    def get_package_version(self, package_name):
        """Get package version using multiple methods"""
        # Try importlib.metadata (Python 3.8+)
        try:
            import importlib.metadata
            return importlib.metadata.version(package_name)
        except (ImportError, importlib.metadata.PackageNotFoundError):
            pass
        
        # Try using pip
        try:
            result = subprocess.run(
                ['pip', 'show', package_name],
                capture_output=True,
                text=True,
                timeout=5
            )
            for line in result.stdout.split('\n'):
                if line.startswith('Version:'):
                    return line.split(':', 1)[1].strip()
        except:
            pass
        
        # Try using conda list
        try:
            result = subprocess.run(
                ['conda', 'list', package_name],
                capture_output=True,
                text=True,
                timeout=5
            )
            for line in result.stdout.split('\n'):
                if line.startswith(package_name):
                    parts = line.split()
                    if len(parts) >= 2:
                        return parts[1]
        except:
            pass
        
        return 'Unknown'
    
    def print_header(self, message: str):
        """Print a formatted section header"""
        print(f"\n{Colors.YELLOW}{'='*60}{Colors.NC}")
        print(f"{Colors.YELLOW} {message} {Colors.NC}")
        print(f"{Colors.YELLOW}{'='*60}{Colors.NC}\n")
    
    def print_success(self, message: str):
        print(f"{Colors.GREEN}✓{Colors.NC} {message}")
        self.results['passed'] += 1
        
    def print_failure(self, message: str):
        print(f"{Colors.RED}✗{Colors.NC} {message}")
        self.results['failed'] += 1
        
    def print_warning(self, message: str):
        print(f"{Colors.YELLOW}⚠{Colors.NC} {message}")
        self.results['warnings'] += 1
        
    def print_info(self, message: str):
        print(f"{Colors.CYAN}▶{Colors.NC} {message}")
    
    def print_bold(self, message: str):
        print(f"{Colors.BOLD}{message}{Colors.NC}")
    
    def check_conda_environment(self):
        """Check conda environment information"""
        self.print_header("Conda Environment Information")
        
        print(f"{Colors.BOLD}Environment:{Colors.NC} {self.conda_env}")
        print(f"{Colors.BOLD}Prefix:{Colors.NC} {self.conda_prefix}")
        print(f"{Colors.BOLD}Python:{Colors.NC} {sys.version.split()[0]}")
        print(f"{Colors.BOLD}OS:{Colors.NC} {platform.system()} {platform.release()}")
        print(f"{Colors.BOLD}Platform:{Colors.NC} {platform.machine()}")
        
        # Check conda packages
        try:
            result = subprocess.run(['conda', 'list'], 
                                  capture_output=True, 
                                  text=True,
                                  timeout=10)
            if result.returncode == 0:
                package_lines = [line for line in result.stdout.splitlines() if line and not line.startswith('#')]
                self.print_success(f"Conda environment has {len(package_lines)} packages installed")
            else:
                self.print_warning("Could not get conda package list")
        except Exception as e:
            self.print_warning(f"Could not get conda list: {e}")
    
    def check_mace_package(self):
        """Check MACE package installation"""
        self.print_header("MACE Package Check")
        
        # Try both possible import names
        import_names = ['mace', 'mace_torch']
        found_mace = False
        
        for import_name in import_names:
            try:
                module = importlib.import_module(import_name)
                found_mace = True
                version = getattr(module, '__version__', 'Unknown')
                if version == 'Unknown':
                    version = self.get_package_version('mace-torch')
                
                self.print_success(f"MACE package imported as '{import_name}' (version: {version})")
                
                # Get installation location
                file_path = module.__file__
                print(f"  Location: {file_path}")
                
                # Check if it's the correct version
                if version.startswith('0.3'):
                    self.print_success(f"MACE version {version} - compatible with this environment")
                else:
                    self.print_warning(f"MACE version {version} - check compatibility with other packages")
                
                # Try to import key modules
                modules_to_check = [
                    f'{import_name}.tools',
                    f'{import_name}.data',
                    f'{import_name}.calculators'
                ]
                available_modules = 0
                for module_path in modules_to_check:
                    try:
                        importlib.import_module(module_path)
                        self.print_success(f"Submodule {module_path} available")
                        available_modules += 1
                    except ImportError as e:
                        self.print_warning(f"Submodule {module_path} not available: {e}")
                
                # Try the calculator
                try:
                    from mace.calculators import MACECalculator
                    self.print_success("MACECalculator available from mace.calculators")
                except ImportError:
                    try:
                        from ase.calculators.mace import MACECalculator
                        self.print_success("MACECalculator available from ase.calculators.mace")
                    except ImportError:
                        self.print_warning("MACECalculator not available")
                
                break  # Found a working import
                
            except ImportError as e:
                continue
        
        if not found_mace:
            self.print_failure("MACE package not found (tried: mace, mace_torch)")
            self.print_info("Install with: pip install mace-torch")
            self.print_info("Or: conda install mace-torch -c conda-forge")
    
    def check_ase_integration(self):
        """Check ASE integration"""
        self.print_header("ASE Integration Check")
        
        try:
            import ase
            version = getattr(ase, '__version__', 'Unknown')
            if version == 'Unknown':
                version = self.get_package_version('ase')
            self.print_success(f"ASE installed (version: {version})")
            
            # Try to import MACE calculator from ASE
            try:
                from ase.calculators.mace import MACECalculator
                self.print_success("MACE calculator available in ASE")
            except ImportError:
                self.print_warning("MACE calculator not available in ASE.calculators.mace")
                self.print_info("  Try: from mace.calculators import MACECalculator")
            
            # Check available models
            print(f"\n{Colors.BOLD}Available MACE models:{Colors.NC}")
            
            # Check if model files exist in common locations
            model_paths = [
                Path.home() / ".ase" / "mace-models",
                Path.home() / ".cache" / "mace-models",
                Path.cwd() / "models",
                Path.cwd() / "mace-models",
                Path.cwd() / "checkpoints"
            ]
            
            found_models = []
            for path in model_paths:
                if path.exists():
                    model_files = list(path.glob("*.model")) + list(path.glob("*.pt")) + list(path.glob("*.pth"))
                    if model_files:
                        found_models.extend([str(f) for f in model_files])
            
            if found_models:
                for model in found_models[:5]:
                    size = Path(model).stat().st_size / (1024 * 1024) if Path(model).exists() else 0
                    print(f"  {Path(model).name} ({size:.1f} MB)")
                if len(found_models) > 5:
                    print(f"  ... and {len(found_models)-5} more")
            else:
                print("  No local model files found")
                self.print_info("  Download models from: https://github.com/ACEsuit/mace-models")
                
        except ImportError as e:
            self.print_failure(f"ASE not installed: {e}")
            self.print_info("Install with: pip install ase")
    
    def check_torch_setup(self):
        """Check PyTorch installation and CUDA support"""
        self.print_header("PyTorch Setup Check")
        
        try:
            import torch
            version = getattr(torch, '__version__', 'Unknown')
            self.print_success(f"PyTorch installed (version: {version})")
            
            # Check CUDA availability
            if torch.cuda.is_available():
                self.print_success(f"CUDA available: {torch.cuda.get_device_name(0)}")
                print(f"  CUDA version: {torch.version.cuda}")
                print(f"  GPU count: {torch.cuda.device_count()}")
                
                # Check memory
                for i in range(torch.cuda.device_count()):
                    mem_info = torch.cuda.get_device_properties(i).total_memory
                    print(f"  GPU {i} memory: {mem_info / 1e9:.1f} GB")
                self.print_success(f"GPU acceleration available with {torch.cuda.device_count()} GPU(s)")
            else:
                self.print_warning("CUDA not available - running on CPU only")
                self.print_info("For GPU support: conda install pytorch cudatoolkit -c pytorch")
                self.print_info("Or: pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118")
            
            # Check MPS support (Apple Silicon)
            if hasattr(torch.backends, 'mps') and torch.backends.mps.is_available():
                self.print_success("MPS (Apple Silicon) acceleration available")
                
        except ImportError as e:
            self.print_failure(f"PyTorch not installed: {e}")
            self.print_info("Install with: pip install torch")
            self.print_info("Or: conda install pytorch -c pytorch")
    
    def check_e3nn(self):
        """Check e3nn package (Euclidean neural networks)"""
        self.print_header("e3nn Package Check")
        
        try:
            import e3nn
            version = getattr(e3nn, '__version__', 'Unknown')
            if version == 'Unknown':
                version = self.get_package_version('e3nn')
            self.print_success(f"e3nn installed (version: {version})")
            
            # Check important modules
            modules = ['e3nn.o3', 'e3nn.nn', 'e3nn.math']
            available_modules = 0
            for module in modules:
                try:
                    importlib.import_module(module)
                    self.print_success(f"e3nn module {module} available")
                    available_modules += 1
                except ImportError:
                    self.print_warning(f"e3nn module {module} not available")
            
            if available_modules == 0:
                self.print_warning("e3nn submodules not found - check installation")
                    
        except ImportError as e:
            self.print_failure(f"e3nn not installed: {e}")
            self.print_info("Install with: pip install e3nn")
    
    def check_dependencies(self):
        """Check all MACE dependencies"""
        self.print_header("Dependency Check")
        
        dependencies = {
            'numpy': 'Numerical operations',
            'scipy': 'Scientific computing',
            'matplotlib': 'Visualization (optional)',
            'matscipy': 'Materials science utilities',
            'pandas': 'Data handling (optional)',
            'tqdm': 'Progress bars (optional)'
        }
        
        installed_packages = []
        for package, description in dependencies.items():
            try:
                importlib.import_module(package)
                version = self.get_package_version(package)
                self.print_success(f"{package} {version} - {description}")
                installed_packages.append(package)
            except (ImportError, subprocess.TimeoutExpired):
                self.print_warning(f"{package} not installed - {description}")
        
        if len(installed_packages) >= 4:
            self.print_success(f"Core dependencies installed ({len(installed_packages)}/{len(dependencies)})")
    
    def check_mace_models(self):
        """Check for MACE model files"""
        self.print_header("MACE Model Files")
        
        # Common model locations
        model_dirs = [
            Path.home() / ".ase" / "mace-models",
            Path.home() / ".cache" / "mace-models",
            Path.cwd() / "models",
            Path.cwd() / "mace-models",
            Path.cwd() / "checkpoints"
        ]
        
        found_models = []
        model_extensions = ['.model', '.pt', '.pth', '.ckpt']
        
        for search_dir in model_dirs:
            if search_dir.exists():
                for ext in model_extensions:
                    found_models.extend(search_dir.glob(f"*{ext}"))
        
        if found_models:
            # Deduplicate
            found_models = list(set(found_models))
            self.print_success(f"Found {len(found_models)} model files")
            print(f"\n{Colors.BOLD}Model files:{Colors.NC}")
            for model in found_models[:10]:
                size = model.stat().st_size / (1024 * 1024) if model.exists() else 0
                print(f"  {model.name} ({size:.1f} MB)")
            if len(found_models) > 10:
                print(f"  ... and {len(found_models)-10} more")
        else:
            self.print_warning("No MACE model files found in common locations")
            self.print_info("Download models from: https://github.com/ACEsuit/mace-models")
            self.print_info("Example: wget https://github.com/ACEsuit/mace-models/raw/main/mace_ani.model")
    
    def test_mace_calculation(self):
        """Test a simple MACE calculation"""
        self.print_header("Test MACE Calculation")
        
        try:
            import ase
            from ase.build import molecule
            
            # Try both import paths for MACECalculator
            MACECalculator = None
            try:
                from mace.calculators import MACECalculator
                self.print_info("Using MACECalculator from mace.calculators")
            except ImportError:
                try:
                    from ase.calculators.mace import MACECalculator
                    self.print_info("Using MACECalculator from ase.calculators.mace")
                except ImportError:
                    self.print_warning("MACECalculator not available")
                    return
            
            # Check for model files
            model_files = []
            model_dirs = [
                Path.home() / ".ase" / "mace-models",
                Path.cwd() / "models",
                Path.cwd() / "mace-models"
            ]
            
            for model_dir in model_dirs:
                if model_dir.exists():
                    model_files.extend(model_dir.glob("*.model"))
                    model_files.extend(model_dir.glob("*.pt"))
            
            if not model_files:
                self.print_warning("No model files found, cannot run test calculation")
                self.print_info("Download a model to test the full functionality")
                self.print_info("Example: wget https://github.com/ACEsuit/mace-models/raw/main/mace_ani.model")
                return
            
            # Use the first found model
            model_path = model_files[0]
            self.print_info(f"Testing with model: {model_path.name}")
            
            # Create a water molecule
            atoms = molecule('H2O')
            atoms.center(vacuum=3.0)
            
            # Set up calculator
            try:
                calculator = MACECalculator(model_path=str(model_path), device='cpu')
                atoms.calc = calculator
                
                # Calculate energy
                energy = atoms.get_potential_energy()
                self.print_success(f"Test calculation successful!")
                print(f"  Energy of H2O: {energy:.6f} eV")
                
                # Calculate forces
                forces = atoms.get_forces()
                self.print_success("Force calculation successful")
                print(f"  Forces (eV/Å):")
                for i, force in enumerate(forces):
                    print(f"    Atom {i}: {force}")
                    
            except Exception as e:
                self.print_failure(f"Error during calculation: {e}")
                self.print_info("The model might be incompatible with this MACE version")
            
        except ImportError as e:
            self.print_warning(f"Could not run test: {e}")
        except Exception as e:
            self.print_failure(f"Test calculation failed: {e}")
    
    def check_performance(self):
        """Check performance and optimization"""
        self.print_header("Performance Settings")
        
        # Check environment variables
        env_vars = {
            'OMP_NUM_THREADS': 'OpenMP threads',
            'MKL_NUM_THREADS': 'MKL threads',
            'CUDA_VISIBLE_DEVICES': 'Visible CUDA devices',
            'TORCH_DEVICE': 'PyTorch device'
        }
        
        print(f"{Colors.BOLD}Environment variables:{Colors.NC}")
        has_settings = False
        for var, desc in env_vars.items():
            value = os.environ.get(var, 'Not set')
            if value != 'Not set':
                print(f"  {Colors.GREEN}{var}{Colors.NC} = {value} ({desc})")
                has_settings = True
            else:
                print(f"  {Colors.YELLOW}{var}{Colors.NC} = {value} ({desc})")
        
        if not has_settings:
            self.print_info("No performance environment variables set - using defaults")
        
        # Check PyTorch configuration
        try:
            import torch
            print(f"\n{Colors.BOLD}PyTorch configuration:{Colors.NC}")
            print(f"  Default device: {'cuda' if torch.cuda.is_available() else 'cpu'}")
            if torch.cuda.is_available():
                print(f"  CUDA devices: {torch.cuda.device_count()}")
                
            # Check for optimizations
            import torch.backends
            if hasattr(torch.backends, 'cudnn'):
                if torch.backends.cudnn.is_available():
                    print(f"  cuDNN available: {torch.backends.cudnn.version()}")
                    
        except Exception:
            pass
    
    def generate_summary(self):
        """Generate installation status summary"""
        self.print_header("MACE-ML Installation Status Summary")
        
        total_checks = self.results['passed'] + self.results['failed'] + self.results['warnings']
        
        print(f"\n{Colors.BOLD}Check Summary:{Colors.NC}")
        print(f"  {Colors.GREEN}Passed: {self.results['passed']}{Colors.NC}")
        print(f"  {Colors.RED}Failed: {self.results['failed']}{Colors.NC}")
        print(f"  {Colors.YELLOW}Warnings: {self.results['warnings']}{Colors.NC}")
        print(f"  Total Checks: {total_checks}")
        
        print(f"\n{Colors.BOLD}Environment Summary:{Colors.NC}")
        try:
            import torch
            device = 'GPU' if torch.cuda.is_available() else 'CPU'
            print(f"  PyTorch: {getattr(torch, '__version__', 'Unknown')} ({device})")
        except:
            print(f"  PyTorch: Not installed")
            
        try:
            import mace
            version = getattr(mace, '__version__', 'Unknown')
            print(f"  MACE: {version}")
        except:
            try:
                import mace_torch
                version = getattr(mace_torch, '__version__', 'Unknown')
                print(f"  MACE: {version}")
            except:
                print(f"  MACE: Not installed")
            
        try:
            import ase
            version = getattr(ase, '__version__', 'Unknown')
            print(f"  ASE: {version}")
        except:
            print(f"  ASE: Not installed")
        
        if self.results['failed'] == 0:
            print(f"\n{Colors.GREEN}{Colors.BOLD}✓ MACE-ML installation appears to be healthy{Colors.NC}")
            
            # Additional recommendations
            if self.results['warnings'] > 0:
                print(f"\n{Colors.YELLOW}Recommendations:{Colors.NC}")
                # Check for models
                if not any(Path.home().glob(".ase/mace-models/*.model")):
                    print("  • Download MACE models for ready-to-use force fields")
                # Check for GPU support
                try:
                    import torch
                    if not torch.cuda.is_available():
                        print("  • Install CUDA version of PyTorch for GPU acceleration")
                except:
                    pass
                print("  • Set OMP_NUM_THREADS environment variable for better CPU performance")
        else:
            print(f"\n{Colors.RED}{Colors.BOLD}✗ Some issues were detected. Review the output above.{Colors.NC}")
        
        print(f"\n{Colors.CYAN}Log file saved to: {self.log_file}{Colors.NC}")
    
    def run(self):
        """Run all checks"""
        print(f"{Colors.GREEN}{'='*60}{Colors.NC}")
        print(f"{Colors.GREEN}{Colors.BOLD}   MACE-ML Installation Check Script   {Colors.NC}")
        print(f"{Colors.GREEN}{'='*60}{Colors.NC}\n")
        
        self.logger.info("Starting MACE-ML installation check")
        
        # Run checks in logical order
        self.check_conda_environment()
        self.check_mace_package()
        self.check_ase_integration()
        self.check_torch_setup()
        self.check_e3nn()
        self.check_dependencies()
        self.check_mace_models()
        
        # Try test calculation if possible
        try:
            self.test_mace_calculation()
        except:
            pass
            
        self.check_performance()
        
        # Generate summary
        self.generate_summary()
        
        self.logger.info("MACE-ML installation check completed")
        return self.results['failed'] == 0

def main():
    """Main entry point"""
    try:
        checker = MACEMLChecker()
        success = checker.run()
        sys.exit(0 if success else 1)
    except KeyboardInterrupt:
        print(f"\n{Colors.YELLOW}Script interrupted by user{Colors.NC}")
        sys.exit(130)
    except Exception as e:
        print(f"{Colors.RED}Fatal error: {e}{Colors.NC}")
        sys.exit(1)

if __name__ == "__main__":
    main()
