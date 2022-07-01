
module load impi/2021.2.0-intel-compilers-2021.2.0

ilias@login1.kelinux.saske.sk:~/work/qch/software/quantum-espresso/qe-7.0/build_intelmpi/.module list

Currently Loaded Modules:
  1) GCCcore/10.3.0                   7) OpenSSL/1.1                    13) gettext/0.21-GCCcore-10.3.0       19) libarchive/3.5.1-GCCcore-10.3.0
  2) zlib/1.2.11-GCCcore-10.3.0       8) cURL/7.76.0-GCCcore-10.3.0     14) libreadline/8.1-GCCcore-10.3.0    20) CMake/3.20.1-GCCcore-10.3.0
  3) binutils/2.36.1-GCCcore-10.3.0   9) expat/2.2.9-GCCcore-10.3.0     15) DB/18.1.40-GCCcore-10.3.0         21) impi/2021.2.0-intel-compilers-2021.2.0
  4) intel-compilers/2021.2.0        10) XZ/5.2.5-GCCcore-10.3.0        16) Perl/5.32.1-GCCcore-10.3.0
  5) numactl/2.0.14-GCCcore-10.3.0   11) libxml2/2.9.10-GCCcore-10.3.0  17) git/2.32.0-GCCcore-10.3.0-nodocs
  6) UCX/1.10.0-GCCcore-10.3.0       12) ncurses/6.2-GCCcore-10.3.0     18) bzip2/1.0.8-GCCcore-10.3.0


ilias@login1.kelinux.saske.sk:~/work/qch/software/quantum-espresso/qe-7.0/build_intelmpi/.cmake -DCMAKE_C_COMPILER=mpiicc -DCMAKE_Fortran_COMPILER=mpiifort ..
-- The Fortran compiler identification is Intel 20.2.2.20210228
-- The C compiler identification is Intel 20.2.2.20210228
-- Detecting Fortran compiler ABI info
-- Detecting Fortran compiler ABI info - done
-- Check for working Fortran compiler: /lustre/home/utils/easybuild_old/software/impi/2021.2.0-intel-compilers-2021.2.0/mpi/2021.2.0/bin/mpiifort - skipped
-- Checking whether /lustre/home/utils/easybuild_old/software/impi/2021.2.0-intel-compilers-2021.2.0/mpi/2021.2.0/bin/mpiifort supports Fortran 90
-- Checking whether /lustre/home/utils/easybuild_old/software/impi/2021.2.0-intel-compilers-2021.2.0/mpi/2021.2.0/bin/mpiifort supports Fortran 90 - yes
-- Detecting C compiler ABI info
-- Detecting C compiler ABI info - done
-- Check for working C compiler: /lustre/home/utils/easybuild_old/software/impi/2021.2.0-intel-compilers-2021.2.0/mpi/2021.2.0/bin/mpiicc - skipped
-- Detecting C compile features
-- Detecting C compile features - done
-- Setting build type to 'Release' as none was specified
-- Looking for mallinfo
-- Looking for mallinfo - found
-- Enable sanitizer QE_ENABLE_SANITIZER=none
-- C preprocessor used by qe_preprocess_source in qeHelpers.cmake: /lustre/home/utils/easybuild_old/software/GCCcore/10.3.0/bin/cpp
-- Performing Test Fortran_ISYSTEM_SUPPORTED
-- Performing Test Fortran_ISYSTEM_SUPPORTED - Success
-- Found MPI_Fortran: /lustre/home/utils/easybuild_old/software/impi/2021.2.0-intel-compilers-2021.2.0/mpi/2021.2.0/bin/mpiifort (found version "3.1") 
-- Found MPI: TRUE (found version "3.1") found components: Fortran 
-- MPI settings used by CTest
     MPIEXEC_EXECUTABLE : /lustre/home/utils/easybuild_old/software/impi/2021.2.0-intel-compilers-2021.2.0/mpi/2021.2.0/bin/mpiexec
     MPIEXEC_NUMPROC_FLAG : -n
     MPIEXEC_PREFLAGS : 
   Tests run as : /lustre/home/utils/easybuild_old/software/impi/2021.2.0-intel-compilers-2021.2.0/mpi/2021.2.0/bin/mpiexec -n <NUM_PROCS>  <EXECUTABLE>
-- Found Git: /lustre/home/utils/easybuild_old/software/git/2.32.0-GCCcore-10.3.0-nodocs/bin/git (found suitable version "2.32.0", minimum required is "2.13") 
-- Source files are not cloned from a git repository.
-- Trying to find LAPACK from Intel MKL
-- Looking for pthread.h
-- Looking for pthread.h - found
-- Performing Test CMAKE_HAVE_LIBC_PTHREAD
-- Performing Test CMAKE_HAVE_LIBC_PTHREAD - Success
-- Found Threads: TRUE  
-- Looking for Fortran sgemm
-- Looking for Fortran sgemm - found
-- Found BLAS: /lustre/home/freeware/intel/compilers_and_libraries_2018.2.199/linux/mkl/lib/intel64_lin/libmkl_intel_lp64.so;/lustre/home/freeware/intel/compilers_and_libraries_2018.2.199/linux/mkl/lib/intel64_lin/libmkl_sequential.so;/lustre/home/freeware/intel/compilers_and_libraries_2018.2.199/linux/mkl/lib/intel64_lin/libmkl_core.so;-lm;-ldl  
-- Looking for Fortran cheev
-- Looking for Fortran cheev - found
-- Found LAPACK: /lustre/home/freeware/intel/compilers_and_libraries_2018.2.199/linux/mkl/lib/intel64_lin/libmkl_intel_lp64.so;/lustre/home/freeware/intel/compilers_and_libraries_2018.2.199/linux/mkl/lib/intel64_lin/libmkl_sequential.so;/lustre/home/freeware/intel/compilers_and_libraries_2018.2.199/linux/mkl/lib/intel64_lin/libmkl_core.so;-lm;-ldl;-lm;-ldl  
-- Found LAPACK: /lustre/home/freeware/intel/compilers_and_libraries_2018.2.199/linux/mkl/lib/intel64_lin/libmkl_intel_lp64.so;/lustre/home/freeware/intel/compilers_and_libraries_2018.2.199/linux/mkl/lib/intel64_lin/libmkl_sequential.so;/lustre/home/freeware/intel/compilers_and_libraries_2018.2.199/linux/mkl/lib/intel64_lin/libmkl_core.so;-lm;-ldl;/lustre/home/freeware/intel/compilers_and_libraries_2018.2.199/linux/mkl/lib/intel64_lin/libmkl_intel_lp64.so;/lustre/home/freeware/intel/compilers_and_libraries_2018.2.199/linux/mkl/lib/intel64_lin/libmkl_sequential.so;/lustre/home/freeware/intel/compilers_and_libraries_2018.2.199/linux/mkl/lib/intel64_lin/libmkl_core.so;-lm;-ldl;-lm;-ldl
-- Looking for Fortran zhpev
-- Looking for Fortran zhpev - found
-- Installing FoX via submodule
-- Cloning https://github.com/pietrodelugas/fox.git into /lustre/home/ilias/work/qch/software/quantum-espresso/qe-7.0/external/fox.
hint: Using 'master' as the name for the initial branch. This default branch name
hint: is subject to change. To configure the initial branch name to use in all
hint: of your new repositories, which will suppress this warning, call:
hint: 
hint:   git config --global init.defaultBranch <name>
hint: 
hint: Names commonly chosen instead of 'master' are 'main', 'trunk' and
hint: 'development'. The just-created branch can be renamed via this command:
hint: 
hint:   git branch -m <name>
Initialized empty Git repository in /lustre/home/ilias/work/qch/software/quantum-espresso/qe-7.0/external/fox/.git/
From https://github.com/pietrodelugas/fox
 * branch            98ce8e36c881ccf511c1c4991ff76c174eaaeab9 -> FETCH_HEAD
Switched to a new branch 'recorded_HEAD'
-- Determining operating system and architecture:
   -> your operating system is : Linux-3.10.0-1160.21.1.el7.x86_64
   -> your architecture is     : x86_64
-- Searching for m4 scripting language
   -> /usr/bin/m4
-- Determining end-of-line character by the host name
   -> end-of-line character is LF
-- Determining method to call flush intrinsic
   -> flush intrinsic method is default
-- Checking for 'associated in restricted expression' bug
-- Determining method to call abort intrinsic
   -> abort : bare works
-- Cloning https://github.com/wannier-developers/wannier90.git into /lustre/home/ilias/work/qch/software/quantum-espresso/qe-7.0/external/wannier90.
hint: Using 'master' as the name for the initial branch. This default branch name
hint: is subject to change. To configure the initial branch name to use in all
hint: of your new repositories, which will suppress this warning, call:
hint: 
hint:   git config --global init.defaultBranch <name>
hint: 
hint: Names commonly chosen instead of 'master' are 'main', 'trunk' and
hint: 'development'. The just-created branch can be renamed via this command:
hint: 
hint:   git branch -m <name>
Initialized empty Git repository in /lustre/home/ilias/work/qch/software/quantum-espresso/qe-7.0/external/wannier90/.git/
From https://github.com/wannier-developers/wannier90
 * branch            9676b93252046524852445c8e44fbe7ce347f63d -> FETCH_HEAD
Switched to a new branch 'recorded_HEAD'
-- Installing MBD via submodule
-- Cloning https://github.com/libmbd/libmbd.git into /lustre/home/ilias/work/qch/software/quantum-espresso/qe-7.0/external/mbd.
hint: Using 'master' as the name for the initial branch. This default branch name
hint: is subject to change. To configure the initial branch name to use in all
hint: of your new repositories, which will suppress this warning, call:
hint: 
hint:   git config --global init.defaultBranch <name>
hint: 
hint: Names commonly chosen instead of 'master' are 'main', 'trunk' and
hint: 'development'. The just-created branch can be renamed via this command:
hint: 
hint:   git branch -m <name>
Initialized empty Git repository in /lustre/home/ilias/work/qch/software/quantum-espresso/qe-7.0/external/mbd/.git/
From https://github.com/libmbd/libmbd
 * branch            82005cbb65bdf5d32ca021848eec8f19da956a77 -> FETCH_HEAD
Switched to a new branch 'recorded_HEAD'
-- Cloning https://gitlab.com/max-centre/components/devicexlib.git into /lustre/home/ilias/work/qch/software/quantum-espresso/qe-7.0/external/devxlib.
hint: Using 'master' as the name for the initial branch. This default branch name
hint: is subject to change. To configure the initial branch name to use in all
hint: of your new repositories, which will suppress this warning, call:
hint: 
hint:   git config --global init.defaultBranch <name>
hint: 
hint: Names commonly chosen instead of 'master' are 'main', 'trunk' and
hint: 'development'. The just-created branch can be renamed via this command:
hint: 
hint:   git branch -m <name>
Initialized empty Git repository in /lustre/home/ilias/work/qch/software/quantum-espresso/qe-7.0/external/devxlib/.git/
From https://gitlab.com/max-centre/components/devicexlib
 * branch            a6b89ef77b1ceda48e967921f1f5488d2df9226d -> FETCH_HEAD
Switched to a new branch 'recorded_HEAD'
-- Found VendorFFTW: /lustre/home/freeware/intel/compilers_and_libraries_2018.2.199/linux/mkl/lib/intel64_lin/libmkl_intel_lp64.so;/lustre/home/freeware/intel/compilers_and_libraries_2018.2.199/linux/mkl/lib/intel64_lin/libmkl_sequential.so;/lustre/home/freeware/intel/compilers_and_libraries_2018.2.199/linux/mkl/lib/intel64_lin/libmkl_core.so;-lm;-ldl;/lustre/home/freeware/intel/compilers_and_libraries_2018.2.199/linux/mkl/lib/intel64_lin/libmkl_intel_lp64.so;/lustre/home/freeware/intel/compilers_and_libraries_2018.2.199/linux/mkl/lib/intel64_lin/libmkl_sequential.so;/lustre/home/freeware/intel/compilers_and_libraries_2018.2.199/linux/mkl/lib/intel64_lin/libmkl_core.so;-lm;-ldl;-lm;-ldl  
-- Enabling tests in test-suite

Only pw and cp results from ctest are reliable, we are working on making the rest tests work reliably with ctest. To run non-pw/cp tests, make a softlink of the bin directory to the root of QE source tree and run tests in the test-suite directory under that root.

-- generating tests in pw category
-- generating tests in cp category
-- generating tests in ph category
-- generating tests in epw category
-- generating tests in tddfpt category
-- generating tests in hp category
-- Configuring done
-- Generating done
-- Build files have been written to: /lustre/home/ilias/work/qch/software/quantum-espresso/qe-7.0/build_intelmpi

