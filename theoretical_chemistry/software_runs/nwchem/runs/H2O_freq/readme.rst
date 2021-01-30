======
NWChem
======

https://github.com/nwchemgit/nwchem/wiki/Getting-Started


milias@194.160.44.72:~/work/projects/open-collection/theoretical_chemistry/software_runs/nwchem/runs/H2O_freq/.bash_ubuntu-kch_nw.01

  NWCHEM_EXECUTABLE=/usr/bin/nwchem
        linux-vdso.so.1 (0x00007ffe253a0000)
        libmpi_mpifh.so.40 => /usr/lib/x86_64-linux-gnu/libmpi_mpifh.so.40 (0x00007fcabd011000)
        libmpi.so.40 => /usr/lib/x86_64-linux-gnu/libmpi.so.40 (0x00007fcabceec000)
        libpthread.so.0 => /lib/x86_64-linux-gnu/libpthread.so.0 (0x00007fcabcec9000)
        libgfortran.so.5 => /usr/lib/x86_64-linux-gnu/libgfortran.so.5 (0x00007fcabcc01000)
        libm.so.6 => /lib/x86_64-linux-gnu/libm.so.6 (0x00007fcabcab2000)
        libmvec.so.1 => /lib/x86_64-linux-gnu/libmvec.so.1 (0x00007fcabca86000)
        libpython3.8.so.1.0 => /usr/lib/x86_64-linux-gnu/libpython3.8.so.1.0 (0x00007fcabc52e000)
        libc.so.6 => /lib/x86_64-linux-gnu/libc.so.6 (0x00007fcabc33c000)
        libopen-pal.so.40 => /usr/lib/x86_64-linux-gnu/libopen-pal.so.40 (0x00007fcabc28e000)
        libopen-rte.so.40 => /usr/lib/x86_64-linux-gnu/libopen-rte.so.40 (0x00007fcabc1d4000)
        libhwloc.so.15 => /usr/lib/x86_64-linux-gnu/libhwloc.so.15 (0x00007fcabc183000)
        /lib64/ld-linux-x86-64.so.2 (0x00007fcacd585000)
        libquadmath.so.0 => /usr/lib/x86_64-linux-gnu/libquadmath.so.0 (0x00007fcabc139000)
        libgcc_s.so.1 => /lib/x86_64-linux-gnu/libgcc_s.so.1 (0x00007fcabc11c000)
        libexpat.so.1 => /lib/x86_64-linux-gnu/libexpat.so.1 (0x00007fcabc0ee000)
        libz.so.1 => /lib/x86_64-linux-gnu/libz.so.1 (0x00007fcabc0d2000)
        libdl.so.2 => /lib/x86_64-linux-gnu/libdl.so.2 (0x00007fcabc0cc000)
        libutil.so.1 => /lib/x86_64-linux-gnu/libutil.so.1 (0x00007fcabc0c7000)
        libevent-2.1.so.7 => /usr/lib/x86_64-linux-gnu/libevent-2.1.so.7 (0x00007fcabc071000)
        libevent_pthreads-2.1.so.7 => /usr/lib/x86_64-linux-gnu/libevent_pthreads-2.1.so.7 (0x00007fcabc06a000)
        libudev.so.1 => /lib/x86_64-linux-gnu/libudev.so.1 (0x00007fcabc03d000)
        libltdl.so.7 => /usr/lib/x86_64-linux-gnu/libltdl.so.7 (0x00007fcabc032000)

 Scratch directory, TMPDIR=/tmp/milias/nwchem_run.f1be025e4918
Size of the scratch dir, df -h /tmp :
Filesystem      Size  Used Avail Use% Mounted on
/dev/nvme0n1p2  117G   58G   53G  53% /
Current working directory,  THISDIR=/home/milias/work/projects/open-collection/theoretical_chemistry/software_runs/nwchem/runs/H2O_freq

 Creating scratch dir,  mkdir -p /tmp/milias/nwchem_run.f1be025e4918

I am in newly created TMPDIR=/tmp/milias/nwchem_run.f1be025e4918
For control,  pwd=/tmp/milias/nwchem_run.f1be025e4918

 Checking : which mpirun ? /usr/bin/mpirun
mpirun (Open MPI) 4.0.3

Report bugs to http://www.open-mpi.org/community/help/

 Launching NWChem project h2o_freq_tasks on  2 CPU:
No protocol specified


 Working files in scratch dir /tmp/milias/nwchem_run.f1be025e4918:
total 956
-rw-r--r-- 1 milias UCITEL 917448 jan 30 19:58  h2o_freq.db
-rw-r--r-- 1 milias UCITEL    736 jan 30 19:58  h2o_freq.nmode
-rw-r--r-- 1 milias UCITEL    594 jan 30 19:58  h2o_freq.fd_ddipole
-rw-r--r-- 1 milias UCITEL    990 jan 30 19:58  h2o_freq.hess
-rw-r--r-- 1 milias UCITEL  11577 jan 30 19:58  h2o_freq.movecs
-rw-r--r-- 1 milias UCITEL  11577 jan 30 19:58  h2o_freq.mp2nos
-rw-r--r-- 1 milias UCITEL    240 jan 30 19:58  h2o_freq.b
-rw-r--r-- 1 milias UCITEL    240 jan 30 19:58 'h2o_freq.b^-1'
-rw-r--r-- 1 milias UCITEL     96 jan 30 19:58  h2o_freq.c
-rw-r--r-- 1 milias UCITEL     96 jan 30 19:58  h2o_freq.drv.hess
-rw-r--r-- 1 milias UCITEL     96 jan 30 19:58  h2o_freq.p
-rw-r--r-- 1 milias UCITEL     48 jan 30 19:58  h2o_freq.zmat
960K    /tmp/milias/nwchem_run.f1be025e4918
just for control -  pwd=/tmp/milias
total 32
drwxr-xr-x 2 milias UCITEL 4096 jan 30 19:58  nwchem_run.f1be025e4918
-rw-r--r-- 1 milias UCITEL   51 jan 30 12:35 'ADF_Geometry Optimization_default.tpl'
-rw-r--r-- 1 milias UCITEL   42 jan 30 12:34 'ADF_Single Point_default.tpl'
-rw-r--r-- 1 milias UCITEL   38 jan 29 12:20 'BAND_Geometry Optimization_default.tpl'
-rw-r--r-- 1 milias UCITEL   29 jan 29 12:12 'BAND_Single Point_default.tpl'
-rw-r--r-- 1 milias UCITEL   41 jan 20 16:38 'Quantum ESPRESSO_Geometry Optimization_default.tpl'
-rw-r--r-- 1 milias UCITEL   32 jan 20 16:38 'Quantum ESPRESSO_Single Point_default.tpl'
-rw-r--r-- 1 milias UCITEL   52 jan 19 15:24 'ForceField_Geometry Optimization_default.tpl'
-rw-r--r-- 1 milias UCITEL    0 jan 19 14:40  logfile

Deleting scratch directory /tmp/milias/nwchem_run.f1be025e4918:

 returning to /home/milias/work/projects/open-collection/theoretical_chemistry/software_runs/nwchem/runs/H2O_freq
milias@194.160.44.72:~/work/projects/open-collection/theoretical_chemistry/software_runs/nwchem/runs/H2O_freq/.



