At@smallQ
=========

At library lanl2dz_ecp does not exists 

using
https://github.com/nwchemgit/nwchem/blob/master/src/basis/libraries/crenbl_ecp

added total memory 180gb, according to SBATCH script mem setting

not converging again, use another starting geometry, plus tweak rodft and odft
rodft NOT converging, using only odft

SLURM jobs sequentially:
https://chuckaknight.wordpress.com/2016/08/02/slurm-scheduling-so-they-run-sequentially

permanent_dir /lustre/ukt/milias/scratch/At-odft_on_quartz

sbatch --dependency=singleton --job-name=At@Q virgo_slurm_nw.main_N4_npn36_geopt.01
sbatch --dependency=singleton --job-name=At@Q virgo_slurm_nw.main_N4_npn36_geopt_restart.01 


