===================================
Si(21)O(60)H(36) Quartz (117 atoms)
===================================

get converged geometry

sbatch --dependency=singleton --job-name=QG117 virgo_slurm_nw.main_N4_npn36_geopt.01

sbatch --dependency=singleton --job-name=QG117 virgo_slurm_nw.main_N4_npn36_geopt_restart.01


