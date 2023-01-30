============================
FDS installation on HPCC UMB
============================

OpenMPI first
-------------
 ##############################################################################################
 #          My newest OpenMPI-4.1.4 GNU 11.2.1 installation
 #         -------------------------------------------------
 #  milias@login.grid.umb.sk:~/bin/openmpi/openmpi-4.1.4_gnu11.2.1/../configure --prefix=$PWD CXX=g++ CC=gcc F77=gfortran FC=gfortran
 # extend_string PATH             /home/milias/bin/openmpi/openmpi-4.1.4_gnu11.2.1/bin          $PATH
 #  extend_string MANPATH          /home/milias/bin/openmpi/openmpi-4.1.4_gnu11.2.1/share/man    $MANPATH
 #  extend_string LD_LIBRARY_PATH  /home/milias/bin/openmpi/openmpi-4.1.4_gnu11.2.1/lib          $LD_LIBRARY_PATH
 #  echo -e "\n  OpenMPI-4.1.4 GNU 11.2.1 variables PATH,MANPATH,LD_LIBRARY_PATH activated ! In /home/milias/bin/openmpi/openmpi-4.1.4_gnu11.2.1 ...  "
 ################################################################################################

 Then compile FDS
-------------------

module purge
export PATH=/home/milias/bin/openmpi/openmpi-4.1.4_gnu11.2.1/bin:$PATH
export LD_LIBRARY_PATH=/home/milias/bin/openmpi/openmpi-4.1.4_gnu11.2.1/lib:$LD_LIBRARY_PATH

ep
elp

milias@login.grid.umb.sk:~/Work/software/firemodels/fds-FDS6.7.9/Build/ompi_gnu_linux/.mpirun --version
mpirun (Open MPI) 4.1.4

milias@login.grid.umb.sk:~/Work/software/firemodels/fds-FDS6.7.9/Build/ompi_gnu_linux/.mpifort --version
GNU Fortran (GCC) 11.2.1 20220127 (Red Hat 11.2.1-9)

milias@login.grid.umb.sk:~/Work/software/firemodels/.wget https://github.com/firemodels/fds/archive/refs/tags/FDS6.7.9.zip
milias@login.grid.umb.sk:~/Work/software/firemodels/fds-FDS6.7.9/Build/ompi_gnu_linux/../make_fds.sh
.
.
mpifort -c -m64 -O2 -std=f2018 -frecursive -ffpe-summary=none -fall-intrinsics -cpp -DGITHASH_PP=\"-\" -DGITDATE_PP=\""\"" -DBUILDDATE_PP=\""Jan 30, 2023  17:27:37\"" -DCOMPVER_PP=\""Gnu gfortran 11.2.1"\" -DWITH_MKL -I/mnt/apps/intel/composer_xe_2013_sp1.1.106/mkl/include  ../../Source/cons.f90
.
.
problem https://github.com/firemodels/fds/issues/11404

Solved
------

use fresh git version; deactivate MKLROOT (unset MKLROOT)

milias@login.grid.umb.sk:~/Work/software/firemodels/fds_cloned/Build/ompi_gnu_linux/.make_fds.sh
.
.
mpifort -c -m64 -O2 -std=f2018 -frecursive -ffpe-summary=none -fall-intrinsics -cpp -DGITHASH_PP=\"FDS6.7.9-1550-g98e6b0d8a-master\" -DGITDATE_PP=\""Mon Jan 30 11:42:58 2023 -0500\"" -DBUILDDATE_PP=\""Jan 30, 2023  18:34:34\"" -DCOMPVER_PP=\""Gnu gfortran 11.2.1"\"   -fopenmp ../../Source/main.f90
mpifort -m64 -O2 -std=f2018 -frecursive -ffpe-summary=none -fall-intrinsics -cpp -DGITHASH_PP=\"FDS6.7.9-1550-g98e6b0d8a-master\" -DGITDATE_PP=\""Mon Jan 30 11:42:58 2023 -0500\"" -DBUILDDATE_PP=\""Jan 30, 2023  18:34:34\"" -DCOMPVER_PP=\""Gnu gfortran 11.2.1"\"   -fopenmp -o fds_ompi_gnu_linux prec.o cons.o devc.o type.o data.o mesh.o func.o gsmv.o smvv.o rcal.o turb.o soot.o pois.o geom.o ccib.o radi.o part.o vege.o ctrl.o hvac.o mass.o wall.o fire.o velo.o pres.o init.o dump.o read.o divg.o main.o
milias@login.grid.umb.sk:~/Work/software/firemodels/fds_cloned/Build/ompi_gnu_linux/.ldd fds_ompi_gnu_linux
        linux-vdso.so.1 =>  (0x00007ffc18bb1000)
        libmpi_usempif08.so.40 => /home/milias/bin/openmpi/openmpi-4.1.4_gnu11.2.1/lib/libmpi_usempif08.so.40 (0x00007f710c6da000)
        libmpi_usempi_ignore_tkr.so.40 => /home/milias/bin/openmpi/openmpi-4.1.4_gnu11.2.1/lib/libmpi_usempi_ignore_tkr.so.40 (0x00007f710c6cb000)
        libmpi_mpifh.so.40 => /home/milias/bin/openmpi/openmpi-4.1.4_gnu11.2.1/lib/libmpi_mpifh.so.40 (0x00007f710c666000)
        libmpi.so.40 => /home/milias/bin/openmpi/openmpi-4.1.4_gnu11.2.1/lib/libmpi.so.40 (0x00007f710c52d000)
        libgfortran.so.5 => /lib64/libgfortran.so.5 (0x00007f710c070000)
        libm.so.6 => /lib64/libm.so.6 (0x00007f710bd6e000)
        libgomp.so.1 => /lib64/libgomp.so.1 (0x00007f710bb48000)
        libgcc_s.so.1 => /lib64/libgcc_s.so.1 (0x00007f710b932000)
        libquadmath.so.0 => /lib64/libquadmath.so.0 (0x00007f710b6f6000)
        libpthread.so.0 => /lib64/libpthread.so.0 (0x00007f710b4da000)
        libc.so.6 => /lib64/libc.so.6 (0x00007f710b10c000)
        libopen-rte.so.40 => /home/milias/bin/openmpi/openmpi-4.1.4_gnu11.2.1/lib/libopen-rte.so.40 (0x00007f710b052000)
        libopen-pal.so.40 => /home/milias/bin/openmpi/openmpi-4.1.4_gnu11.2.1/lib/libopen-pal.so.40 (0x00007f710af47000)
        libdl.so.2 => /lib64/libdl.so.2 (0x00007f710ad43000)
        librt.so.1 => /lib64/librt.so.1 (0x00007f710ab3b000)
        libutil.so.1 => /lib64/libutil.so.1 (0x00007f710a938000)
        libz.so.1 => /lib64/libz.so.1 (0x00007f710a722000)
        /lib64/ld-linux-x86-64.so.2 (0x00007f710c4fb000)



