==========================
ASE-GPAW on lx-pool.gsi.de
==========================

milias@lxi099.gsi.de:~/Work/qch/projects/open-collection/theoretical_chemistry/software/ase/servers/gsi_de/lx-pool_gsi_de/.python3 -m pip install gpaw
Successfully built gpaw
Installing collected packages: scipy, gpaw
Successfully installed gpaw-23.6.1 scipy-1.7.3

You need to set the GPAW_SETUP_PATH environment variable to point to
the directories where PAW dataset and basis files are stored.  See
https://wiki.fysik.dtu.dk/gpaw/install.html#install-paw-datasets
for details.

milias@lxi099.gsi.de:~/Work/qch/projects/open-collection/theoretical_chemistry/software/ase/servers/gsi_de/lx-pool_gsi_de/.gpaw install-data .
--------------------------------------------------------------------------
[[54358,1],0]: A high-performance Open MPI point-to-point messaging module
was unable to find any relevant network interfaces:

Module: OpenFabrics (openib)
  Host: lxi099

Another transport will be used instead, although this may result in
lower performance.

NOTE: You can disable this warning by setting the MCA parameter
btl_base_warn_component_unused to 0.
--------------------------------------------------------------------------
Available setups and pseudopotentials
  [*] https://wiki.fysik.dtu.dk/gpaw-files/gpaw-setups-0.9.20000.tar.gz
      https://wiki.fysik.dtu.dk/gpaw-files/gpaw-setups-0.9.11271.tar.gz
      https://wiki.fysik.dtu.dk/gpaw-files/gpaw-setups-0.9.9672.tar.gz
      https://wiki.fysik.dtu.dk/gpaw-files/gpaw-setups-0.8.7929.tar.gz
      https://wiki.fysik.dtu.dk/gpaw-files/gpaw-setups-0.6.6300.tar.gz
      https://wiki.fysik.dtu.dk/gpaw-files/gpaw-setups-0.5.3574.tar.gz

Selected gpaw-setups-0.9.20000.tar.gz.  Downloading...
Extracting tarball into .
Setups installed into /u/milias/Work/qch/projects/open-collection/theoretical_chemistry/software/ase/servers/gsi_de/lx-pool_gsi_de/gpaw-setups-0.9.20000.
Register this setup path in /u/milias/.gpaw/rc.py? [y/n] y
Setup path registered in /u/milias/.gpaw/rc.py.
Current GPAW setup paths in order of search priority:
   1. /u/milias/Work/qch/projects/open-collection/theoretical_chemistry/software/ase/servers/gsi_de/lx-pool_gsi_de/gpaw-setups-0.9.20000
Installation complete.


milias@lxi099.gsi.de:~/Work/qch/projects/open-collection/theoretical_chemistry/software/ase/servers/gsi_de/lx-pool_gsi_de/.gpaw test
Doing a test calculation (cores: 1): ... Done

milias@lxi099.gsi.de:~/Work/qch/projects/open-collection/theoretical_chemistry/software/ase/servers/gsi_de/lx-pool_gsi_de/.gpaw -P 4 test





