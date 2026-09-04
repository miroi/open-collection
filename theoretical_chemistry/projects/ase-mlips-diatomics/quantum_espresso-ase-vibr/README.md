# Diatomic Molecule Analysis with Quantum ESPRESSO

## Description
This package performs geometry optimization and vibrational frequency calculations for diatomic molecules using Quantum ESPRESSO through the ASE interface.

## Features
- Geometry optimization with BFGS
- Three vibrational frequency calculation methods:
  - 1D Scan (fastest)
  - X-Only Hessian (accurate, only along bond)
  - Full 3D Hessian (most accurate, slow)
- Comparison with experimental (NIST) reference values
- Multiple molecule support
- MPI parallelization support

## File Structure