====================================
CUDA-Fortran-Book buildup on Govorun
====================================

make.logfile_Govorun-ampere_SAVED
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

mpif90 -O2  -o mpiDevices.out mpiDevices.cuf
/cvmfs/hybrilit.jinr.ru/sw/slc7_x86-64/cuda/v12.1/Linux_x86_64/23.5/comm_libs/openmpi/openmpi-3.1.5/bin/.bin/mpif90: error while loading shared libraries: librdmacm.so.1: cannot open shared object file: No such file or directory

0: ALLOCATE: 80 bytes requested; status = 35(CUDA driver version is insufficient for CUDA runtime version)


dgx
~~~
sbatch hydra_gpu-build_dgx.01 :

             JOBID PARTITION     NAME     USER    STATE       TIME TIME_LIMI  NODES NODELIST(REASON)
          13294514       dgx  CUDAFor   milias  PENDING       0:00   2:00:00      1 (launch failed requeued held)


