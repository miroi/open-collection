#
#  https://wiki.fysik.dtu.dk/ase/ase/thermochemistry/thermochemistry.html#id2
#

from ase.calculators.emt import EMT
from ase.build import fcc100, add_adsorbate
from ase.optimize import QuasiNewton
from ase.phonons import Phonons
from ase.vibrations import Vibrations
from ase.spacegroup import crystal
from ase.thermochemistry import (IdealGasThermo, HarmonicThermo,
                                 CrystalThermo, HinderedThermo)

atoms = fcc100('Cu', (2, 2, 2), vacuum=10.0)
atoms.calc = EMT()
add_adsorbate(atoms, 'Pt', 1.5, 'hollow')

calc = EMT()
atoms.calc = calc
qn = QuasiNewton(atoms)
qn.run(fmax=0.05)
potentialenergy = atoms.get_potential_energy()

vib = Vibrations(atoms, name='harmonicthermo-vib',
                 indices=[atom.index for atom in atoms
                         if atom.symbol != 'Cu'])
vib.run()
vib.summary()
vib_energies = vib.get_energies()

thermo = HarmonicThermo(vib_energies=vib_energies,
                        potentialenergy=atoms.get_potential_energy())
thermo.get_helmholtz_energy(temperature=298.15)
