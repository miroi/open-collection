Abinit on ADF2
==============


milias@adf2:~/work/software/abinit/abinit-8.10.3/../configure FC=mpif90 CC=mpicc  --prefix=$PWD --enable-mpi
 ==============================================================================
 === Final remarks                                                          ===
 ==============================================================================


Summary of important options:

  * C compiler      : gnu version 9.3
  * Fortran compiler: gnu version 9.3
  * architecture    : intel xeon (64 bits)

  * debugging       : basic
  * optimizations   : standard

  * OpenMP enabled  : no (collapse: ignored)
  * MPI    enabled  : yes
  * MPI-IO enabled  : auto
  * GPU    enabled  : no (flavor: none)

  * TRIO   flavor = none
  * TIMER  flavor = abinit (libs: ignored)
  * LINALG flavor = netlib (libs: auto-detected)
  * ALGO   flavor = none (libs: ignored)
  * FFT    flavor = none (libs: ignored)
  * MATH   flavor = none (libs: ignored)
  * DFT    flavor = none

Configuration complete.
You may now type "make" to build ABINIT.
(or, on a SMP machine, "make mj4", or "make multi multi_nprocs=<n>")

PROBLEM
-------
milias@adf2:~/work/software/abinit/abinit-8.10.3/.make
CDPATH="${ZSH_VERSION+.}:" && cd . && /bin/sh /home/milias/work/software/abinit/abinit-8.10.3/config/gnu/missing aclocal-1.16 -I config/m4
/home/milias/work/software/abinit/abinit-8.10.3/config/gnu/missing: line 81: aclocal-1.16: command not found
WARNING: 'aclocal-1.16' is missing on your system.
         You should only need it if you modified 'acinclude.m4' or
         'configure.ac' or m4 files included by 'configure.ac'.
         The 'aclocal' program is part of the GNU Automake package:
         <https://www.gnu.org/software/automake>
         It also requires GNU Autoconf, GNU m4 and Perl in order to run:
         <https://www.gnu.org/software/autoconf>
         <https://www.gnu.org/software/m4/>
         <https://www.perl.org/>
make: *** [aclocal.m4] Error 127

