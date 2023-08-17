At@smallQ
=========

basis ecp
~~~~~~~~~
At library lanl2dz_ecp does not exists !!!

https://github.com/nwchemgit/nwchem/blob/master/src/basis/libraries/crenbl_ecp

2nd run after 8 hours...

SLURM jobs sequentially:
https://chuckaknight.wordpress.com/2016/08/02/slurm-scheduling-so-they-run-sequentially

sbatch --dependency=singleton --job-name=AtOH@Q virgo_slurm_nw.main_N4_npn36_geopt.01
sbatch --dependency=singleton --job-name=AtOH@Q virgo_slurm_nw.main_N4_npn36_geopt_restart.01 

