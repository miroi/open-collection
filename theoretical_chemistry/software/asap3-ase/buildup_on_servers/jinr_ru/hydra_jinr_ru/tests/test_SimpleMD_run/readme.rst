========
SimpleMD
========

https://asap3.readthedocs.io/en/latest/examples/Simple_molecular_dynamics_simulation.html#simple-molecular-dynamics-simulation

interactive run
---------------
milias@hydra.jinr.ru:~/work/projects/open-collection/theoretical_chemistry/software/asap3-ase/buildup_on_servers/jinr_ru/hydra_jinr_ru/test_SimpleMD_run/.python SimpleMD.py > SimpleMD.py_logfile
/lustre/home/user/m/milias/work/projects/open-collection/theoretical_chemistry/software/asap3-ase/buildup_on_servers/jinr_ru/hydra_jinr_ru/test_SimpleMD_run/SimpleMD.py:25: FutureWarning: Please use atoms.calc = calc
  atoms.set_calculator(EMT())
Using Asap-optimized Verlet algorithm


run in batch
-------------
sbatch hydra_slurm_asap3.01

see log_slurm_job.8949516.n02p065.std_out_err_SAVED



