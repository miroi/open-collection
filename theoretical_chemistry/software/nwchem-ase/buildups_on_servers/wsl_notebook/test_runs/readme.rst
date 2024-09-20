========================
nwchem package test runs
========================

files
~~~~~~~
ls /usr/share/doc/nwchem/examples/
ls  /usr/share/nwchem/


runs
~~~~~

milias@Miro:/mnt/c/Users/miroi/OneDrive/Desktop/Work/projekty/open-collection/theoretical_chemistry/software/nwchem/buildups_on_servers/wsl_notebook/test_runs/.nwchem  /usr/share/doc/nwchem/examples/h2o.nw > h2o.out

milias@Miro:/mnt/c/Users/miroi/OneDrive/Desktop/Work/projekty/open-collection/theoretical_chemistry/software/nwchem/buildups_on_servers/wsl_notebook/test_runs/.mpirun -np 2 nwchem.openmpi /usr/share/doc/nwchem/examples/h2o.nw > h2o.out2


