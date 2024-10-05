#
#  https://wiki.fysik.dtu.dk/ase/ase/calculators/mopac.html
#

from ase.build import molecule
from ase.calculators.mopac import MOPAC

atoms = molecule('O2')
atoms.calc = MOPAC(label='O2')

#atoms.get_potential_energy() # does not work with sudo installed ase
#eigs = atoms.calc.get_eigenvalues()
#somos = atoms.calc.get_somo_levels()
#homo, lumo = atoms.calc.get_homo_lumo_levels()
