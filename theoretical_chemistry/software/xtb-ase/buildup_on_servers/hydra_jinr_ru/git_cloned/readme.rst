==============
xtb git-cloned
==============

clone
~~~~~
git@github.com:grimme-lab/xtb.git

CMake buildup
~~~~~~~~~~~~~~

https://github.com/grimme-lab/xtb?tab=readme-ov-file#cmake

https://github.com/grimme-lab/xtb/blob/main/cmake/README.adoc#configure-intel-fortran-build-with-mkl

module add intel/oneapi CMake/v3.29.2
export FC=ifort CC=icc

milias@hydra.jinr.ru:~/work/software/xtb/git_cloned/xtb/.cmake -B_build -S. -GNinja -DCMAKE_BUILD_TYPE=Release --install-prefix /lustre/home/user/m/milias/work/software/xtb/git_cloned/install

-- The C compiler identification is Intel 2021.4.0.20210910
-- The Fortran compiler identification is Intel 2021.4.0.20210910
-- Detecting C compiler ABI info
-- Detecting C compiler ABI info - done
-- Check for working C compiler: /cvmfs/hybrilit.jinr.ru/sw/slc7_x86-64/intel/oneapi/compiler/latest/linux/bin/intel64/icc - skipped
-- Detecting C compile features
-- Detecting C compile features - done
-- Detecting Fortran compiler ABI info
-- Detecting Fortran compiler ABI info - done
-- Check for working Fortran compiler: /cvmfs/hybrilit.jinr.ru/sw/slc7_x86-64/intel/oneapi/compiler/latest/linux/bin/intel64/ifort -        skipped
-- Retrieving mctc-lib from https://github.com/grimme-lab/mctc-lib
-- Found OpenMP_C: -qopenmp (found version "5.0")
-- Found OpenMP_Fortran: -qopenmp (found version "5.0")
-- Found OpenMP: TRUE (found version "5.0")
-- Retrieving tblite from https://github.com/tblite/tblite
-- Looking for Fortran sgemm
-- Looking for Fortran sgemm - not found
-- Performing Test CMAKE_HAVE_LIBC_PTHREAD
-- Performing Test CMAKE_HAVE_LIBC_PTHREAD - Failed
-- Looking for pthread_create in pthreads
-- Looking for pthread_create in pthreads - not found
-- Looking for pthread_create in pthread
-- Looking for pthread_create in pthread - found
-- Found Threads: TRUE
-- Looking for Fortran sgemm
-- Looking for Fortran sgemm - found
-- Found BLAS: /cvmfs/hybrilit.jinr.ru/sw/slc7_x86-64/intel/oneapi/mkl/latest/lib/intel64/libmkl_intel_lp64.so;/cvmfs/hybrilit.jinr.ru/sw/slc7_x86-64/intel/oneapi/mkl/latest/lib/intel64/libmkl_intel_thread.so;/cvmfs/hybrilit.jinr.ru/sw/slc7_x86-64/intel/oneapi/mkl/latest/lib/intel64/libmkl_core.so;/cvmfs/hybrilit.jinr.ru/sw/slc7_x86-64/intel/oneapi/compiler/latest/linux/compiler/lib/intel64_lin/libiomp5.so;-lpthread;-lm;-ldl
-- Looking for Fortran cheev
-- Looking for Fortran cheev - found
-- Found LAPACK: /cvmfs/hybrilit.jinr.ru/sw/slc7_x86-64/intel/oneapi/mkl/latest/lib/intel64/libmkl_intel_lp64.so;/cvmfs/hybrilit.jinr.ru/sw/slc7_x86-64/intel/oneapi/mkl/latest/lib/intel64/libmkl_intel_thread.so;/cvmfs/hybrilit.jinr.ru/sw/slc7_x86-64/intel/oneapi/mkl/latest/lib/intel64/libmkl_core.so;/cvmfs/hybrilit.jinr.ru/sw/slc7_x86-64/intel/oneapi/compiler/latest/linux/compiler/lib/intel64_lin/libiomp5.so;-lpthread;-lm;-ldl;-lpthread;-lm;-ldl
-- mstore: Find installed package
-- Retrieving mstore from https://github.com/grimme-lab/mstore
-- toml-f: Find installed package
-- Retrieving toml-f from https://github.com/toml-f/toml-f
-- Retrieving test-drive from https://github.com/fortran-lang/test-drive
-- Performing Test WITH_QP
-- Performing Test WITH_QP - Failed
-- Performing Test WITH_XDP
-- Performing Test WITH_XDP - Failed
-- dftd4: Find installed package
-- Retrieving dftd4 from https://github.com/dftd4/dftd4
-- multicharge: Find installed package
-- Retrieving multicharge from https://github.com/grimme-lab/multicharge
-- s-dftd3: Find installed package
-- Retrieving s-dftd3 from https://github.com/dftd3/simple-dftd3
-- Retrieving cpcmx from https://github.com/grimme-lab/CPCM-X
-- Could NOT find numsa (missing: numsa_DIR)
-- Retrieving numsa from https://github.com/grimme-lab/numsa
-- Retrieving test-drive from https://github.com/fortran-lang/test-drive
-- Could NOT find toml-f (missing: toml-f_DIR)
-- Retrieving toml-f from https://github.com/toml-f/toml-f
-- Retrieving test-drive from https://github.com/fortran-lang/test-drive
-- Retrieving test-drive from https://github.com/fortran-lang/test-drive
-- Configuring done (634.0s)
-- Generating done (62.0s)
-- Build files have been written to: /lustre/home/user/m/milias/work/software/xtb/git_cloned/xtb/_build
milias@hydra.jinr.ru:~/work/software/xtb/git_cloned/xtb/.


milias@hydra.jinr.ru:~/work/software/xtb/git_cloned/xtb/.cmake -B_build -S. -GNinja -DCMAKE_BUILD_TYPE=Release --install-prefix /lustre/home/user/m/milias/work/software/xtb/git_cloned/install
-- Retrieving mctc-lib from https://github.com/grimme-lab/mctc-lib
-- Retrieving tblite from https://github.com/tblite/tblite
-- mstore: Find installed package
-- Retrieving mstore from https://github.com/grimme-lab/mstore
-- toml-f: Find installed package
-- Retrieving toml-f from https://github.com/toml-f/toml-f
-- Retrieving test-drive from https://github.com/fortran-lang/test-drive
-- dftd4: Find installed package
-- Retrieving dftd4 from https://github.com/dftd4/dftd4
-- multicharge: Find installed package
-- Retrieving multicharge from https://github.com/grimme-lab/multicharge
-- s-dftd3: Find installed package
-- Retrieving s-dftd3 from https://github.com/dftd3/simple-dftd3
-- Retrieving cpcmx from https://github.com/grimme-lab/CPCM-X
-- Could NOT find numsa (missing: numsa_DIR)
-- Retrieving numsa from https://github.com/grimme-lab/numsa
-- Retrieving test-drive from https://github.com/fortran-lang/test-drive
-- Could NOT find toml-f (missing: toml-f_DIR)
-- Retrieving toml-f from https://github.com/toml-f/toml-f
-- Retrieving test-drive from https://github.com/fortran-lang/test-drive
-- Retrieving test-drive from https://github.com/fortran-lang/test-drive
-- Configuring done (104.1s)

milias@hydra.jinr.ru:~/work/software/xtb/git_cloned/xtb/.ninja -C _build

see https://github.com/grimme-lab/xtb/issues/1346


