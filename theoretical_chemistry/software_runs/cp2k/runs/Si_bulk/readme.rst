Si bulk with CP2K
=================

see https://www.cp2k.org/howto:static_calculation

do "wget https://www.cp2k.org/_media/static_calculation.tgz"

Run
----
mpirun -n 4  cp2k.popt -o Si_bulk8.out Si_bulk8.inp &

milias@labs.fpv.umb.sk:~/work/open-collection/theoretical_chemistry/software_runs/cp2k/runs/Si_bulk/.ls
BASIS_SET  GTH_POTENTIALS  readme.rst  Si_bulk8.inp  Si_bulk8.out  Si_bulk8-RESTART.wfn




