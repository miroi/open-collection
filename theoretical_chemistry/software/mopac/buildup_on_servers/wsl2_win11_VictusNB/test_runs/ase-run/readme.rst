==============
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

see https://gitlab.com/ase/ase/-/issues/449#note_2144350344

miroi@MIRO:~/work/projects/open-collection/theoretical_chemistry/software/mopac/buildup_on_servers/wsl_win11_VictusNB/test_runs/ase-run/.ase info --calculators mopac

 Configuration
 -------------

Loaded: /home/miroi/.config/ase/config.ini

mopac
  Name:     MOPAC
  Import:   ase.calculators.mopac.MOPAC
  Type:     FileIOCalculator (legacy)

  Configured by section [mopac]:
    command = /opt/mopac/bin/mopac
    configvars = {}


