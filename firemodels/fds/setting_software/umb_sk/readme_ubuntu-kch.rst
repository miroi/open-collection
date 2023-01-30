=================
FDS on ubuntu-kch
=================

milias@194.160.44.72:~/work/software/fds/fds-FDS6.7.9/Build/ompi_gnu_linux/make_fds.sh
.
.
.
mpifort -c -m64 -O2 -std=f2018 -frecursive -ffpe-summary=none -fall-intrinsics -cpp -DGITHASH_PP=\"-\" -DGITDATE_PP=\""\"" -DBUILDDATE_PP=\""jan 28, 2023  18:42:05\"" -DCOMPVER_PP=\""Gnu gfortran 11.3.0-1ubuntu1~22.04)"\"   -fopenmp ../../Source/main.f90
mpifort -m64 -O2 -std=f2018 -frecursive -ffpe-summary=none -fall-intrinsics -cpp -DGITHASH_PP=\"-\" -DGITDATE_PP=\""\"" -DBUILDDATE_PP=\""jan 28, 2023  18:42:05\"" -DCOMPVER_PP=\""Gnu gfortran 11.3.0-1ubuntu1~22.04)"\"   -fopenmp -o fds_ompi_gnu_linux prec.o cons.o devc.o type.o data.o mesh.o func.o gsmv.o smvv.o rcal.o turb.o soot.o pois.o geom.o ccib.o radi.o part.o vege.o ctrl.o hvac.o mass.o wall.o fire.o velo.o scrc.o pres.o init.o dump.o read.o divg.o main.o 
milias@194.160.44.72:~/work/software/fds/fds-FDS6.7.9/Build/ompi_gnu_linux/.
milias@194.160.44.72:~/work/software/fds/fds-FDS6.7.9/Build/ompi_gnu_linux/.ldd fds_ompi_gnu_linux
	linux-vdso.so.1 (0x00007ffebffcd000)
	libmpi_usempif08.so.40 => /lib/x86_64-linux-gnu/libmpi_usempif08.so.40 (0x00007f9f34c8b000)
	libmpi.so.40 => /lib/x86_64-linux-gnu/libmpi.so.40 (0x00007f9f34b54000)
	libgfortran.so.5 => /lib/x86_64-linux-gnu/libgfortran.so.5 (0x00007f9f34879000)
	libm.so.6 => /lib/x86_64-linux-gnu/libm.so.6 (0x00007f9f34792000)
	libgomp.so.1 => /lib/x86_64-linux-gnu/libgomp.so.1 (0x00007f9f34748000)
	libgcc_s.so.1 => /lib/x86_64-linux-gnu/libgcc_s.so.1 (0x00007f9f34726000)
	libc.so.6 => /lib/x86_64-linux-gnu/libc.so.6 (0x00007f9f344fe000)
	libmpi_mpifh.so.40 => /lib/x86_64-linux-gnu/libmpi_mpifh.so.40 (0x00007f9f34498000)
	libopen-rte.so.40 => /lib/x86_64-linux-gnu/libopen-rte.so.40 (0x00007f9f343db000)
	libopen-pal.so.40 => /lib/x86_64-linux-gnu/libopen-pal.so.40 (0x00007f9f34328000)
	libhwloc.so.15 => /lib/x86_64-linux-gnu/libhwloc.so.15 (0x00007f9f342ca000)
	libquadmath.so.0 => /lib/x86_64-linux-gnu/libquadmath.so.0 (0x00007f9f34282000)
	/lib64/ld-linux-x86-64.so.2 (0x00007f9f35367000)
	libz.so.1 => /lib/x86_64-linux-gnu/libz.so.1 (0x00007f9f34266000)
	libevent_core-2.1.so.7 => /lib/x86_64-linux-gnu/libevent_core-2.1.so.7 (0x00007f9f34231000)
	libevent_pthreads-2.1.so.7 => /lib/x86_64-linux-gnu/libevent_pthreads-2.1.so.7 (0x00007f9f3422c000)
	libudev.so.1 => /lib/x86_64-linux-gnu/libudev.so.1 (0x00007f9f34200000)
#
milias@194.160.44.72:~/work/software/fds/fds-FDS6.7.9/Build/ompi_gnu_linux/.fds_ompi_gnu_linux 

 Fire Dynamics Simulator

 Current Date     : January 28, 2023  18:46:38
 Revision         : -
 Revision Date    : 
 Compiler         : Gnu gfortran 11.3.0-1ubuntu1~22.04)
 Compilation Date : jan 28, 2023  18:42:05

 MPI Enabled;    Number of MPI Processes:       1
 OpenMP Enabled; Number of OpenMP Threads:      4

 MPI version: 3.1
 MPI library version: Open MPI v4.1.2, package: Debian OpenMPI, ident: 4.1.2, repo rev: v4.1.2, Nov 24, 2021
 Consult FDS Users Guide Chapter, Running FDS, for further instructions.

