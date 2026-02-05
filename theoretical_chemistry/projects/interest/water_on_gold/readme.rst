=========================
Water on the gold surface
=========================

Testing positions of the water molecule on the gold surface using fast interatomic potential (IP) method in ASE.

Program automatically checks all positions of the adsorbate (water molecule) on the gold surface.

run the code
------------
source ~/work/software/myenv/bin/activate

(myenv) miroi@MIRO:~/work/projects/open-collection/theoretical_chemistry/projects/interest/theme/.python ase_adsorption_finder_mol.py > ase_adsorption_finder_mol.py_logfile 2>&1

after finishing the job
~~~~~~~~~~~~~~~~~~~~~~~~

check adsorption_summary.txt, ase_outputs/, traj_files/ , vasp_outputs/


display trajectory
~~~~~~~~~~~~~~~~~~
ase gui traj_files/H2O_hollow_27-36-39_rot060.traj


