Surface diffusion energy barriers
=================================

https://wiki.fysik.dtu.dk/ase/tutorials/neb/diffusion.html

Surface diffusion energy barriers using the Nudged Elastic Band (NEB) method

WSL(Win11) Victus NB
~~~~~~~~~~~~~~~~~~~~

First, set up the initial and final states:

milias@Miro:/mnt/c/Users/miroi/OneDrive/Desktop/Work/projekty/open-collection/theoretical_chemistry/software/ase/runs/surface_diffusion_energy_barriers/.python3 init_final_states.py
                Step[ FC]     Time          Energy          fmax
BFGSLineSearch:    0[  0] 21:08:42        3.323870       0.2462
BFGSLineSearch:    1[  1] 21:08:42        3.314754       0.0378
                Step[ FC]     Time          Energy          fmax
BFGSLineSearch:    0[  0] 21:08:42        3.320051       0.1208
BFGSLineSearch:    1[  1] 21:08:42        3.316117       0.0474

Now, do the NEB calculation:

milias@Miro:/mnt/c/Users/miroi/OneDrive/Desktop/Work/projekty/open-collection/theoretical_chemistry/software/ase/runs/surface_diffusion_energy_barriers/.python3 do_neb_calc.py
      Step     Time          Energy          fmax
BFGS:    0 21:10:37        4.219952        3.520752
BFGS:    1 21:10:37        3.937039        2.176459
BFGS:    2 21:10:37        3.719814        0.435144
BFGS:    3 21:10:37        3.709652        0.230130
BFGS:    4 21:10:37        3.708879        0.244129
BFGS:    5 21:10:37        3.706088        0.257744
BFGS:    6 21:10:37        3.698532        0.213396
BFGS:    7 21:10:37        3.692121        0.246181
BFGS:    8 21:10:37        3.692274        0.187321
BFGS:    9 21:10:38        3.693484        0.172736
BFGS:   10 21:10:38        3.692659        0.151427
BFGS:   11 21:10:38        3.690809        0.073608
BFGS:   12 21:10:38        3.690202        0.070785
BFGS:   13 21:10:38        3.690382        0.078195
BFGS:   14 21:10:38        3.690426        0.103450
BFGS:   15 21:10:38        3.689890        0.099762
BFGS:   16 21:10:38        3.689029        0.054308
BFGS:   17 21:10:38        3.688737        0.028916

Visualize the results with:

ase gui neb.traj@-5:

and select Tools->NEB.

milias@Miro:/mnt/c/Users/miroi/OneDrive/Desktop/Work/projekty/open-collection/theoretical_chemistry/software/ase/runs/surface_diffusion_energy_barriers/.chmod 0700 /run/user/1000


milias@Miro:/mnt/c/Users/miroi/OneDrive/Desktop/Work/projekty/open-collection/theoretical_chemistry/software/ase/runs/surface_diffusion_energy_barriers/.python3 nebtools.py

