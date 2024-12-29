Ase on hydra.jinr.ru
====================

interactive run
~~~~~~~~~~~~~~~~
python test_N2Cu.py
                Step[ FC]     Time          Energy          fmax
*Force-consistent energies used in optimization.
BFGSLineSearch:    0[  0] 19:53:04       11.689927*       1.0797
BFGSLineSearch:    1[  2] 19:53:05       11.670814*       0.4090
BFGSLineSearch:    2[  4] 19:53:06       11.625880*       0.0409
Adsorption energy: 0.323519422318034

batch run
~~~~~~~~~
sbatch hydra_slurm_ase.01

display in vm01/02:
milias@vm01.hydra.local:~/work/projects/open-collection/theoretical_chemistry/software/ase/buildup_on_servers/jinr_ru/hydra_jinr_ru/tests/.ase gui N2Cu.traj

