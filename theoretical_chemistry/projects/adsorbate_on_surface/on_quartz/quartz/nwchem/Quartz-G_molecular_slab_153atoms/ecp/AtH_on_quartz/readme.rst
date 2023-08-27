AtH@smallQ
=========

https://github.com/nwchemgit/nwchem/blob/master/src/basis/libraries/crenbl_ecp

SLURM jobs sequentially:
https://chuckaknight.wordpress.com/2016/08/02/slurm-scheduling-so-they-run-sequentially

permanent_dir /lustre/ukt/milias/scratch/AtH_on_quartz

sbatch --dependency=singleton --job-name=AtH@Q virgo_slurm_nw.main_N4_npn36_geopt.01
sbatch --dependency=singleton --job-name=AtH@Q virgo_slurm_nw.main_N4_npn36_geopt_restart.01 




