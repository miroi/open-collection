#!/usr/bin/env python
"""
Check what potentials are available in your QUIPPY installation.
"""

import quippy
from quippy.potential import Potential
import subprocess
import os

print("="*60)
print("Checking QUIPPY Installation")
print("="*60)

# Method 1: Try to list potentials using quip command
try:
    result = subprocess.run(['quip', 'list'], capture_output=True, text=True)
    print("Available potentials from 'quip list':")
    print(result.stdout)
except:
    print("Could not run 'quip list'")

# Method 2: Try creating a dummy potential and check
print("\nTrying to create different potentials:")

# Try common potentials
potential_names = [
    "IP Si",
    "IP Silicon",
    "IP GAP",
    "GAP",
    "LennardJones",
    "LJ",
    "Tersoff",
    "tersoff"
]

for pot_name in potential_names:
    try:
        calc = Potential(args_str=pot_name, param_str="")
        print(f"✓ {pot_name} - Success")
        # Clean up
        del calc
    except Exception as e:
        # Check if it's a "not found" error vs other error
        if "not found" in str(e).lower():
            print(f"✗ {pot_name} - Not found")
        else:
            print(f"✗ {pot_name} - Error: {str(e)[:80]}")

# Method 3: Check environment variables
print("\nEnvironment variables:")
for var in ['QUIP_ROOT', 'QUIP_PATH', 'LD_LIBRARY_PATH']:
    if var in os.environ:
        print(f"  {var} = {os.environ[var]}")
    else:
        print(f"  {var} = not set")
