==================
Si cell relaxation
==================

direct QE run
-------------
mpirun -np 2 /opt/espresso/7.5/pw.x < cell_relaxation_si.in  > cell_relaxation_si.out

(venv) milias@DESKTOP-7OTLCGO:~/work/projects/open-collection/theoretical_chemistry/projects/materials_modeling2026winter/3_Cell_Relaxation/reference_outputs/step1/.../../../rconv.sh
Energy and force convergence for vc-relax runs
------------------------------------
Cut off  Total Energy  Total Force
 (Ry)       (Ry)        (Ry/au)
------------------------------------
65.0000 -16.92488384 0.000000
65.0000 -16.92516612 0.000000
65.0000 -16.92527468 0.000000
65.0000 -16.92527482 0.000000
65.0000 -16.92527497 0.000000
------------------------------------


ASE driven QE run
-----------------
..


