===============
Fl2 with QE-XDM
===============


WSL2-Win11-NB
~~~~~~~~~~~~~~
miroi@MIRO:~/work/projects/open-collection/theoretical_chemistry/software/quantum-espresso-ase/runs/xdm_tests/Fl2/.mpirun -np 2 ~/work/software/quantum_espresso/q-e/build_gnu_openmpi/bin/pw.x <   Fl2.scfso_xdm.in


WSL2-Win10-PC
~~~~~~~~~~~~~
nohup mpirun -np  8  /home/milias/work/software/qe/q-e/build_gnu_openmpi/bin/pw.x < Fl2.scfso_xdm.in > logfile & 

milias@DESKTOP-7OTLCGO:~/work/git-projects/open-collection/theoretical_chemistry/software/quantum-espresso-ase/runs/xdm_tests/Fl2/.nohup mpirun -np 8  /home/milias/work/software/qe/q-e/build_gnu_openmpi/bin/pw.x < Fl2.scfso.in >  Fl2.scfso.logfile  &

  nohup mpirun -np 8 /home/milias/work/software/qe/q-e/build_gnu_openmpi/bin/pw.x < Fl2.scfso_xdm.in > Fl2.scfso_xdm.logfile &

Govorun
~~~~~~~
~
