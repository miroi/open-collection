==============
Test ASE-DFTD4
==============

from /lustre/home/user/d/dsen/Documents/0_debug/d4

module add intel/oneapi Python/v3.10.13


milias@hydra.jinr.ru:~/work/projects/open-collection/theoretical_chemistry/software/dftd4-ase/runs/test_dftd4_executable/.python test_a8fac.py
Weakening DFT-D4 interaction by reducing s8 parameter:
============================================================
s8 =  1.0: D4 energy = -1.547227e-04 Hartree
s8 =  0.8: D4 energy = -1.466177e-04 Hartree
s8 =  0.6: D4 energy = -1.385128e-04 Hartree
s8 =  0.4: D4 energy = -1.304078e-04 Hartree
s8 =  0.2: D4 energy = -1.223028e-04 Hartree
s8 =  0.0: D4 energy = -1.141979e-04 Hartree

============================================================
Note: Lower s8 values result in weaker dispersion interaction
s8 = 1.0: Full strength D4 dispersion
s8 = 0.0: No D4 dispersion (only s6 term)


