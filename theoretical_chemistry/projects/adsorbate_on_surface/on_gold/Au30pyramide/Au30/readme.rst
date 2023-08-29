Au30 pyramide with NWChem
=========================

SLURM jobs sequentially:
https://chuckaknight.wordpress.com/2016/08/02/slurm-scheduling-so-they-run-sequentially

sbatch --dependency=singleton --job-name=Au30 virgo_slurm_nw.main_N4_npn36_geopt.01
sbatch --dependency=singleton --job-name=Au30 virgo_slurm_nw.main_N4_npn36_geopt_restart.01 


NOT good Au30 pyramide !!! need another cut...

