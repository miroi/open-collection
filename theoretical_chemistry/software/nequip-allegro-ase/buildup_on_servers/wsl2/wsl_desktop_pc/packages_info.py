#!/usr/bin/env python3
"""
System Package Inspector for NequIP/Allegro Setup
Shows all Ubuntu and pip packages needed/recommended for the environment
"""

import subprocess
import sys
import os
import platform
import importlib.metadata
import pkg_resources
from typing import List, Dict, Tuple

class PackageInspector:
    def __init__(self):
        self.system_info = self._get_system_info()
        self.ubuntu_packages = self._get_ubuntu_packages()
        self.pip_packages = self._get_pip_packages()
        
    def _get_system_info(self) -> Dict:
        """Get system information."""
        info = {
            "OS": platform.platform(),
            "Distribution": self._get_distribution(),
            "Python version": sys.version.split()[0],
            "Python path": sys.executable,
            "Virtual env": os.environ.get('VIRTUAL_ENV', 'No virtual environment'),
            "CUDA available": self._check_cuda(),
        }
        
        # Get GPU info if available
        try:
            result = subprocess.run(['nvidia-smi', '--query-gpu=name', '--format=csv,noheader'], 
                                  capture_output=True, text=True)
            if result.returncode == 0:
                info["GPU"] = result.stdout.strip()
        except:
            pass
            
        return info
    
    def _get_distribution(self) -> str:
        """Get Linux distribution info."""
        try:
            with open('/etc/os-release') as f:
                for line in f:
                    if line.startswith('PRETTY_NAME='):
                        return line.split('=')[1].strip().strip('"')
        except:
            return "Unknown"
        return "Unknown"
    
    def _check_cuda(self) -> str:
        """Check if CUDA is available."""
        try:
            import torch
            if torch.cuda.is_available():
                return f"Available (v{torch.version.cuda})"
            else:
                return "Not available"
        except:
            return "Unknown (torch not installed)"
    
    def _get_ubuntu_packages(self) -> Dict[str, Tuple[str, str]]:
        """Get essential Ubuntu system packages for NequIP."""
        packages = {
            # Essential build tools
            "build-essential": ("Build tools", "Required for compiling C++ code"),
            "gcc": ("Compiler", "C compiler, needed for many packages"),
            "g++": ("Compiler", "C++ compiler, needed for many packages"),
            "make": ("Build tool", "Required for compiling packages"),
            "cmake": ("Build tool", "Used by some Python packages"),
            
            # Python development
            "python3-dev": ("Python dev", "Headers for Python development"),
            "python3-pip": ("Package manager", "Python package installer"),
            "python3-venv": ("Virtual env", "For creating virtual environments"),
            
            # CUDA-related (for GPU support)
            "nvidia-cuda-toolkit": ("CUDA toolkit", "Required for GPU acceleration"),
            "nvidia-driver-550": ("NVIDIA driver", "GPU driver (version may vary)"),
            "libcudart12": ("CUDA runtime", "CUDA runtime library"),
            
            # System libraries
            "libssl-dev": ("SSL dev", "Required for some Python packages"),
            "libffi-dev": ("FFI dev", "Required for cffi"),
            "libbz2-dev": ("BZ2 dev", "Required for some Python packages"),
            "liblzma-dev": ("LZMA dev", "Required for some Python packages"),
            "libsqlite3-dev": ("SQLite dev", "Required for Python SQLite support"),
            
            # Optional but useful
            "git": ("Version control", "For cloning repositories"),
            "wget": ("Download tool", "For downloading files"),
            "curl": ("Download tool", "For downloading files"),
            "htop": ("System monitor", "For monitoring resources"),
            "nvtop": ("GPU monitor", "For monitoring GPU usage"),
            
            # Scientific computing (optional)
            "libatlas-base-dev": ("BLAS/LAPACK", "For optimized linear algebra"),
            "libopenblas-dev": ("BLAS/LAPACK", "For optimized linear algebra"),
        }
        return packages
    
    def _get_pip_packages(self) -> Dict[str, str]:
        """Get pip packages needed for NequIP/Allegro."""
        packages = {
            # Core packages
            "torch": "Deep learning framework (with CUDA support)",
            "nequip": "Neural network potentials for atomic systems",
            "ase": "Atomic Simulation Environment",
            
            # Scientific computing
            "numpy": "Array operations",
            "scipy": "Scientific computing",
            "matplotlib": "Plotting",
            "pandas": "Data manipulation",
            
            # E3NN (required by NequIP)
            "e3nn": "E3nn: Euclidean neural networks",
            
            # Optimization and tools
            "tqdm": "Progress bars",
            "pyyaml": "YAML parsing for configuration files",
            "h5py": "HDF5 file support",
            "tensorboard": "TensorBoard for logging (optional)",
            
            # Additional utilities
            "nvidia-ml-py3": "NVIDIA Management Library (optional)",
            "psutil": "Process monitoring (optional)",
            "tabulate": "Pretty-print tables (optional)",
        }
        
        # Try to get actual installed versions
        installed = {}
        for pkg in packages.keys():
            try:
                version = importlib.metadata.version(pkg)
                installed[pkg] = version
            except:
                installed[pkg] = "Not installed"
        
        return installed
    
    def print_report(self):
        """Print the complete report."""
        print("=" * 80)
        print("NequIP/Allegro System Package Inspector")
        print("=" * 80)
        
        # System Information
        print("\n" + "=" * 80)
        print("SYSTEM INFORMATION")
        print("=" * 80)
        for key, value in self.system_info.items():
            print(f"  {key:20s}: {value}")
        
        # Ubuntu Packages
        print("\n" + "=" * 80)
        print("UBUNTU SYSTEM PACKAGES (Required/Recommended)")
        print("=" * 80)
        print("\nInstallation command:")
        print("  sudo apt-get install \\")
        pkgs = sorted(self.ubuntu_packages.keys())
        for i, pkg in enumerate(pkgs):
            end = " \\" if i < len(pkgs) - 1 else ""
            print(f"    {pkg}{end}")
        
        print("\nPackage details:")
        for pkg, (category, desc) in sorted(self.ubuntu_packages.items()):
            print(f"  {pkg:30s} [{category:15s}] {desc}")
        
        # Check which Ubuntu packages are installed
        print("\n" + "-" * 80)
        print("Package Status Check:")
        for pkg in sorted(self.ubuntu_packages.keys()):
            status = self._check_ubuntu_package(pkg)
            symbol = "✅" if status else "❌"
            print(f"  {symbol} {pkg}")
        
        # Pip Packages
        print("\n" + "=" * 80)
        print("PIP PACKAGES (Required for NequIP/Allegro)")
        print("=" * 80)
        print("\nInstallation commands:")
        print("  pip install --upgrade pip")
        print("  pip install \\")
        installed_pkgs = sorted(self.pip_packages.keys())
        for i, pkg in enumerate(installed_pkgs):
            end = " \\" if i < len(installed_pkgs) - 1 else ""
            version = self.pip_packages[pkg]
            if version != "Not installed":
                print(f"    {pkg}=={version}{end}")
            else:
                print(f"    {pkg}{end}")
        
        print("\nPackage details:")
        for pkg, version in sorted(self.pip_packages.items()):
            status = f"v{version}" if version != "Not installed" else "❌ Not installed"
            desc = self._get_pip_description(pkg)
            print(f"  {pkg:25s} {status:20s} {desc}")
        
        # Post-installation verification
        print("\n" + "=" * 80)
        print("POST-INSTALLATION VERIFICATION")
        print("=" * 80)
        self._verify_installation()
        
        # Recommendations
        print("\n" + "=" * 80)
        print("RECOMMENDATIONS")
        print("=" * 80)
        self._print_recommendations()
    
    def _check_ubuntu_package(self, package: str) -> bool:
        """Check if Ubuntu package is installed."""
        try:
            result = subprocess.run(['dpkg', '-l', package], 
                                  capture_output=True, text=True)
            return result.returncode == 0 and 'ii' in result.stdout
        except:
            return False
    
    def _get_pip_description(self, package: str) -> str:
        """Get description for pip package."""
        descriptions = {
            "torch": "PyTorch with CUDA support",
            "nequip": "NequIP: Neural network potentials",
            "ase": "Atomic Simulation Environment",
            "numpy": "NumPy: Array computing",
            "scipy": "SciPy: Scientific computing",
            "matplotlib": "Matplotlib: Plotting",
            "pandas": "Pandas: Data manipulation",
            "e3nn": "E3NN: Euclidean neural networks",
            "tqdm": "Progress bars",
            "pyyaml": "YAML parser",
            "h5py": "HDF5 support",
            "tensorboard": "TensorBoard logging",
            "nvidia-ml-py3": "NVIDIA Management Library",
            "psutil": "Process monitoring",
            "tabulate": "Pretty table printing",
        }
        return descriptions.get(package, "")
    
    def _verify_installation(self):
        """Verify key components are working."""
        print("\nTesting key components...")
        
        # Check Python version
        print(f"  Python {sys.version.split()[0]} : {'✅' if sys.version_info >= (3, 8) else '⚠️ (needs >=3.8)'}")
        
        # Check torch
        try:
            import torch
            cuda = "✅" if torch.cuda.is_available() else "⚠️"
            print(f"  PyTorch {torch.__version__} : {cuda} (CUDA: {torch.version.cuda})")
            if torch.cuda.is_available():
                print(f"    GPU: {torch.cuda.get_device_name(0)}")
                print(f"    Memory: {torch.cuda.get_device_properties(0).total_memory / 1e9:.2f} GB")
        except ImportError:
            print("  ❌ PyTorch not installed")
        
        # Check NequIP
        try:
            import nequip
            print(f"  NequIP {nequip.__version__} : ✅")
        except ImportError:
            print("  ❌ NequIP not installed")
        
        # Check ASE
        try:
            import ase
            print(f"  ASE {ase.__version__} : ✅")
        except ImportError:
            print("  ❌ ASE not installed")
    
    def _print_recommendations(self):
        """Print recommendations based on detected environment."""
        recommendations = []
        
        # Check if CUDA is available
        try:
            import torch
            if not torch.cuda.is_available():
                recommendations.append("  ⚠️ CUDA not available - consider installing NVIDIA drivers and CUDA toolkit")
            else:
                recommendations.append("  ✅ CUDA is available - GPU acceleration enabled")
        except:
            recommendations.append("  ⚠️ Torch not installed - install PyTorch with CUDA support")
        
        # Check virtual environment
        if not os.environ.get('VIRTUAL_ENV'):
            recommendations.append("  ℹ️ Not using virtual environment - recommended for isolation")
        
        # Memory recommendation
        try:
            import torch
            if torch.cuda.is_available():
                gpu_mem = torch.cuda.get_device_properties(0).total_memory / 1e9
                if gpu_mem < 4:
                    recommendations.append(f"  ℹ️ GPU has {gpu_mem:.1f}GB VRAM - may limit large systems")
                recommendations.append("  ℹ️ For large systems (>1000 atoms), use CPU")
        except:
            pass
        
        # Python version
        if sys.version_info < (3, 8):
            recommendations.append("  ⚠️ Python 3.8+ recommended for best compatibility")
        
        if recommendations:
            for rec in recommendations:
                print(rec)
        else:
            print("  ✅ All systems ready for NequIP calculations!")
    
    def export_requirements(self, filename="requirements.txt"):
        """Export pip requirements to file."""
        with open(filename, 'w') as f:
            for pkg, version in sorted(self.pip_packages.items()):
                if version != "Not installed":
                    f.write(f"{pkg}=={version}\n")
                else:
                    f.write(f"{pkg}\n")
        print(f"\n✅ Requirements exported to {filename}")
    
    def export_ubuntu_install_script(self, filename="install_ubuntu_packages.sh"):
        """Export Ubuntu installation script."""
        with open(filename, 'w') as f:
            f.write("#!/bin/bash\n")
            f.write("# Install Ubuntu packages for NequIP/Allegro\n")
            f.write("set -e\n\n")
            f.write("echo 'Installing Ubuntu packages...'\n")
            f.write("sudo apt-get update\n")
            f.write("sudo apt-get install -y \\\n")
            pkgs = sorted(self.ubuntu_packages.keys())
            for i, pkg in enumerate(pkgs):
                end = " \\" if i < len(pkgs) - 1 else ""
                f.write(f"  {pkg}{end}\n")
            f.write("\necho 'Ubuntu packages installed successfully!'")
        
        # Make executable
        os.chmod(filename, 0o755)
        print(f"\n✅ Ubuntu install script exported to {filename}")
        print(f"   Run: ./{filename}")

def main():
    inspector = PackageInspector()
    inspector.print_report()
    
    # Ask if user wants to export files
    print("\n" + "=" * 80)
    response = input("Export requirements.txt and install script? (y/n): ")
    if response.lower() == 'y':
        inspector.export_requirements()
        inspector.export_ubuntu_install_script()
        print("\n📁 Files created:")
        print("  - requirements.txt (pip install -r requirements.txt)")
        print("  - install_ubuntu_packages.sh (sudo bash install_ubuntu_packages.sh)")

if __name__ == "__main__":
    main()
