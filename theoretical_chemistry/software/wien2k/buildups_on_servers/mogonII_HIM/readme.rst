Wien2k on MogonII
=================

mirilias@login23.mogon:~/work/software/wien2k/wien2k-openmpi-intel/.

module purge;
module load mpi/OpenMPI/3.1.1-iccifort-2018.3.222-GCC-6.3.0;
module load numlib/FFTW/3.3.8-intel-2018.03
module load lang/Python/2.7.15-intel-2018.03;


mirilias@login23.mogon:~/work/software/wien2k/wien2k-openmpi-intel/../check_minimal_software_requirements.sh

*******************************************************************************
*                        Minimal Software Requirements                        *
*                                  (Summary)                                  *
*                                                                             *
*                               Necessary Software                            *
*******************************************************************************

tcsh:
   A tcsh installation was found at /bin/tcsh . No further changes are needed.

Compiler:
   The FORTRAN compiler (ifort) was found at:
   /cluster/easybuild/broadwell/software/compiler/ifort/2018.3.222-GCC-6.3.0/compilers_and_libraries_2018.3.222/linux/bin/intel64/ifort

   The required linear algebra libraries could be found as part of the MKL at
   the following path:
   /cluster/easybuild/broadwell/software/imkl/2018.3.222-iimpi-2018.03/mkl

   The C compiler (icc) was found at:
   /cluster/easybuild/broadwell/software/compiler/ifort/2018.3.222-GCC-6.3.0/compilers_and_libraries_2018.3.222/linux/bin/intel64/icc

FFTW3 libraries:
   The fftw3 libraries (fftw3) were found at:
   /usr/lib64/

GNU make:
   GNU Make (GNU Make 4.2.1) could be found at:
   /usr/bin/make

bc:
   bc (basic calculator) could be found at:
   /usr/bin/bc

*******************************************************************************
*                 Optional Software (graphics, plotting,...)                  *
*******************************************************************************

Gnuplot:
   Gnuplot (Version: gnuplot 5.2 patchlevel 4) could be found at:
   /usr/bin/gnuplot

octave:
   No version of octave could be found.
   If you want to make use of the structeditor,  please
   install octave!

xcrysden:
   No version of xcrysden could be found.
   xcrysden renders WIEN2k struct files and is highly recommended
   I would install xcrysden!

VESTA:
   No version of VESTA could be found.
   VESTA is an alternative structure redering program
   I would install VESTA!

Perl:
   PERL (Version: 5.026003) could be found at:
   /usr/bin/perl
   Your version of perl is supported.

Ghostscript:
   gs (Ghostscript) could be found at:
   /usr/bin/gs

Python:
   Python 2.7.15 could be found at:
   /cluster/easybuild/broadwell/software/lang/Python/2.7.15-intel-2018.03/bin/python
   NumPy  1.14.5 could be found

*******************************************************************************
 The basic software requirements are probably fulfilled. 
 You can proceed with the installation using   ./expand_lapw





