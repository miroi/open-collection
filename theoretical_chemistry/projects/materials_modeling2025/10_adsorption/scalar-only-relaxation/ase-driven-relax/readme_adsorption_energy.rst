Hg@C8(graphene)
===============
python atom_relaxation_c_hg.py

Starting cell relaxation by ASE

Final results
  Total Energy                  : -5827.982600 eV
  ASE-style max force (norm)    : 0.003579 eV/Å
  QE-style max force            : 0.003579 eV/Å
  Pressure                      : -3.785504 kbar

Final relaxed structure saved to: final_relaxed_structure.vasp

graphene
~~~~~~~~~
python atom_relaxation_c.py

Starting cell relaxation by ASE

Final results
  Total Energy                  : -1311.600966 eV
  ASE-style max force (norm)    : 0.000005 eV/Å
  QE-style max force            : 0.000005 eV/Å
  Pressure                      : 0.516829 kbar

Final relaxed structure saved to: final_relaxed_structure.vasp

Hg addatom
~~~~~~~~~~
python hg_addatom.py

Running SCF calculation...
  Total energy: -4516.127513 eV
  Fermi level: -3.457900 eV


Final adsorption energy: 

Eads = E(Hg@C8)-E(C8)-E(Hg)
Eads =  -5827.982600 -( -1311.600966)-(-4516.127513)
Eads = -.254121 eV

Google AI:  Mercury's adsorption energy on pristine graphene is low (around -0.220 eV), indicating physisorption


