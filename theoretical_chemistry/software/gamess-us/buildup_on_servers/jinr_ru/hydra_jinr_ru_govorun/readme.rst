============================
GAMESS-US buildup on Govorun
============================


milias@hydra.jinr.ru:/zfs/scratch/HybriLITWorkshop2025/milias/software/gamess-us/gamess/.

interactive configure
~~~~~~~~~~~~~~~~~~~~~

module add Python/v3.10.13
module add intel/oneapi

please enter your target machine name: linux64
Setting up GAMESS compile and link for GMS_TARGET=linux64
GAMESS software is located at GMS_PATH=/zfs/scratch/HybriLITWorkshop2025/milias/software/gamess-us/gamess
GAMESS build directory? [/zfs/scratch/HybriLITWorkshop2025/milias/software/gamess-us/gamess]
HPC system target for 64-bit Linux system: <ENTER>      - none
Please enter your choice of FORTRAN: oneapi-ifort
Enter your math library choice from one of the options below: mkl
Math library 'mkl' will be taken from /cvmfs/hybrilit.jinr.ru/sw/slc7_x86-64/intel/oneapi/mkl/latest/lib/intel64

communication library ('serial','sockets' or 'mpi' or 'mixed')? sockets

Enter MPI library (hpcx, impi, mpich, mvapich2, mpt, openmpi, sockets): impi
MPI library 'impi' will be taken from /cvmfs/hybrilit.jinr.ru/sw/slc7_x86-64/intel/oneapi/mpi/latest

no plugins !

Your configuration for GAMESS compilation is in
     /zfs/scratch/HybriLITWorkshop2025/milias/software/gamess-us/gamess/install.info

milias@hydra.jinr.ru:/zfs/scratch/HybriLITWorkshop2025/milias/software/gamess-us/gamess/.make -j4


compile
~~~~~~~~
sbatch hydra_slurm_gamess-us-compile.01

ldd with impi:
~~~~~~~~~~~~~~
milias@hydra.jinr.ru:/zfs/scratch/HybriLITWorkshop2025/milias/software/gamess-us/gamess/.ldd gamess.00.x
        linux-vdso.so.1 =>  (0x00007ffc9e1e8000)
        libmpifort.so.12 => /cvmfs/hybrilit.jinr.ru/sw/slc7_x86-64/intel/oneapi/mpi/latest/lib/libmpifort.so.12 (0x00007ff718fd4000)
        librt.so.1 => /lib64/librt.so.1 (0x00007ff718dcc000)
        libmpi.so.12 => /cvmfs/hybrilit.jinr.ru/sw/slc7_x86-64/intel/oneapi/mpi/latest/lib/release/libmpi.so.12 (0x00007ff7176fc000)
        libpthread.so.0 => /lib64/libpthread.so.0 (0x00007ff7174e0000)
        libmpi_ilp64.so => /cvmfs/hybrilit.jinr.ru/sw/slc7_x86-64/intel/oneapi/mpi/latest/lib/release/libmpi_ilp64.so (0x00007ff71729a000)
        libdl.so.2 => /lib64/libdl.so.2 (0x00007ff717096000)
        libm.so.6 => /lib64/libm.so.6 (0x00007ff716d94000)
        libc.so.6 => /lib64/libc.so.6 (0x00007ff7169c6000)
        /lib64/ld-linux-x86-64.so.2 (0x00007ff719388000)
        libgcc_s.so.1 => /lib64/libgcc_s.so.1 (0x00007ff7167b0000)

ldd with sockets
~~~~~~~~~~~~~~~~
milias@hydra.jinr.ru:/zfs/scratch/HybriLITWorkshop2025/milias/software/gamess-us/gamess/.ldd gamess.00.x
        linux-vdso.so.1 =>  (0x00007ffeae545000)
        libpthread.so.0 => /lib64/libpthread.so.0 (0x00007f96a3678000)
        libm.so.6 => /lib64/libm.so.6 (0x00007f96a3376000)
        libc.so.6 => /lib64/libc.so.6 (0x00007f96a2fa8000)
        /lib64/ld-linux-x86-64.so.2 (0x00007f96a3894000)
        libgcc_s.so.1 => /lib64/libgcc_s.so.1 (0x00007f96a2d92000)
        libdl.so.2 => /lib64/libdl.so.2 (0x00007f96a2b8e000)


tests
~~~~~
runall 00

milias@hydra.jinr.ru:/zfs/scratch/HybriLITWorkshop2025/milias/software/gamess-us/gamess/.tests/standard/checktst
.
.
.
All 49 test results are correct!


