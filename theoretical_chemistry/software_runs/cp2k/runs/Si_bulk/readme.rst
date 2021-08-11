Si bulk with CP2K
=================

see https://www.cp2k.org/howto:static_calculation

do "wget https://www.cp2k.org/_media/static_calculation.tgz"

mpirun -n 2 cp2k.popt -o Si_bulk8.out Si_bulk8.inp &
