Bi@smallQ-G with NWChem
========================


frequency calcs

180gb, long, N4 ... virgo_slurm_nw.main_N4_npn36_freq.01

try 360gb, main, N4 , restartable /lustre/ukt/milias/scratch/Bi-odft_on_quartz_freq


sbatch --dependency=singleton --job-name=Bi@Q   virgo_slurm_nw.main_N4_npn36_freq.01
sbatch --dependency=singleton --job-name=Bi@Q   virgo_slurm_nw.main_N4_npn36_freq_restart.01





