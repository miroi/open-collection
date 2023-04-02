==============================
  NWChem on kelinux.saske.sk 
==============================

Modules
-------
ilias@login1.kelinux.saske.sk:~/work/qch/software/nwchem/nwchem-7.2.0/src/.module load imkl/2021.2.0-iimpi-2021a
ilias@login1.kelinux.saske.sk:~/work/qch/software/nwchem/nwchem-7.2.0/src/.module load ELPA/2021.11.001-foss-2022a 
ilias@login1.kelinux.saske.sk:~/work/qch/software/nwchem/nwchem-7.2.0/src/.module load ScaLAPACK

ilias@login1.kelinux.saske.sk:~/work/qch/software/nwchem/nwchem-7.2.0/src/.emkl
Intel MKL library ? MKLROOT=/lustre/home/utils/easybuild_old/software/imkl/2021.2.0-iimpi-2021a/mkl/2021.2.0

ilias@login1.kelinux.saske.sk:~/work/qch/software/nwchem/nwchem-7.2.0/src/.module list

Currently Loaded Modules:
  1) prun/1.3                                12) libxml2/2.9.13-GCCcore-11.3.0     23) UCC/1.0.0-GCCcore-11.3.0
  2) gnu7/7.3.0                              13) libpciaccess/0.16-GCCcore-11.3.0  24) OpenMPI/4.1.4-GCC-11.3.0
  3) openmpi3/3.1.0                          14) hwloc/2.7.1-GCCcore-11.3.0        25) OpenBLAS/0.3.20-GCC-11.3.0
  4) ohpc                                    15) OpenSSL/1.1                       26) FlexiBLAS/3.2.0-GCC-11.3.0
  5) intel-compilers/2021.2.0                16) libevent/2.1.12-GCCcore-11.3.0    27) FFTW/3.3.10-GCC-11.3.0
  6) impi/2021.2.0-intel-compilers-2021.2.0  17) GCCcore/11.3.0                    28) gompi/2022a
  7) iimpi/2021a                             18) zlib/1.2.12-GCCcore-11.3.0        29) FFTW.MPI/3.3.10-gompi-2022a
  8) imkl/2021.2.0-iimpi-2021a               19) numactl/2.0.14-GCCcore-11.3.0     30) foss/2022a
  9) binutils/2.38-GCCcore-11.3.0            20) UCX/1.12.1-GCCcore-11.3.0         31) ELPA/2021.11.001-foss-2022a
 10) GCC/11.3.0                              21) libfabric/1.15.1-GCCcore-11.3.0   32) ScaLAPACK/2.2.0-gompi-2022a-fb
 11) XZ/5.2.5-GCCcore-11.3.0                 22) PMIx/4.1.2-GCCcore-11.3.0


NWChem clone and variables setting
-----------------------------------
from https://nwchemgit.github.io/Compiling-NWChem.html :

git clone -b release-7-2-0 https://github.com/nwchemgit/nwchem.git nwchem-7.2.0

export NWCHEM_TOP=/lustre/home/ilias/work/qch/software/nwchem/nwchem-7.2.0
export NWCHEM_TARGET=LINUX64
export ARMCI_NETWORK=MPI-PR
export USE_MPI=y
export NWCHEM_MODULES="all python"
export USE_NOFSCHECK=TRUE
export USE_SCALAPACK=y
export BLAS_SIZE=8
export SCALAPACK_SIZE=8
export BLASOPT="-L${MKLROOT}/lib/intel64_lin -lmkl_blas95_ilp64 -lmkl_intel_ilp64 -lmkl_intel_thread -lmkl_core -liomp5 -lpthread -lm -ldl"
export LAPACK_LIB="-L${MKLROOT}/lib/intel64_lin -lmkl_lapack95_ilp64 -lmkl_intel_ilp64 -lmkl_intel_thread -lmkl_core -liomp5 -lpthread -lm -ldl"

make -j8
.
.

configure: WARNING: ScaLAPACK library not found, interfaces won't be defined
configure: WARNING: ELPA library not found, interfaces won't be defined
configure: WARNING: ELPA 2015 library not found, interfaces won't be defined
configure: WARNING: ELPA 2016 library not found, interfaces won't be defined
configure: WARNING: ELPA 2017 library not found, interfaces won't be defined
.
.
make[1]: Leaving directory '/lustre/home/ilias/work/qch/software/nwchem/nwchem-7.2.0/src' 
gfortran   -L/lustre/home/ilias/work/qch/software/nwchem/nwchem-7.2.0/lib/LINUX64 -L/lustre/home/ilias/work/qch/software/nwchem/nwchem-7.2.0/src/tools/install/lib  -o /lustre/home/ilias/work/qch/software/nwchem/nwchem-7.2.0/bin/LINUX64/nwchem nwchem.o stubs.o -lnwctask -lccsd -lmcscf -lselci -lmp2 -lmoints -lstepper -ldriver -loptim -lnwdft -lgradients -lcphf -lesp -lddscf -ldangchang -lguess -lhessian -lvib -lnwcutil -lrimp2 -lproperty -lsolvation -lnwints -lprepar -lnwmd -lnwpw -lofpw -lpaw -lpspw -lband -lnwpwlib -lcafe -lspace -lanalyze -lqhop -lpfft -ldplot -lnwpython -ldrdy -lvscf -lqmmm -lqmd -letrans -lpspw -ltce -lbq -lmm -lcons -lperfm -ldntmc -lccca -ldimqm -lfcidump -lgwmol -lnwcutil -lga -larmci -lpeigs -lperfm -lcons -lbq -lnwcutil    -L/lustre/home/utils/easybuild_old/software/imkl/2021.2.0-iimpi-2021a/mkl/2021.2.0/lib/intel64_lin -lmkl_lapack95_ilp64 -lmkl_intel_ilp64 -lmkl_intel_thread -lmkl_core -liomp5 -lpthread -lm -ldl -L/lustre/home/utils/easybuild_old/software/imkl/2021.2.0-iimpi-2021a/mkl/2021.2.0/lib/intel64_lin -lmkl_blas95_ilp64 -lmkl_intel_ilp64 -lmkl_intel_thread -lmkl_core -liomp5 -lpthread -lm -ldl  -L/lustre/home/utils/easybuild_old/software/OpenMPI/4.1.4-GCC-11.3.0/lib -L/lustre/home/utils/easybuild_old/software/hwloc/2.7.1-GCCcore-11.3.0/lib -L/lustre/home/utils/easybuild_old/software/libevent/2.1.12-GCCcore-11.3.0/lib -lmpi_usempif08 -lmpi_usempi_ignore_tkr -lmpi_mpifh -lmpi -L/lustre/home/utils/easybuild_old/software/hwloc/2.7.1-GCCcore-11.3.0/lib -lhwloc    -lcomex -lmpi_usempif08 -lmpi_usempi_ignore_tkr -lmpi_mpifh -lmpi -lhwloc -lmkl_blas95_ilp64 -lmkl_intel_ilp64 -lmkl_intel_thread -lmkl_core -liomp5 -lpthread -lm -ldl -lrt -lpthread -lm -lpthread  -lnwcutil  -L/usr/lib64 -lpython3.6m -lpthread -ldl  -lutil -lm  -Xlinker -export-dynamic
/bin/rm -f nwchem.o stubs.o

ilias@login1.kelinux.saske.sk:~/work/qch/software/nwchem/nwchem-7.2.0/bin/LINUX64/.ldd *
depend.x:
        linux-vdso.so.1 =>  (0x00007fff479ee000)
        libc.so.6 => /lib64/libc.so.6 (0x00007f1db0325000)
        /lib64/ld-linux-x86-64.so.2 (0x00007f1db06f3000)
nwchem:
        linux-vdso.so.1 =>  (0x00007fff9557d000)
        libmkl_intel_ilp64.so.1 => /lustre/home/utils/easybuild_old/software/imkl/2021.2.0-iimpi-2021a/mkl/2021.2.0/lib/intel64/libmkl_intel_ilp64.so.1 (0x00007f26a0d04000)
        libmkl_intel_thread.so.1 => /lustre/home/utils/easybuild_old/software/imkl/2021.2.0-iimpi-2021a/mkl/2021.2.0/lib/intel64/libmkl_intel_thread.so.1 (0x00007f269d40f000)
        libmkl_core.so.1 => /lustre/home/utils/easybuild_old/software/imkl/2021.2.0-iimpi-2021a/mkl/2021.2.0/lib/intel64/libmkl_core.so.1 (0x00007f2693e74000)
        libiomp5.so => /lustre/home/utils/easybuild_old/software/imkl/2021.2.0-iimpi-2021a/compiler/2021.2.0/linux/compiler/lib/intel64_lin/libiomp5.so (0x00007f2693a5d000)
        libpthread.so.0 => /lib64/libpthread.so.0 (0x00007f2693841000)
        libgfortran.so.5 => /lustre/home/utils/easybuild_old/software/GCCcore/11.3.0/lib64/libgfortran.so.5 (0x00007f2693594000)
        libm.so.6 => /lib64/libm.so.6 (0x00007f2693292000)
        libdl.so.2 => /lib64/libdl.so.2 (0x00007f269308e000)
        libmpi_usempif08.so.40 => /lustre/home/utils/easybuild_old/software/OpenMPI/4.1.4-GCC-11.3.0/lib/libmpi_usempif08.so.40 (0x00007f26a1ba1000)
        libmpi_usempi_ignore_tkr.so.40 => /lustre/home/utils/easybuild_old/software/OpenMPI/4.1.4-GCC-11.3.0/lib/libmpi_usempi_ignore_tkr.so.40 (0x00007f26a1b94000)
        libmpi_mpifh.so.40 => /lustre/home/utils/easybuild_old/software/OpenMPI/4.1.4-GCC-11.3.0/lib/libmpi_mpifh.so.40 (0x00007f26a1b28000)
        libmpi.so.40 => /lustre/home/utils/easybuild_old/software/OpenMPI/4.1.4-GCC-11.3.0/lib/libmpi.so.40 (0x00007f26a1a05000)
        libhwloc.so.15 => /lustre/home/utils/easybuild_old/software/hwloc/2.7.1-GCCcore-11.3.0/lib/libhwloc.so.15 (0x00007f2693030000)
        librt.so.1 => /lib64/librt.so.1 (0x00007f2692e28000)
        libpython3.6m.so.1.0 => /lib64/libpython3.6m.so.1.0 (0x00007f2692900000)
        libutil.so.1 => /lib64/libutil.so.1 (0x00007f26926fd000)
        libgcc_s.so.1 => /lustre/home/utils/easybuild_old/software/GCCcore/11.3.0/lib64/libgcc_s.so.1 (0x00007f26926e3000)
        libquadmath.so.0 => /lustre/home/utils/easybuild_old/software/GCCcore/11.3.0/lib64/libquadmath.so.0 (0x00007f269269a000)
        libc.so.6 => /lib64/libc.so.6 (0x00007f26922cc000)
        /lib64/ld-linux-x86-64.so.2 (0x00007f26a19d1000)
        libopen-rte.so.40 => /lustre/home/utils/easybuild_old/software/OpenMPI/4.1.4-GCC-11.3.0/lib/libopen-rte.so.40 (0x00007f2692214000)
        libopen-pal.so.40 => /lustre/home/utils/easybuild_old/software/OpenMPI/4.1.4-GCC-11.3.0/lib/libopen-pal.so.40 (0x00007f2692165000)
        libpciaccess.so.0 => /lustre/home/utils/easybuild_old/software/libpciaccess/0.16-GCCcore-11.3.0/lib/libpciaccess.so.0 (0x00007f26a19f6000)
        libxml2.so.2 => /lustre/home/utils/easybuild_old/software/libxml2/2.9.13-GCCcore-11.3.0/lib/libxml2.so.2 (0x00007f2691ff8000)
        libz.so.1 => /lustre/home/utils/easybuild_old/software/zlib/1.2.12-GCCcore-11.3.0/lib/libz.so.1 (0x00007f2691fde000)
        liblzma.so.5 => /lustre/home/utils/easybuild_old/software/XZ/5.2.5-GCCcore-11.3.0/lib/liblzma.so.5 (0x00007f2691fb5000)
        libevent_core-2.1.so.7 => /lustre/home/utils/easybuild_old/software/libevent/2.1.12-GCCcore-11.3.0/lib/libevent_core-2.1.so.7 (0x00007f2691f7e000)
        libevent_pthreads-2.1.so.7 => /lustre/home/utils/easybuild_old/software/libevent/2.1.12-GCCcore-11.3.0/lib/libevent_pthreads-2.1.so.7 (0x00007f2691f79000)


