from ase.build import bulk
from ase.calculators.emt import EMT
from ase.eos import calculate_eos
from ase.db import connect

# open the database
dbfile='bulk.db'
db = connect(dbfile)

#for symb in ['Al', 'Ni', 'Cu', 'Pd', 'Ag', 'Pt', 'Au', 'Tl']:
for symb in ['Al', 'Ni', 'Cu', 'Pd', 'Ag', 'Pt', 'Au']:
#  https://en.wikipedia.org/wiki/Cubic_crystal_system
    atoms = bulk(symb, 'fcc')
#    atoms = bulk(symb, 'bcc')
    atoms.calc = EMT()

    eos = calculate_eos(atoms)
    v, e, B = eos.fit()  # find minimum

    # Do one more calculation at the minimum and write to database:
    atoms.cell *= (v / atoms.get_volume())**(1 / 3)
    atoms.get_potential_energy()
    print(symb, 'fcc crystal energy:',atoms.get_potential_energy()
)
    db.write(atoms, bm=B)

print('results written into database file ',dbfile)
