# Check_quip_installation.py
import sys
print(f"Python version: {sys.version}")
print(f"Python path: {sys.path}")

# Try to find quippy
try:
    import quippy
    print(f"quippy found at: {quippy.__file__}")
    print(f"quippy version: {getattr(quippy, '__version__', 'unknown')}")
    print(f"quippy attributes: {dir(quippy)}")
except ImportError as e:
    print(f"quippy not found: {e}")

# Try to find ase.calculators
try:
    import ase.calculators
    print(f"ase.calculators found at: {ase.calculators.__file__}")
    print(f"Available calculators: {[c for c in dir(ase.calculators) if not c.startswith('_')]}")
except ImportError as e:
    print(f"ase.calculators not found: {e}")

# Try specific imports
for module in ['ase.calculators.quip', 'ase.calculators.quipty', 'quipty']:
    try:
        exec(f"import {module}")
        print(f"✓ {module} found")
    except ImportError:
        print(f"✗ {module} not found")
