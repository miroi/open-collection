=========================
Quantum Espresso with ASE
=========================

miroi@MIRO:~/work/projects/open-collection/theoretical_chemistry/software/mopac/buildup_on_servers/wsl_win11_VictusNB/test_runs/ase-run/sole_mopac_run/.ase info --calculators espresso
Configuration
-------------

Loaded: /home/miroi/.config/ase/config.ini

espresso
  Name:     Quantum Espresso
  Import:   ase.calculators.espresso.EspressoTemplate
  Type:     GenericFileIOCalculator

  Configured by section [espresso]:
    command = mpiexec /usr/bin/pw.x
    pseudo_dir = /usr/share/espresso/pseudo



