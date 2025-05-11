=============
Pb2 with Q.E.
=============

milias@DESKTOP-7OTLCGO:~/work/git-projects/open-collection/theoretical_chemistry/software/quantum-espresso-ase/runs/xdm_tests/Pb2/. nohup mpirun -np 8 /home/milias/work/software/qe/q-e/build_gnu_openmpi/bin/pw.x < Pb2.scfso.in >  Pb2.scfso.logfile_SAVED &

milias@DESKTOP-7OTLCGO:~/work/git-projects/open-collection/theoretical_chemistry/software/quantum-espresso-ase/runs/xdm_tests/Pb2/xdm/.nohup mpirun -np 8 /home/milias/work/software/qe/q-e/build_gnu_openmpi/bin/pw.x < Pb2.scfso_xdm.in >  Pb2.scfso_xdm.logfile_SAVED &

milias@DESKTOP-7OTLCGO:~/work/git-projects/open-collection/theoretical_chemistry/software/quantum-espresso-ase/runs/xdm_tests/Pb2/other_vdw_corr/.nohup mpirun -np 8 /home/milias/work/software/qe/q-e/build_gnu_openmpi/bin/pw.x <  Pb2.scfso_vdw.in &


SOSCF energy:     -280.64032113 Ry

SOSCF+DFT-D3:     -280.64087939 Ry
DFT-D3 Dispersion   -0.00055826 Ry

SOSCF+TS:                -280.64060228 Ry
Dispersion Correction      -0.00027095 Ry

SOSCF+MBD:            -280.64037018 Ry
Dispersion Correction      -0.00003886 Ry

