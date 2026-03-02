#
#  openbabel convert ase bulk to pybel atoms use periodic boundary condition code
# fix to cif

import io
from ase.build import bulk
from ase.io import write
from openbabel import pybel

# 1. Create the bulk structure
atoms = bulk('Au', 'fcc', a=4.08, cubic=True)

# 2. Convert to CIF using a BytesIO buffer
# ASE's CIF writer requires a binary file-like object
cif_buffer = io.BytesIO()
write(cif_buffer, atoms, format='cif')

# 3. Retrieve the string and read into Pybel
# We decode the bytes to a string for pybel.readstring
cif_string = cif_buffer.getvalue().decode('utf-8')
mol = pybel.readstring("cif", cif_string)

# 4. Verify PBC / Unit Cell and Atoms
if mol.unitcell:
    print("Success: Unit Cell and PBC preserved.")
    print(f"Lattice a: {mol.unitcell.GetA():.2f} Å")
    print(f"Total Atoms: {len(mol.atoms)}")

# 5. Optional: View with Pybel's 2D engine (if GUI available)
# mol.draw(show=True)

