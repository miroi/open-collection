==============
LAMMPS example
==============

ls /usr/share/lammps/examples/peptide/

miroi@MIRO:~/work/projects/open-collection/theoretical_chemistry/software/lammps-ase/buildup_on_servers/wsl2/win11_VictusNB/tests/peptide/.ln -sf /usr/share/lammps/examples/peptide/data.peptide .

mpirun -np 4 lmp  -in   /usr/share/lammps/examples/peptide/in.peptide

miroi@MIRO:~/work/projects/open-collection/theoretical_chemistry/software/lammps-ase/buildup_on_servers/wsl2/win11_VictusNB/tests/peptide/.diff log.lammps /usr/share/lammps/examples/peptide/log.27Nov18.peptide.g++.1



