#!/usr/bin/env python3
"""
Debug script to inspect the CIF file structure
"""

with open('ja030260r_2.cif', 'r') as f:
    lines = f.readlines()

print("CIF File Structure Analysis")
print("="*60)

# Find all loop_ statements
print("\n1. Loop statements found:")
for i, line in enumerate(lines):
    if 'loop_' in line:
        print(f"  Line {i}: {line.strip()[:50]}...")

# Find atom_site sections
print("\n2. Atom_site sections:")
for i, line in enumerate(lines):
    if '_atom_site' in line:
        print(f"  Line {i}: {line.strip()}")

# Look for atom data lines
print("\n3. Looking for atom data lines:")
for i in range(len(lines)):
    line = lines[i].strip()
    if line and not line.startswith('_') and not line.startswith('#') and not line.startswith(';'):
        # Check if it looks like atom data
        parts = line.split()
        if len(parts) >= 5 and parts[0][0].isalpha():
            print(f"  Line {i}: {line[:60]}...")

# Show the atom_site loop section
print("\n4. Atom_site loop section:")
in_loop = False
for i, line in enumerate(lines):
    if '_atom_site_label' in line:
        in_loop = True
        print(f"  Line {i}: {line.strip()}")
    elif in_loop and line.strip() and not line.startswith('_'):
        if line.strip().startswith('U') or line.strip().startswith('I') or line.strip().startswith('O'):
            print(f"  Line {i}: {line.strip()}")
        elif len(line.strip()) > 10:  # Most data lines are long
            print(f"  Line {i}: {line.strip()[:60]}...")
