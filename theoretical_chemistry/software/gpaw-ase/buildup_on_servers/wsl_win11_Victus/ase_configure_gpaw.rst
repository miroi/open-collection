configure gpaw
==============


vim ~/.config/ase/config.ini

[gpaw]
command = mpiexec gpaw


ase test  --help-calculators


milias@Miro:~/work/software/gpaw-datasets/.gpaw install-data .
Available setups and pseudopotentials
  [*] https://wiki.fysik.dtu.dk/gpaw-files/gpaw-setups-24.1.0.tar.gz
      https://wiki.fysik.dtu.dk/gpaw-files/gpaw-setups-0.9.20000.tar.gz
      https://wiki.fysik.dtu.dk/gpaw-files/gpaw-setups-0.9.11271.tar.gz
      https://wiki.fysik.dtu.dk/gpaw-files/gpaw-setups-0.9.9672.tar.gz
      https://wiki.fysik.dtu.dk/gpaw-files/gpaw-setups-0.8.7929.tar.gz
      https://wiki.fysik.dtu.dk/gpaw-files/gpaw-setups-0.6.6300.tar.gz
      https://wiki.fysik.dtu.dk/gpaw-files/gpaw-setups-0.5.3574.tar.gz

Selected gpaw-setups-24.1.0.tar.gz.  Downloading...
Extracting tarball into .
Setups installed into /home/milias/work/software/gpaw-datasets/gpaw-setups-24.1.0.
Register this setup path in /home/milias/.gpaw/rc.py? [y/n] y
Setup path registered in /home/milias/.gpaw/rc.py.
Current GPAW setup paths in order of search priority:
   1. /home/milias/work/software/gpaw-datasets/gpaw-setups-24.1.0
Installation complete.
milias@Miro:~/work/software/gpaw-datasets/.

