==========
LAMMPS run
==========

lammps_stable/examples/melt:
~~~~~~~~~~~~~~~~~~~~~~~~~~~~


Kronos (GSI.de) - run OK

grid.umb.sk - run OK (see also https://github.com/open-mpi/ompi/issues/6981)

labs.fpv.umb.sk - run OK

bash.01 - universal script for interactive runs on labs,notebook


On Victus Mirov NB
~~~~~~~~~~~~~~~~~~
mpirun -np 4 lmp -in in.melt
