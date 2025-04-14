====================================
QE-develop build with CMake/IntelMPI 
====================================

milias@vm02.hydra.local:~/work/software/quantum-espresso/qe-develop/.git clone git@gitlab.com:QEF/q-e.git  


mkdir build_intelmpi_mkl

milias@hydra.jinr.ru:~/work/software/quantum-espresso/xdm-fix/q-e-extendZ/.module add intel/v2021.1
milias@hydra.jinr.ru:~/work/software/quantum-espresso/xdm-fix/q-e-extendZ/.emkl
Intel MKL library ? MKLROOT=/cvmfs/hybrilit.jinr.ru/sw/slc7_x86-64/intel/v2021.1/mkl/latest
milias@hydra.jinr.ru:~/work/software/quantum-espresso/xdm-fix/q-e-extendZ/.which mpiifort
/cvmfs/hybrilit.jinr.ru/sw/slc7_x86-64/intel/v2021.1/mpi/2021.1.1/bin/mpiifort
milias@hydra.jinr.ru:~/work/software/quantum-espresso/xdm-fix/q-e-extendZ/.mpiifort -V
Intel(R) Fortran Intel(R) 64 Compiler Classic for applications running on Intel(R) 64, Version 2021.1 Build 20201112_000000
Copyright (C) 1985-2020 Intel Corporation.  All rights reserved.

milias@hydra.jinr.ru:~/work/software/quantum-espresso/xdm-fix/q-e-extendZ/build_intelmpi_mkl/.module add CMake/v3.29.2

milias@hydra.jinr.ru:~/work/software/quantum-espresso/xdm-fix/q-e-extendZ/.module list
Currently Loaded Modulefiles:
  1) GVR/v1.0-1                              6) Python/v3.6.5
  2) intel/v2021.1                           7) ELPA/v2020.05.001_intel2018_python365
  3) BASE/1.0                                8) fftw/v3.3.7-5
  4) intel/v2018.1.163-9                     9) CMake/v3.29.2
  5) openmpi/v1.8.8-1

build
~~~~~
milias@hydra.jinr.ru:~/work/software/quantum-espresso/xdm-extend/q-e-ext-xdm/build_intelmpi_mkl/.cmake -DQE_ENABLE_MPI=ON -DQE_ENABLE_MPI_MODULE=ON   -DCMAKE_C_COMPILER=icc -DCMAKE_CXX_COMPILER=icpc -DCMAKE_Fortran_COMPILER=mpiifort ..
-- The Fortran compiler identification is Intel 2021.1.0.20201112
-- The C compiler identification is Intel 2021.1.0.20201112
-- Detecting Fortran compiler ABI info
-- Detecting Fortran compiler ABI info - done
-- Check for working Fortran compiler: /cvmfs/hybrilit.jinr.ru/sw/slc7_x86-64/intel/v2021.1/mpi/2021.1.1/bin/mpiifort - skipped
-- Detecting C compiler ABI info
-- Detecting C compiler ABI info - done
-- Check for working C compiler: /cvmfs/hybrilit.jinr.ru/sw/slc7_x86-64/intel/v2021.1/compiler/2021.1.1/linux/bin/intel64/icc - skipped
-- Detecting C compile features
-- Detecting C compile features - done
-- Setting build type to 'Release' as none was specified
-- Enable sanitizer QE_ENABLE_SANITIZER=none
-- C preprocessor used by qe_preprocess_source in qeHelpers.cmake: /usr/bin/cpp
-- Performing Test Fortran_ISYSTEM_SUPPORTED
-- Performing Test Fortran_ISYSTEM_SUPPORTED - Success
-- Found MPI_Fortran: /cvmfs/hybrilit.jinr.ru/sw/slc7_x86-64/intel/v2021.1/mpi/2021.1.1/bin/mpiifort (found version "3.1")
-- Found MPI: TRUE (found version "3.1") found components: Fortran
-- Selected the Fortran 'mpi' module. QE_ENABLE_MPI_MODULE=ON
-- MPI settings used by CTest
     MPIEXEC_EXECUTABLE : /cvmfs/hybrilit.jinr.ru/sw/slc7_x86-64/intel/v2021.1/mpi/2021.1.1/bin/mpiexec
     MPIEXEC_NUMPROC_FLAG : -n
     MPIEXEC_PREFLAGS :
   Tests run as : /cvmfs/hybrilit.jinr.ru/sw/slc7_x86-64/intel/v2021.1/mpi/2021.1.1/bin/mpiexec -n <NUM_PROCS>  <EXECUTABLE>
-- Found Git: /usr/bin/git (found suitable version "2.23.0", minimum required is "2.13")
-- Source files are cloned from a git repository.
   sed supports -E
   Git branch: xdm_ext
   Git commit hash: 839a6640b681fa6855c99a7112dabbf6dd2c92d6
-- Trying to find LAPACK from Intel MKL
-- Performing Test CMAKE_HAVE_LIBC_PTHREAD
-- Performing Test CMAKE_HAVE_LIBC_PTHREAD - Failed
-- Looking for pthread_create in pthreads
-- Looking for pthread_create in pthreads - not found
-- Looking for pthread_create in pthread
-- Looking for pthread_create in pthread - found
-- Found Threads: TRUE
-- Looking for Fortran sgemm
-- Looking for Fortran sgemm - found
-- Found BLAS: /cvmfs/hybrilit.jinr.ru/sw/slc7_x86-64/intel/v2021.1/mkl/latest/lib/intel64/libmkl_intel_lp64.so;/cvmfs/hybrilit.jinr.ru/sw/slc7_x86-64/intel/v2021.1/mkl/latest/lib/intel64/libmkl_sequential.so;/cvmfs/hybrilit.jinr.ru/sw/slc7_x86-64/intel/v2021.1/mkl/latest/lib/intel64/libmkl_core.so;-lpthread;-lm;-ldl
-- Looking for Fortran cheev
-- Looking for Fortran cheev - found
-- Found LAPACK: /cvmfs/hybrilit.jinr.ru/sw/slc7_x86-64/intel/v2021.1/mkl/latest/lib/intel64/libmkl_intel_lp64.so;/cvmfs/hybrilit.jinr.ru/sw/slc7_x86-64/intel/v2021.1/mkl/latest/lib/intel64/libmkl_sequential.so;/cvmfs/hybrilit.jinr.ru/sw/slc7_x86-64/intel/v2021.1/mkl/latest/lib/intel64/libmkl_core.so;-lpthread;-lm;-ldl;-lpthread;-lm;-ldl
-- Looking for Fortran zhpev
-- Looking for Fortran zhpev - found
-- Installing Wannier90 via submodule
Submodule 'external/wannier90' (https://github.com/wannier-developers/wannier90.git) registered for path 'external/wannier90'
Cloning into '/lustre/home/user/m/milias/work/software/quantum-espresso/xdm-extend/q-e-ext-xdm/external/wannier90'...
From https://github.com/wannier-developers/wannier90
 * branch            1d6b187374a2d50b509e5e79e2cab01a79ff7ce1 -> FETCH_HEAD
Submodule path 'external/wannier90': checked out '1d6b187374a2d50b509e5e79e2cab01a79ff7ce1'
-- Installing MBD via submodule
Submodule 'external/mbd' (https://github.com/libmbd/libmbd.git) registered for path 'external/mbd'
Cloning into '/lustre/home/user/m/milias/work/software/quantum-espresso/xdm-extend/q-e-ext-xdm/external/mbd'...
Submodule path 'external/mbd': checked out '89a3cc199c0a200c9f0f688c3229ef6b9a8d63bd'
-- Found Git: /usr/bin/git (found version "2.23.0")
-- Setting version tag to 0.13.0-2-g89a3cc1 from Git
-- Installing DeviceXlib via submodule
Submodule 'external/devxlib' (https://gitlab.com/max-centre/components/devicexlib.git) registered for path 'external/devxlib'
Cloning into '/lustre/home/user/m/milias/work/software/quantum-espresso/xdm-extend/q-e-ext-xdm/external/devxlib'...
From https://gitlab.com/max-centre/components/devicexlib
 * branch            a6b89ef77b1ceda48e967921f1f5488d2df9226d -> FETCH_HEAD
Submodule path 'external/devxlib': checked out 'a6b89ef77b1ceda48e967921f1f5488d2df9226d'
-- Found VendorFFTW: /cvmfs/hybrilit.jinr.ru/sw/slc7_x86-64/intel/v2021.1/mkl/latest/lib/intel64/libmkl_intel_lp64.so;/cvmfs/hybrilit.jinr.ru/sw/slc7_x86-64/intel/v2021.1/mkl/latest/lib/intel64/libmkl_sequential.so;/cvmfs/hybrilit.jinr.ru/sw/slc7_x86-64/intel/v2021.1/mkl/latest/lib/intel64/libmkl_core.so;-lpthread;-lm;-ldl;/cvmfs/hybrilit.jinr.ru/sw/slc7_x86-64/intel/v2021.1/mkl/latest/lib/intel64/libmkl_intel_lp64.so;/cvmfs/hybrilit.jinr.ru/sw/slc7_x86-64/intel/v2021.1/mkl/latest/lib/intel64/libmkl_sequential.so;/cvmfs/hybrilit.jinr.ru/sw/slc7_x86-64/intel/v2021.1/mkl/latest/lib/intel64/libmkl_core.so;-lpthread;-lm;-ldl;-lpthread;-lm;-ldl
-- Looking for mallinfo
-- Looking for mallinfo - found
-- Enabling tests in test-suite

Only pw and cp results from ctest are reliable, we are working on making the rest tests work reliably with ctest. To run non-pw/cp tests, make a softlink of the bin directory to the root of QE source tree and run tests in the test-suite directory under that root.

-- generating tests in pw category
-- generating tests in cp category
-- Configuring done (405.4s)
-- Generating done (292.9s)
-- Build files have been written to: /lustre/home/user/m/milias/work/software/quantum-espresso/xdm-extend/q-e-ext-xdm/build_intelmpi_mkl
milias@hydra.jinr.ru:~/work/software/quantum-espresso/xdm-extend/q-e-ext-xdm/build_intelmpi_mkl/.

compile
~~~~~~~~
milias@hydra.jinr.ru:~/work/software/quantum-espresso/xdm-extend/q-e-ext-xdm/build_intelmpi_mkl/.m -j4
.
.
milias@hydra.jinr.ru:~/work/software/quantum-espresso/xdm-extend/q-e-ext-xdm/build_intelmpi_mkl/.ls bin/
abcoeff_to_eps.x*  epa.x*             hgh2qe.x*           open_grid.x*           pw2bgw.x*              turbo_eels.x*
all_currents.x*    epsilon_Gaus.x*    hp.x*               path_interpolation.x*  pw2critic.x*           turbo_lanczos.x*
alpha2f.x*         epsilon.x*         ibrav2cell.x*       pawplot.x*             pw2gt.x*               turbo_magnon.x*
average.x*         epw.x*             initial_state.x*    phcg.x*                pw2gw.x*               turbo_spectrum.x*
bands_unfold.x*    ev.x*              kcwpp_interp.x*     ph.x*                  pw2wannier90.x*        upfconv.x*
bands.x*           fd_ef.x*           kcwpp_sh.x*         plan_avg.x*            pw4gww.x*              ups.x*
bse_main.x*        fd_ifc.x*          kcw.x*              plotband.x*            pwcond.x*              virtual_v2.x*
casino2upf.x*      fd.x*              kpoints.x*          plotproj.x*            pwi2xsf.x*             w90chk2chk.x*
cell2ibrav.x*      fermi_int_0.x*     lambda.x*           plotrho.x*             pw.x*                  wannier2pw.x*
cppp.x*            fermi_int_1.x*     ld1.x*              pmw.x*                 q2qstar.x*             wannier90.x*
cp.x*              fermi_proj.x*      manycp.x*           postahc.x*             q2r.x*                 wannier_ham.x*
d3hess.x*          fermi_velocity.x*  matdyn.x*           postw90.x*             scan_ibrav.x*          wannier_plot.x*
disca.x*           fqha.x*            memory_pw4gww.x*    ppacf.x*               simple_bse.x*          wfck2r.x*
dos_sp.x*          fs.x*              merge_wann.x*       pp_disca.x*            simple_ip.x*           wfdd.x*
dos.x*             graph.x*           molecularnexafs.x*  pprism.x*              simple.x*              xspectra.x*
dvscf_q2r.x*       gww_fit.x*         molecularpdos.x*    pp_spctrlfn.x*         spectra_correction.x*  ZG.x*
dynmat.x*          gww.x*             neb.x*              pp.x*                  sumpdos.x*
ef.x*              head.x*            nscf2supercond.x*   projwfc.x*             turbo_davidson.x*




