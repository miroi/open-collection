=======================
Au slab with Pt addatom
=======================

exp.data :  https://www.sciencedirect.com/science/article/pii/S0009261407006513
take Au(1 1 1) surface (Table 1)

experimental data: https://sci-hub.ru/10.1021/jp5033228 ( https://doi.org/10.1021/jp5033228 )


WSL2 on own PC
---------------
python3 Pt_on_Au-slab.py
Au fcc crystal energy: -0.00013514121662172585  a= 4.056168091621226
energy of the Au slab = 0.47677295552592724
Pt single atom pot.energy = 5.85
energy of atom plus surface system : 0.6714933807144492
adsorption energy of Pt on Au fcc111 = -5.655279574811478

miroi@MiroPhenomII-X6:~/work/git-projects/open-collection/theoretical_chemistry/software/ase/runs/adsorption_study/Au_slab_simpler/.python  Pt_on_Au-slab.py
Au fcc crystal energy: -0.00013514121662172585  a= 4.056168091621226
energy of the Au slab = 0.47677295552592724
Pt single atom pot.energy = 5.85
energy of atom plus surface system : 0.6714933807144492
adsorption energy of Pt on Au fcc111 = -5.655279574811478 (exp. cca -4.8 eV)


Govorun job
~~~~~~~~~~~
milias@hydra.jinr.ru:~/work/projects/open-collection/theoretical_chemistry/software/ase/runs/adsorption_study/Au_slab_simpler/.sbatch hydra_slurm_ase.01


display trajectory
~~~~~~~~~~~~~~~~~~
milias@vm01.hydra.local:~/work/projects/open-collection/theoretical_chemistry/software/ase/runs/adsorption_study/Au_slab_simpler/.ase gui Pt_on_Au-slab.traj

(venv) miroi@MiroPhenomII-X6:~/work/git-projects/open-collection/theoretical_chemistry/software/ase/runs/adsorption_study/Au_slab_simpler/.ase gui Pt_on_Au-slab.traj


