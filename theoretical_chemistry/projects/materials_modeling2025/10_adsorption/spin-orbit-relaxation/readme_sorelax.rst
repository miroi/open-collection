===========
Hg@graphene
===========


full relativistic pseudos from https://github.com/PseudoDojo/ONCVPSP-PBE-FR-PDv0.4/tree/master

ase-driven relaxation
~~~~~~~~~~~~~~~~~~~~~

(myenv) miroi@MIRO:~/work/projects/open-collection/theoretical_chemistry/projects/materials_modeling2025/10_adsorption/spin-orbit-relaxation/.python atom_so-relaxation_c_hg.py

Starting cell relaxation by ASE

Final results
  Total Energy                  : -5852.075294 eV
  ASE-style max force (norm)    : 0.005897 eV/Å
  QE-style max force            : 0.005897 eV/Å
  Pressure                      : 0.603621 kbar

Final relaxed structure saved to: final_relaxed_structure.vasp

Relaxation complete


milias@DESKTOP-7OTLCGO
~~~~~~~~~~~~~~~~~~~~~~
milias@DESKTOP-7OTLCGO:~/work/git-projects/open-collection/theoretical_chemistry/projects/materials_modeling2025/10_adsorption/spin-orbit-relaxation/ase_driven_relax/.python atom_so-relaxation_c_hg.py

Starting cell relaxation by ASE

Final results
  Total Energy                  : -5852.075390 eV
  ASE-style max force (norm)    : 0.000555 eV/Å
  QE-style max force            : 0.000555 eV/Å
  Pressure                      : 0.603621 kbar

Final relaxed structure saved to: final_relaxed_structure.vasp

Relaxation complete

qe-driven relaxation
~~~~~~~~~~~~~~~~~~~~
-430.1196442627 Ry ... -5852.0805542 eV

better precision:
-430.1196454044 Ry ... -5852.0805698 eV 

diff (Num-Anal) = -5852.075390 -(-5852.0805698) = .0051798 eV
