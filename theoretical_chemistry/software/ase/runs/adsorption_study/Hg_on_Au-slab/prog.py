#
# try to calculate Hg on Au slab
#
from ase.build import bulk
from ase.calculators.emt import EMT
from ase.eos import calculate_eos
from ase.db import connect
from ase.build import fcc111, add_adsorbate

# open the database
#db = connect('bulk.db')

#for symb in ['Al', 'Ni', 'Cu', 'Pd', 'Ag', 'Pt', 'Au', 'Tl']:
#for symb in ['Al', 'Ni', 'Cu', 'Pd', 'Ag', 'Pt', 'Au']:
for symb in ['Au']:
#  https://en.wikipedia.org/wiki/Cubic_crystal_system
    atoms = bulk(symb, 'fcc')
#    atoms = bulk(symb, 'bcc')
    atoms.calc = EMT()

    eos = calculate_eos(atoms)
    v, e, B = eos.fit()  # find minimum

    # Do one more calculation at the minimum and write to database:
    atoms.cell *= (v / atoms.get_volume())**(1 / 3)
    a = row.cell[0, 1] * 2
    atoms.get_potential_energy()
    print(symb, 'fcc crystal energy:',atoms.get_potential_energy()
)
    #db.write(atoms, bm=B)

atoms = fcc111('Hg', (1, 1, 3), a=a)
add_adsorbate(atoms, ads, height=1.0, position='fcc')
#   print(symb," fcc111 lattice constant,  a=",a)

    # Constrain all atoms except the adsorbate:
fixed = list(range(len(atoms) - 1))
atoms.constraints = [FixAtoms(indices=fixed)]

atoms.calc = EMT()
opt = BFGS(atoms, logfile=None)
opt.run(fmax=0.01)
