=============
MACE training
=============

see https://claude.ai/share/b793c9dc-eed8-49bc-a343-9d83d3d59626

github
~~~~~~
https://github.com/dipayanster/MatScProjects/tree/main/MLIP_training_tutorial/MACE_training

source /lustre/projects/m/milias/work/software/mace_volta_venv/bin/activate
mace_run_train --config="mace_config.yaml"

train at volta gpu
------------------
sbatch slurm_govorun_volta.01

files after training
--------------------
milias@hydra.jinr.ru:/lustre/projects/m/milias/work/git-projects/open-collection/theoretical_chemistry/software/mace-ase/runs/MACE_training_Dip/gpu_volta/.ls -lt
total 33020
-rw-r--r--. 1 milias hybrilit  271154 Nov 25 00:49 SAVED_log_slurm_job.2996143.dgx02.std_out_err
drwxr-xr-x. 2 milias hybrilit   11264 Nov 25 00:49 results/
-rw-r--r--. 1 milias hybrilit 7666791 Nov 25 00:49 MACE_GrapheneHg_stagetwo_compiled.model
-rw-r--r--. 1 milias hybrilit 7554429 Nov 25 00:49 MACE_GrapheneHg_stagetwo.model
drwxr-xr-x. 2 milias hybrilit   11264 Nov 25 00:49 checkpoints/
-rw-r--r--. 1 milias hybrilit 7649765 Nov 25 00:49 MACE_GrapheneHg_compiled.model
-rw-r--r--. 1 milias hybrilit 7552705 Nov 25 00:49 MACE_GrapheneHg.model
-rw-r--r--. 1 milias hybrilit      45 Nov 25 00:33 MACE_GrapheneHg_valid_indices_123.txt
drwxr-xr-x. 2 milias hybrilit   11264 Nov 25 00:33 logs/
-rw-r--r--. 1 milias hybrilit     316 Nov 25 00:32 readme.rst
-rw-r--r--. 1 milias hybrilit    3937 Nov 25 00:30 slurm_govorun_volta.01
drwxr-xr-x. 4 milias hybrilit   11264 Nov 24 23:10 MACE_calculations/
-rw-r--r--. 1 milias hybrilit    1705 Nov 24 23:10 mace_config.yaml
drwxr-xr-x. 2 milias hybrilit   11264 Nov 24 23:10 training_dataset/
