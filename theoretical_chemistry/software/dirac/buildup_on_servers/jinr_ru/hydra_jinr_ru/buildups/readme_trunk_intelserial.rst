============
DIRAC on GVR
============

milias@hydra.jinr.ru:~/work/software/dirac/trunk/.


Intel-serial
~~~~~~~~~~~~

milias@hydra.jinr.ru:~/work/software/dirac/trunk/build_ifort_mklpar_i8/.

milias@hydra.jinr.ru:~/work/software/dirac/trunk/.module add  intel/v2021.1  CMake/v3.29.2
milias@hydra.jinr.ru:~/work/software/dirac/trunk/.module list
Currently Loaded Modulefiles:
  1) GVR/v1.0-1      2) intel/v2021.1   3) BASE/1.0        4) CMake/v3.29.2

./setup --fc=ifort --mkl=parallel --int64 build_ifort_mklpar_i8

milias@vm02.hydra.local:~/work/software/dirac/trunk/../setup --fc=ifort --mkl=parallel --int64 build_ifort_mklpar_i8
cmake -DCMAKE_Fortran_COMPILER=ifort -DEXTRA_FCFLAGS="''" -DCMAKE_C_COMPILER=gcc -DEXTRA_CFLAGS="''" -DCMAKE_CXX_COMPILER=g++ -DEXTRA_CXXFLAGS="''" -DPREPROCESSOR_DEFINITIONS="''" -DPYTHON_INTERPRETER="''" -DENABLE_BLAS=auto -DENABLE_LAPACK=auto -DMKL_FLAG=parallel -DMATH_LIB_SEARCH_ORDER="MKL;ESSL;OPENBLAS;ATLAS;ACML;SYSTEM_NATIVE" -DBLAS_LANG=Fortran -DLAPACK_LANG=Fortran -DENABLE_MPI=False -DENABLE_OPENMP=True -DENABLE_CODE_COVERAGE=False -DENABLE_STATIC_LINKING=False -DENABLE_PROFILING=False -DENABLE_RUNTIMECHECK=False -DENABLE_64BIT_INTEGERS=True -DEXPLICIT_LIBS="off" -DENABLE_EXATENSOR=ON -DENABLE_PCMSOLVER=ON -DPCMSOLVER_ROOT='' -DCMAKE_BUILD_TYPE=release -G"Unix Makefiles" -H/lustre/home/user/m/milias/work/software/dirac/trunk -Bbuild_ifort_mklpar_i8

milias@hydra.jinr.ru:~/work/software/dirac/trunk/build_ifort_mklpar_i8/.


