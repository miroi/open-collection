from ase.build import molecule
from ase.parallel import paropen
from gpaw import GPAW

a = 8.0
h = 0.2

energies = {}
with open(f'results-{h:.2f}.txt', 'w') as resultfile:

    for name in ['H2O', 'H', 'O']:
        system = molecule(name)
        system.set_cell((a, a, a))
        system.center()

        if name in ['H', 'O']:
            hund = True
        else:
            hund = False
        calc = GPAW(h=h, hund=hund,
                    txt=f'gpaw-{name}-{h:.2f}.txt')
    
        system.calc = calc
    
        energy = system.get_potential_energy()
        energies[name] = energy
        print(name, energy, file=resultfile)
    
    e_atomization = energies['H2O'] - 2 * energies['H'] - energies['O']
    print(e_atomization, file=resultfile)
