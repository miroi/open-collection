Bi@smallQ-G
============

permanent_dir /lustre/ukt/milias/scratch/At-odft_on_quartz

sbatch --dependency=singleton --job-name=At@Q virgo_slurm_nw.main_N4_npn36_geopt.01
sbatch --dependency=singleton --job-name=At@Q virgo_slurm_nw.main_N4_npn36_geopt_restart.01 


