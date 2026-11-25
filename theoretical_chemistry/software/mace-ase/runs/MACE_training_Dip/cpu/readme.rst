=============
MACE training
=============

see https://claude.ai/share/b793c9dc-eed8-49bc-a343-9d83d3d59626

github
~~~~~~
https://github.com/dipayanster/MatScProjects/tree/main/MLIP_training_tutorial/MACE_training

source /lustre/projects/m/milias/work/software/mace_cpu_venv/bin/activate
mace_run_train --config="mace_config.yaml"

train at cpu node 
------------------
sbatch slurm_govorun_cpu.01

files after training
--------------------
