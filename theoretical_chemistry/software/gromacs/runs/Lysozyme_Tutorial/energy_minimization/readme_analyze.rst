=====================================================
analyze any .edr file using the GROMACS energy module
=====================================================

module add GROMACS/v2024.3

which gmx_mpi
/cvmfs/hybrilit.jinr.ru/sw/slc7_x86-64/GROMACS/v2024.3/bin/gmx_mpi

gmx_mpi energy -f em.edr -o potential.xvg

                      :-) GROMACS - gmx energy, 2024.3 (-:

Executable:   /cvmfs/hybrilit.jinr.ru/sw/slc7_x86-64/GROMACS/v2024.3/bin/gmx_mpi
Data prefix:  /cvmfs/hybrilit.jinr.ru/sw/slc7_x86-64/GROMACS/v2024.3
Working dir:  /zfs/scratch/HybriLITWorkshop2025/milias/projects/open-collection/theoretical_chemistry/software/gromacs/runs/Lysozyme_Tutorial/energy_minimization
Command line:
  gmx_mpi energy -f em.edr -o potential.xvg

Opened em.edr as single precision energy file

Select the terms you want from the following list by
selecting either (part of) the name or the number or a combination.
End your selection with an empty line or a zero.
-------------------------------------------------------------------
  1  Bond             2  Angle            3  Proper-Dih.      4  Per.-Imp.-Dih.
  5  LJ-14            6  Coulomb-14       7  LJ-(SR)          8  Coulomb-(SR)
  9  Coul.-recip.    10  Potential       11  Pressure        12  Vir-XX
 13  Vir-XY          14  Vir-XZ          15  Vir-YX          16  Vir-YY
 17  Vir-YZ          18  Vir-ZX          19  Vir-ZY          20  Vir-ZZ
 21  Pres-XX         22  Pres-XY         23  Pres-XZ         24  Pres-YX
 25  Pres-YY         26  Pres-YZ         27  Pres-ZX         28  Pres-ZY
 29  Pres-ZZ         30  #Surf*SurfTen   31  T-rest

11
0
Last energy frame read 596 time  753.000

Statistics over 754 steps [ 0.0000 through 753.0000 ps ], 1 data sets
All statistics are over 597 points (frames)

Energy                      Average   Err.Est.       RMSD  Tot-Drift
-------------------------------------------------------------------------------
Pressure                   -4587.09        860    2798.51   -5132.95  (bar)

GROMACS reminds you: "Act like Prometheus would" (Gogol Bordello)


