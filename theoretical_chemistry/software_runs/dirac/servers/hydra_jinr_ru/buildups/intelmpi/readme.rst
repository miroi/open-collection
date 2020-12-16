DIRAC on JINR
=============

Intel-MPI i8/mkl build
-----------------------
milias@hydra.jinr.ru:~/work/software/dirac/trunk_master/../setup --mpi  --int64 --mkl=parallel --fc=mpiifort --cc=mpiicc --cxx=mpiicpc  build_intelmpi_i8_mklpar

Intel-MPI i4/mkl=parallel build
-------------------------------
milias@hydra.jinr.ru:~/work/software/dirac/trunk_master/../setup --mpi   --mkl=parallel --fc=mpiifort --cc=mpiicc --cxx=mpiicpc  build_intelmpi_i4_mklpar

  DIRAC is failing with IntelMPI :

DIRAC pam run in /zfs/store5.hydra.local/user/m/milias/work/projects/open-collection/theoretical_chemistry/software_runs/dirac/servers/hydra_jinr_ru/builds

 ====  below this line is the stderr stream  ====
/cvmfs/hybrilit.jinr.ru/sw/slc7_x86-64/intel/v2019.3.199/compilers_and_libraries_2019.3.199/linux/mpi/intel64/bin/mpirun: line 103: 115440 Segmentation fault      (core dumped) mpiexec.hydra "$@" 0<&0

DIRAC pam run in /zfs/store5.hydra.local/user/m/milias/work/projects/open-collection/theoretical_chemistry/software_runs/dirac/servers/hydra_jinr_ru/builds

 ====  below this line is the stderr stream  ====
[mpiexec@n02p076.gvr.local] wait_proxies_to_terminate (../../../../../src/pm/i_hydra/mpiexec/intel/i_mpiexec.c:393): downstream from host n02p076 was killed by signal 8 (Floating point exception)
[mpiexec@n02p076.gvr.local] main (../../../../../src/pm/i_hydra/mpiexec/mpiexec.c:1957): assert (exitcodes != NULL) failed

