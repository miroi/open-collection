#!/usr/bin/env python3
"""
Simple Package Inspector for NequIP/Allegro Setup
Shows installed packages and what's needed
"""

import subprocess
import sys
import importlib.metadata
import os

def get_installed_pip_packages():
    """Get installed pip packages."""
    packages = {}
    try:
        # Use importlib.metadata for Python 3.8+
        for dist in importlib.metadata.distributions():
            packages[dist.metadata['Name'].lower()] = dist.version
    except:
        # Fallback to pip list
        result = subprocess.run(['pip', 'list', '--format=freeze'], 
                              capture_output=True, text=True)
        for line in result.stdout.strip().split('\n'):
            if '==' in line:
                name, version = line.split('==')
                packages[name.lower()] = version
    return packages

def check_ubuntu_package(pkg):
    """Check if Ubuntu package is installed."""
    try:
        result = subprocess.run(['dpkg', '-l', pkg], 
                              capture_output=True, text=True)
        return result.returncode == 0 and 'ii' in result.stdout
    except:
        return False

def main():
    print("=" * 70)
    print("NequIP/Allegro Package Inspector")
    print("=" * 70)
    
    # System info
    print("\n[System Information]")
    print(f"  OS: Ubuntu 24.04 LTS")
    print(f"  Python: {sys.version.split()[0]}")
    print(f"  Virtual Env: {os.environ.get('VIRTUAL_ENV', 'No')}")
    
    # CUDA info
    try:
        import torch
        print(f"  PyTorch: {torch.__version__}")
        print(f"  CUDA Available: {'Yes' if torch.cuda.is_available() else 'No'}")
        if torch.cuda.is_available():
            print(f"  GPU: {torch.cuda.get_device_name(0)}")
            print(f"  GPU Memory: {torch.cuda.get_device_properties(0).total_memory / 1e9:.2f} GB")
    except:
        print("  PyTorch: Not installed")
    
    # Core Python packages
    print("\n[Core Python Packages]")
    core_packages = ['torch', 'nequip', 'ase', 'numpy', 'scipy', 'e3nn']
    installed = get_installed_pip_packages()
    
    for pkg in core_packages:
        if pkg in installed:
            print(f"  ✅ {pkg}: {installed[pkg]}")
        else:
            print(f"  ❌ {pkg}: Not installed")
    
    # Additional useful packages
    print("\n[Additional Useful Packages]")
    useful = ['matplotlib', 'pandas', 'tqdm', 'pyyaml', 'h5py', 'tensorboard']
    for pkg in useful:
        if pkg in installed:
            print(f"  ✅ {pkg}: {installed[pkg]}")
        else:
            print(f"  ⚠️  {pkg}: Not installed (optional)")
    
    # Ubuntu packages
    print("\n[Ubuntu System Packages]")
    ubuntu_packages = {
        'build-essential': 'Compiler tools',
        'python3-dev': 'Python headers',
        'nvidia-cuda-toolkit': 'CUDA toolkit',
        'cmake': 'Build tool',
        'git': 'Version control',
        'wget': 'Download tool',
    }
    
    for pkg, desc in ubuntu_packages.items():
        if check_ubuntu_package(pkg):
            print(f"  ✅ {pkg}: {desc}")
        else:
            print(f"  ❌ {pkg}: {desc}")
    
    # Status summary
    print("\n" + "=" * 70)
    print("SUMMARY")
    print("=" * 70)
    
    all_core = all(pkg in installed for pkg in core_packages)
    if all_core:
        print("✅ All core packages are installed!")
        print("✅ Ready for NequIP calculations!")
    else:
        print("⚠️ Some core packages are missing.")
        print("   Run: pip install torch nequip ase numpy scipy e3nn")
    
    # Quick test
    print("\n[Quick Test]")
    try:
        from ase.build import bulk
        atoms = bulk('Si', 'diamond', a=5.43)
        print("  ✅ ASE import successful")
    except:
        print("  ❌ ASE import failed")
    
    try:
        from nequip.integrations.ase import NequIPCalculator
        print("  ✅ NequIP import successful")
    except:
        print("  ❌ NequIP import failed")

if __name__ == "__main__":
    main()
