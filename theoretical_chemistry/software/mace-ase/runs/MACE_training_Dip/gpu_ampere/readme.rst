===========================
MACE training on GPU ampere
===========================

see https://claude.ai/share/b793c9dc-eed8-49bc-a343-9d83d3d59626

github
~~~~~~
https://github.com/dipayanster/MatScProjects/tree/main/MLIP_training_tutorial/MACE_training

source /lustre/projects/m/milias/work/software/mace_volta_venv/bin/activate
mace_run_train --config="mace_config.yaml"

train at volta gpu
------------------
sbatch slurm_govorun_ampere.01

files after training
--------------------
milias@hydra.jinr.ru:/lustre/projects/m/milias/work/git-projects/open-collection/theoretical_chemistry/software/mace-ase/runs/MACE_training_Dip/gpu_ampere/.ls -lt
total 30985
-rw-r--r--. 1 milias hybrilit  277278 Nov 25 06:59 SAVED_log_slurm_job.2999829.ampere01.std_out_err
drwxr-xr-x. 2 milias hybrilit   11264 Nov 25 06:59 results/
-rw-r--r--. 1 milias hybrilit 7666855 Nov 25 06:59 MACE_GrapheneHg_stagetwo_compiled.model
-rw-r--r--. 1 milias hybrilit 7554557 Nov 25 06:59 MACE_GrapheneHg_stagetwo.model
drwxr-xr-x. 2 milias hybrilit   11264 Nov 25 06:59 checkpoints/
-rw-r--r--. 1 milias hybrilit 7649829 Nov 25 06:59 MACE_GrapheneHg_compiled.model
-rw-r--r--. 1 milias hybrilit 7552897 Nov 25 06:59 MACE_GrapheneHg.model
-rw-r--r--. 1 milias hybrilit      45 Nov 25 06:39 MACE_GrapheneHg_valid_indices_123.txt
drwxr-xr-x. 2 milias hybrilit   11264 Nov 25 06:39 logs/
-rw-r--r--. 1 milias hybrilit    4135 Nov 25 06:34 slurm_govorun_ampere.01
-rw-r--r--. 1 milias hybrilit     448 Nov 25 06:28 readme.rst
drwxr-xr-x. 4 milias hybrilit   11264 Nov 25 06:25 MACE_calculations/
drwxr-xr-x. 2 milias hybrilit   11264 Nov 25 06:25 training_dataset/
-rw-r--r--. 1 milias hybrilit    1705 Nov 25 06:25 mace_config.yaml
