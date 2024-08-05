=======================
Equation of state (EOS)
=======================

https://wiki.fysik.dtu.dk/ase/tutorials/eos/eos.html

First, do a bulk calculation for different lattice constants:

milias@Miro:/mnt/c/Users/miroi/OneDrive/Desktop/Work/projekty/open-collection/theoretical_chemistry/software/ase/runs/eos/.python3 bulk_calc.py
milias@Miro:/mnt/c/Users/miroi/OneDrive/Desktop/Work/projekty/open-collection/theoretical_chemistry/software/ase/runs/eos/.ls
Ag.traj*  bulk_calc.py*  plot_traj.py*  readme.rst*

This will write a trajectory file containing five configurations of FCC silver for five different lattice constants. Now, analyse the result with the EquationOfState class and this script:a

milias@Miro:/mnt/c/Users/miroi/OneDrive/Desktop/Work/projekty/open-collection/theoretical_chemistry/software/ase/runs/eos/.python3 plot_traj.py
100.1418924197427 GPa


A quicker way to do this analysis, is to use the ase.gui tool:

$ ase gui Ag.traj


