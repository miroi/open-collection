


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
