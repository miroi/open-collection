#
#  https://wiki.fysik.dtu.dk/ase/ase/calculators/mopac.html
#

from ase.build import molecule
from ase.calculators.mopac import MOPAC

atoms = molecule('O2')
atoms.calc = MOPAC(label='O2')

print("O2 MOPAC energy :",atoms.get_potential_energy() )

eigs = atoms.calc.get_eigenvalues()
print("O2 MOPAC eigs:", eigs)

somos = atoms.calc.get_somo_levels()
print("O2 MOPAC somos:", somos)


homo, lumo = atoms.calc.get_homo_lumo_levels()

print("O2 MOPAC  homo, lumo", homo, lumo)

