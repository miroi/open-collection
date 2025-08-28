


mpirun -np 8 /usr/bin/pw.x < cell_relaxation_si.in > cell_relaxation_si.logfile


Getting the converged energies
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

grep 'total energy'   cell_relaxation_si.logfile_SAVED

grep '!    total energy'   cell_relaxation_si.logfile_SAVED
!    total energy              =     -16.92488384 Ry
!    total energy              =     -16.92516612 Ry
!    total energy              =     -16.92527469 Ry
!    total energy              =     -16.92527482 Ry
!    total energy              =     -16.92527497 Ry


milias@DESKTOP-7OTLCGO:~/work/git-projects/open-collection/theoretical_chemistry/projects/materials_modeling2025/3_Cell_Relaxation/.rconv.sh cell_relaxation_si.out
Energy and force convergence for vc-relax runs
------------------------------------
Cut off  Total Energy  Total Force
 (Ry)       (Ry)        (Ry/au)
------------------------------------
65.0000 -16.92488384 0.000000
65.0000 -16.92516612 0.000000
65.0000 -16.92527469 0.000000
65.0000 -16.92527482 0.000000
65.0000 -16.92527497 0.000000
------------------------------------


more strict thresholds
~~~~~~~~~~~~~~~~~~~~~~

Also slightly distorting atomic geometries 

milias@DESKTOP-7OTLCGO:~/work/git-projects/open-collection/theoretical_chemistry/projects/materials_modeling2025/3_Cell_Relaxation/.mpirun -np 10 /usr/bin/pw.x < cell_relaxation2_si.in > cell_relaxation2_si.out

milias@DESKTOP-7OTLCGO:~/work/git-projects/open-collection/theoretical_chemistry/projects/materials_modeling2025/3_Cell_Relaxation/.rconv.sh    cell_relaxation2_si.out
Energy and force convergence for vc-relax runs
------------------------------------
Cut off  Total Energy  Total Force
 (Ry)       (Ry)        (Ry/au)
------------------------------------
65.0000 -16.91933286 0.070850
65.0000 -16.92397126 0.033123
65.0000 -16.92503185 0.000669
65.0000 -16.92512884 0.001472
65.0000 -16.92522880 0.001004
65.0000 -16.92527348 0.000240
65.0000 -16.92527440 0.000172
65.0000 -16.92527481 0.000033
65.0000 -16.92527481 0.000016
65.0000 -16.92527481 0.000009
65.0000 -16.92527497 0.000009
65.0000 -16.92488384 0.000000
65.0000 -16.92516612 0.000000
65.0000 -16.92527469 0.000000
65.0000 -16.92527482 0.000000
65.0000 -16.92527497 0.000000
------------------------------------


