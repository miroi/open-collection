=====================================
Vibrational modes of the H2O molecule
=====================================

https://wiki.fysik.dtu.dk/gpaw/tutorialsexercises/vibrational/vibrations/vibrations.html

milias@lxi085.gsi.de:~/Work/qch/projects/open-collection/theoretical_chemistry/software/ase/runs/gpaw-ase/vibrations_H2O/.python3 vibr_H2O.py 
                Step[ FC]     Time          Energy          fmax
*Force-consistent energies used in optimization.
BFGSLineSearch:    0[  0] 15:27:21       -9.313801*       5.8622
BFGSLineSearch:    1[  1] 15:27:23      -10.846138*       7.7659
BFGSLineSearch:    2[  2] 15:27:26      -12.601781*       7.3392
BFGSLineSearch:    3[  3] 15:27:28      -13.334419*       4.4396
BFGSLineSearch:    4[  5] 15:27:32      -13.505857*       2.8911
BFGSLineSearch:    5[  7] 15:27:36      -13.704775*       1.0850
BFGSLineSearch:    6[  9] 15:27:39      -13.719613*       0.1253
BFGSLineSearch:    7[ 10] 15:27:40      -13.719917*       0.0452
.
.
RuntimeError: Broken symmetry!
milias@lxi085.gsi.de:~/Work/qch/projects/open-collection/theoretical_chemistry/software/ase/runs/gpaw-ase/vibrations_H2O/.

https://gitlab.com/gpaw/gpaw/-/issues/934

fixed
-----

milias@Miro:/mnt/c/Users/miroi/OneDrive/Desktop/Work/projekty/open-collection/theoretical_chemistry/software/gpaw-ase/runs/vibrations_H2O/.python3 gpaw_h2o_vibrations.py
                Step[ FC]     Time          Energy          fmax
BFGSLineSearch:    0[  0] 22:29:29       -9.313801       5.8622
BFGSLineSearch:    1[  1] 22:29:31      -10.846138       7.7659
BFGSLineSearch:    2[  2] 22:29:32      -12.601781       7.3392
BFGSLineSearch:    3[  3] 22:29:33      -13.334419       4.4396
BFGSLineSearch:    4[  5] 22:29:37      -13.505857       2.8911
BFGSLineSearch:    5[  7] 22:29:39      -13.704775       1.0850
BFGSLineSearch:    6[  9] 22:29:41      -13.719613       0.1253
BFGSLineSearch:    7[ 10] 22:29:42      -13.719917       0.0452
---------------------
  #    meV     cm^-1
---------------------
  0   51.3i    413.9i
  1   40.6i    327.5i
  2   23.1i    186.6i
  3    0.8i      6.2i
  4    5.6      45.5
  5    9.0      72.7
  6  186.9    1507.3
  7  450.7    3635.2
  8  465.0    3750.8
---------------------
Zero-point energy: 0.559 eV

milias@Miro:/mnt/c/Users/miroi/OneDrive/Desktop/Work/projekty/open-collection/theoretical_chemistry/software/gpaw-ase/runs/vibrations_H2O/.ls
gpaw_h2o_vibrations.py*  readme.rst*  vib.0.traj*  vib.2.traj*  vib.4.traj*  vib.6.traj*  vib.8.traj*
h2o.txt*                 vib/         vib.1.traj*  vib.3.traj*  vib.5.traj*  vib.7.traj*  vibr_H2O.py_bad*
milias@Miro:/mnt/c/Users/miroi/OneDrive/Desktop/Work/projekty/open-collection/theoretical_chemistry/software/gpaw-ase/runs/vibrations_H2O/.ls vib
cache.0x+.json*  cache.0y-.json*  cache.1x+.json*  cache.1y-.json*  cache.2x+.json*  cache.2y-.json*  cache.eq.json*
cache.0x-.json*  cache.0z+.json*  cache.1x-.json*  cache.1z+.json*  cache.2x-.json*  cache.2z+.json*
cache.0y+.json*  cache.0z-.json*  cache.1y+.json*  cache.1z-.json*  cache.2y+.json*  cache.2z-.json*
display vibrations:

ase gui vib.*.traj


