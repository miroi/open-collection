
# https://www.ovito.org/manual/python/modules/ovito_io_ase.html

from ovito.pipeline import StaticSource, Pipeline
from ovito.io.ase import ase_to_ovito
from ase.atoms import Atoms

# The ASE Atoms object to convert:
ase_atoms = Atoms('CO', positions=[(0, 0, 0), (0, 0, 1.1)])

# Convert the ASE object to an OVITO DataCollection:
data = ase_to_ovito(ase_atoms)

# We may now create a Pipeline object with a StaticSource and use the 
# converted dataset as input for a data pipeline:
pipeline = Pipeline(source = StaticSource(data = data))


