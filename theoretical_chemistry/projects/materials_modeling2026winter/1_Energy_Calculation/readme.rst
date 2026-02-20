Si crystal
==========

saved as vasp, cartesian coordinates

provide Si.upf

direct QE run
-------------
mpirun -np 2 /opt/espresso/7.5/pw.x < Si.in > Si.out

ASE driven QE run
-----------------
(venv) milias@DESKTOP-7OTLCGO:~/work/projects/open-collection/theoretical_chemistry/projects/materials_modeling2026winter/1_Energy_Calculation/.python si_ase.py

Running SCF calculation...
  Total energy: -227.711622 eV

