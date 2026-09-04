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

## Summary of All Files

| File | Description |
|------|-------------|
| `config_qe.yaml` | Configuration file |
| `main.py` | Main entry point |
| `config_loader.py` | Configuration loading |
| `utils.py` | Utility functions |
| `calculator.py` | QE calculator setup |
| `vibration.py` | Vibration calculation methods |
| `analysis.py` | Molecule analysis |
| `io_utils.py` | Results saving and comparison |
| `requirements.txt` | Python dependencies |
| `README.md` | Documentation |

**To run the code:**
```bash
pip install -r requirements.txt
python main.py
