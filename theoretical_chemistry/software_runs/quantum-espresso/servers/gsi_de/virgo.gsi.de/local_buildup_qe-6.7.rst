Quantum Espresso on Virgo cluster
=================================

/lustre/ukt/milias/work/software/quantum-espresso/qe-6.7

module purge

module load openmpi/intel/4.0.3_intel19.0

ESPRESSO can take advantage of several optimized numerical libraries
(essl, fftw, mkl...).  This configure script attempts to find them,
but may fail if they have been installed in non-standard locations.
If a required library is not found, the local copy will be compiled.

The following libraries have been found:
  BLAS_LIBS=  -lmkl_intel_lp64  -lmkl_sequential -lmkl_core
  LAPACK_LIBS=
  SCALAPACK_LIBS=-lmkl_scalapack_lp64 -lmkl_blacs_openmpi_lp64
  FFT_LIBS=

make -j16 all





