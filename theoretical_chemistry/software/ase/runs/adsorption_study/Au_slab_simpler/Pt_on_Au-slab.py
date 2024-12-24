#
# try to calculate adsorption energy of Pt on Au slab
#
# see https://www.sciencedirect.com/science/article/pii/S0009261407006513
#
from ase import Atoms
from ase.build import bulk
from ase.calculators.emt import EMT
from ase.eos import calculate_eos
from ase.db import connect
from ase.build import fcc111, add_adsorbate
from ase.constraints import FixAtoms
from ase.optimize import BFGS

#for symb in ['Al', 'Ni', 'Cu', 'Pd', 'Ag', 'Pt', 'Au']:
symb='Au'
#  https://en.wikipedia.org/wiki/Cubic_crystal_system
atoms = bulk(symb,'fcc')
atoms.calc = EMT()
eos = calculate_eos(atoms)
v, e, B = eos.fit()  # find minimum

# Do one more calculation at the minimum 
atoms.cell *= (v / atoms.get_volume())**(1 / 3)
a = atoms.cell[0, 1] * 2
atoms.get_potential_energy()
print(symb, 'fcc crystal energy:',atoms.get_potential_energy(), ' a=',a)

n = 3;
atoms = fcc111(symb, (1, 1, n), a=a)
atoms.calc=EMT()
atoms.get_forces()
en_slab = atoms.get_potential_energy()
print('energy of the Au slab =',en_slab)


add_atom='Pt'
#add_atom='C' # this is veryfied with program (-3.547)
a1=Atoms(add_atom)
a1.calc = EMT()
en_atom=a1.get_potential_energy()
print(a1.symbols,'single atom pot.energy =',en_atom)

add_adsorbate(atoms, add_atom, height=1.0, position='fcc')
# Constrain all atoms except the adsorbate:
fixed = list(range(len(atoms) - 1))
atoms.constraints = [FixAtoms(indices=fixed)]

atoms.calc = EMT()
opt = BFGS(atoms, logfile=None)
opt.run(fmax=0.01)
en_atom_on_surface=atoms.get_potential_energy()

#print('atoms ', atoms)
print('energy of atom plus surface system :',en_atom_on_surface)

en_ads = en_atom_on_surface - en_atom - en_slab
print('adsorption energy of Pt on Au fcc111 =', en_ads)

