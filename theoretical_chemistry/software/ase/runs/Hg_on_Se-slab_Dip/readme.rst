============
Hg@Se54(100)
============

Program systematicaly scans all surface positions on frozen Se54(100) slab, places Hg atom on each position and optimizes the system's  geometry.

After checking all the surface positions it finds the most suitable - that is the global minima of Hg@Se54(100) system.

All energies get stored in the file adsorption_summary.txt . 

The program creates subdirectries with optimized geometries, and also with optimization trajectories. 

Program works upon the fast Lenard-Johnson (LJ) interatomic potential, which part of ase ecosystem.

from Dip's /lustre/home/user/d/dsen/Documents/2_example/adorption_example/5
modified - removed DFTD4 part, keeping only LJ term

running: python hg_se.py > logfile
