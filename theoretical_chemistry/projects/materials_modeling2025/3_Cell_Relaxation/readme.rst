


mpirun -np 8 /usr/bin/pw.x < cell_relaxation_si.in > cell_relaxation_si.logfile


grep 'total energy'   cell_relaxation_si.logfile_SAVED
