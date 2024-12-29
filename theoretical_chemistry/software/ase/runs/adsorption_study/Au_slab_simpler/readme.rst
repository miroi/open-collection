=======================
Au slab with Pt addatom
=======================

exp.data :  https://www.sciencedirect.com/science/article/pii/S0009261407006513
take Au(1 1 1) surface (Table 1)


WSL on own PC
~~~~~~~~~~~~~
python3 Pt_on_Au-slab.py
Au fcc crystal energy: -0.00013514121662172585  a= 4.056168091621226
energy of the Au slab = 0.47677295552592724
Pt single atom pot.energy = 5.85
energy of atom plus surface system : 0.6714933807144492
adsorption energy of Pt on Au fcc111 = -5.655279574811478

Govorun job
~~~~~~~~~~~
milias@hydra.jinr.ru:~/work/projects/open-collection/theoretical_chemistry/software/ase/runs/adsorption_study/Au_slab_simpler/.sbatch hydra_slurm_ase.01

