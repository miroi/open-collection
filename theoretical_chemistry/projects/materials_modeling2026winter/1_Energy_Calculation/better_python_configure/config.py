#
#  Adjust these variables for your QE run
#

# full path to your QE binaries (pw.x, pp.x etc)
#qe_path="/opt/espresso/7.5"
qe_path=...

# for OpenMP parallelization, if active,OMP_NUM_THREADS envirovariable
#omp_threads="2"

# set up our own command for the parallel runa

mpi_command="mpirun -np 2"
