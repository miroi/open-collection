# Example of the use of the ASE interface
# 20-1-2025, L. Visscher
from ase import Atoms
from ase.build import molecule
from ase.units import Ha
from ase_dirac import DIRAC

# Some simple small molecules taken from the G2 set in the ASE database
#molecules = ['H2O','N2','F2','Cl2','CH4','C2H4']
molecules = ['H2O']
# Defines the **HAMILTONIAN input block, note that two lines input for the full DCG Hamiltonian
#hamiltonian_inputs = ['.nonrel','.x2cmmf','.gaunt\n.dossss']
hamiltonian_inputs = ['.nonrel']
# Labeling the different inputs with a descriptive string
#calculation_labels = ['NR-MP2','X2Cmmf-MP2','DCG-MP2']
calculation_labels = ['NR-MP2']
# Making an empty list to store results (energies) for each molecule
results = []

# Outermost loop over different molecules
for mol in molecules:
    ase_molecule = molecule(mol)
    energy = []
    # Loop over the three different Hamiltonians that we consider
    for ham, calc in zip(hamiltonian_inputs,calculation_labels):
        label=calc+'_'+mol
        try:
            ase_molecule.calc = DIRAC(
              hamiltonian={ham: ''},
              wave_function={'.scf': '', '.mp2': '',
                             '*scf': {'.ergcnv': '1.E-8 1.E-6',
                                      '.maxitr': '35'},
                             '*mp2cal': {'.occup': 'all','.virtual': 'all'},
                            },
              molecule={'*basis': {'.default': 'cc-pVDZ'}},
              label=label)
            energy.append(ase_molecule.get_potential_energy() / Ha)
        except:
            print (f'Calculation {label} could not be run correctly, please check')
            energy.append(0)
    results.append(energy)
    
# Print results in a table
#print(' Møller-Plesset second order (MP2) energies computed with different Hamiltonians\n')
#print(80*'-')
#print('  {:<15} {:>20} {:>20} {:>20}'.format('Molecule',*calculation_labels))
#print(80*'-')
for mol, result in zip(molecules,results):
#    print ('  {:<15} {:>20.8f} {:>20.8f} {:>20.8f}'.format(mol,*result))
   # print(mol, result)

    print('mol=',mol)
    print('result=',result)

#print(80*'-')

