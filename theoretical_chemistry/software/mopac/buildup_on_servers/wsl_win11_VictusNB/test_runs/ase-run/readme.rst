MOPAC with ASE
==============

see https://wiki.fysik.dtu.dk/ase/ase/calculators/calculators.html#calculator-configuration

~/.config/ase/config.ini

[abinit]
command = mpiexec /usr/bin/abinit
pp_paths = /usr/share/abinit/psp

[espresso]
command = mpiexec /usr/bin/pw.x
pseudo_path = /usr/share/espresso/pseudo/

[mopac]
command =  /opt/mopac/bin/mopac

