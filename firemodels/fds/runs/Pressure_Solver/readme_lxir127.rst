milias@lxir127.gsi.de:/data.local1/milias/projects/open-collection/firemodels/fds/runs/Pressure_Solver/.ba            sh_run-lxir127.01

 Running  FDS ...

FI_PROVIDER_PATH=/data.local1/milias/software/fds-smv/bin/INTEL/prov
LD_LIBRARY_PATH=/data.local1/milias/software/fds-smv/bin/INTEL/lib:/usr/lib64:/cvmfs/vae.gsi.de/debian10/s            pack-0.17/opt/linux-debian10-broadwell/gcc-8.3.0/openssl-1.1.1l-npammwlyftckqstpzkaktzr2wx64efdh/lib:/cvmf            s/vae.gsi.de/debian10/spack-0.17/opt/linux-debian10-broadwell/gcc-8.3.0/zlib-1.2.11-pqdidq3pxucqbvyxnlf552            vxypl6zxvs/lib
PATH=/data.local1/milias/software/fds-smv/smvbin:/data.local1/milias/software/fds-smv/bin/INTEL/bin:/data.            local1/milias/software/fds-smv/bin:/cvmfs/vae.gsi.de/debian10/spack-0.17/opt/linux-debian10-broadwell/gcc-            8.3.0/cmake-3.21.4-ir3zrlgttevmqv4n3gg6ldkn4nf67ver/bin:/cvmfs/vae.gsi.de/debian10/spack-0.17/opt/linux-de            bian10-broadwell/gcc-8.3.0/openssl-1.1.1l-npammwlyftckqstpzkaktzr2wx64efdh/bin:/cvmfs/vae.gsi.de/debian10/            spack-0.17/vaesoft/spack/bin:/u/milias/.local/bin:/usr/sbin:/usr/local/bin:/usr/bin:/bin:/usr/local/games:            /usr/games:.
OMP_NUM_THREADS=4
position of fds : /data.local1/milias/software/fds-smv/bin/fds
linked libraries, ldd fds:
        linux-vdso.so.1 (0x00007ffc150ba000)
        libpthread.so.0 => /lib/x86_64-linux-gnu/libpthread.so.0 (0x00007f3651af3000)
        libm.so.6 => /lib/x86_64-linux-gnu/libm.so.6 (0x00007f3651970000)
        libdl.so.2 => /lib/x86_64-linux-gnu/libdl.so.2 (0x00007f365196b000)
        libmpifort.so.12 => /data.local1/milias/software/fds-smv/bin/INTEL/lib/libmpifort.so.12 (0x00007f3            6515b7000)
        libmpi.so.12 => /data.local1/milias/software/fds-smv/bin/INTEL/lib/libmpi.so.12 (0x00007f364fd6f00            0)
        librt.so.1 => /lib/x86_64-linux-gnu/librt.so.1 (0x00007f364fd63000)
        libc.so.6 => /lib/x86_64-linux-gnu/libc.so.6 (0x00007f364fba3000)
        /lib64/ld-linux-x86-64.so.2 (0x00007f3651b56000)
        libgcc_s.so.1 => /lib/x86_64-linux-gnu/libgcc_s.so.1 (0x00007f364fb89000)
MPIEXEC=/data.local1/milias/software/fds-smv/bin/INTEL/bin/mpiexec
Intel(R) MPI Library for Linux* OS, Version 2021.6 Build 20220227 (id: 28877f3f32)
Copyright 2003-2022, Intel Corporation.

 ldd /data.local1/milias/software/fds-smv/bin/INTEL/bin/mpiexec :
        linux-vdso.so.1 (0x00007fffa09af000)
        libdl.so.2 => /lib/x86_64-linux-gnu/libdl.so.2 (0x00007fb3e71f6000)
        libpthread.so.0 => /lib/x86_64-linux-gnu/libpthread.so.0 (0x00007fb3e71d5000)
        libm.so.6 => /lib/x86_64-linux-gnu/libm.so.6 (0x00007fb3e7052000)
        libgcc_s.so.1 => /lib/x86_64-linux-gnu/libgcc_s.so.1 (0x00007fb3e7038000)
        libc.so.6 => /lib/x86_64-linux-gnu/libc.so.6 (0x00007fb3e6e78000)
        /lib64/ld-linux-x86-64.so.2 (0x00007fb3e723d000)

 running /data.local1/milias/software/fds-smv/bin/INTEL/bin/mpiexec -n 4 /data.local1/milias/software/fds-            smv/bin/fds dancing_eddies_default.fds :

 Starting FDS ...

 MPI Process      1 started on lxir127
 MPI Process      3 started on lxir127
 MPI Process      0 started on lxir127
 MPI Process      2 started on lxir127

 Reading FDS input file ...


 Fire Dynamics Simulator

 Current Date     : October 17, 2022  21:19:17
 Revision         : FDS6.7.9-0-gec52dee42-release
 Revision Date    : Sun Jun 26 14:36:40 2022 -0400
 Compiler         : ifort version 2021.6.0
 Compilation Date : Jun 28, 2022 23:02:23

 MPI Enabled;    Number of MPI Processes:       4
 OpenMP Disabled

 MPI version: 3.1
 MPI library version: Intel(R) MPI Library 2021.6 for Linux* OS


 Job TITLE        : Simple 2D Tunnel
 Job ID string    : dancing_eddies_default

 Time Step:      1, Simulation Time:     0.004 s
 Time Step:      2, Simulation Time:     0.008 s
 Time Step:      3, Simulation Time:      0.01 s
 Time Step:      4, Simulation Time:      0.02 s
 Time Step:      5, Simulation Time:      0.02 s
 Time Step:      6, Simulation Time:      0.02 s
 Time Step:      7, Simulation Time:      0.03 s
 Time Step:      8, Simulation Time:      0.03 s
 Time Step:      9, Simulation Time:      0.04 s
 Time Step:     10, Simulation Time:      0.04 s
 Time Step:     20, Simulation Time:      0.08 s
 Time Step:     30, Simulation Time:      0.11 s
 Time Step:     40, Simulation Time:      0.13 s
 Time Step:     50, Simulation Time:      0.15 s
 Time Step:     60, Simulation Time:      0.17 s
 Time Step:     70, Simulation Time:      0.19 s
 Time Step:     80, Simulation Time:      0.20 s
 Time Step:     90, Simulation Time:      0.22 s
 Time Step:    100, Simulation Time:      0.23 s
 Time Step:    200, Simulation Time:      0.34 s
 Time Step:    300, Simulation Time:      0.42 s
 Time Step:    400, Simulation Time:      0.49 s
 Time Step:    500, Simulation Time:      0.56 s
 Time Step:    600, Simulation Time:      0.62 s
 Time Step:    700, Simulation Time:      0.67 s
 Time Step:    800, Simulation Time:      0.72 s
 Time Step:    900, Simulation Time:      0.77 s
 Time Step:   1000, Simulation Time:      0.82 s
 Time Step:   1100, Simulation Time:      0.87 s
 Time Step:   1200, Simulation Time:      0.91 s
 Time Step:   1300, Simulation Time:      0.95 s
 Time Step:   1400, Simulation Time:      0.99 s
 Time Step:   1500, Simulation Time:      1.03 s
 Time Step:   1600, Simulation Time:      1.07 s
 Time Step:   1700, Simulation Time:      1.11 s
 Time Step:   1800, Simulation Time:      1.15 s
 Time Step:   1900, Simulation Time:      1.18 s
 Time Step:   2000, Simulation Time:      1.22 s
 Time Step:   2100, Simulation Time:      1.25 s
 Time Step:   2200, Simulation Time:      1.28 s
 Time Step:   2300, Simulation Time:      1.31 s
 Time Step:   2400, Simulation Time:      1.34 s
 Time Step:   2500, Simulation Time:      1.37 s
 Time Step:   2600, Simulation Time:      1.40 s
 Time Step:   2700, Simulation Time:      1.42 s
 Time Step:   2800, Simulation Time:      1.45 s
 Time Step:   2900, Simulation Time:      1.48 s
 Time Step:   3000, Simulation Time:      1.50 s
 Time Step:   3100, Simulation Time:      1.53 s
 Time Step:   3200, Simulation Time:      1.55 s
 Time Step:   3300, Simulation Time:      1.58 s
 Time Step:   3400, Simulation Time:      1.60 s
 Time Step:   3500, Simulation Time:      1.63 s
 Time Step:   3600, Simulation Time:      1.65 s
 Time Step:   3700, Simulation Time:      1.68 s
 Time Step:   3800, Simulation Time:      1.70 s
 Time Step:   3900, Simulation Time:      1.72 s
 Time Step:   4000, Simulation Time:      1.75 s
 Time Step:   4100, Simulation Time:      1.77 s
 Time Step:   4200, Simulation Time:      1.80 s
 Time Step:   4300, Simulation Time:      1.82 s
 Time Step:   4400, Simulation Time:      1.84 s
 Time Step:   4500, Simulation Time:      1.87 s
 Time Step:   4600, Simulation Time:      1.89 s
 Time Step:   4700, Simulation Time:      1.91 s
 Time Step:   4800, Simulation Time:      1.94 s
 Time Step:   4900, Simulation Time:      1.96 s
 Time Step:   5000, Simulation Time:      1.98 s
 Time Step:   5063, Simulation Time:      2.00 s

STOP: FDS completed successfully (CHID: dancing_eddies_default)

milias@lxir127.gsi.de:/data.local1/milias/projects/open-collection/firemodels/fds/runs/Pressure_Solver/.ls
bash_run-labs.01*                  dancing_eddies_default_2_4.sf      dancing_eddies_default_4_3.sf
bash_run-lxir127.01*               dancing_eddies_default_2_4.sf.bnd  dancing_eddies_default_4_3.sf.bnd
dancing_eddies_default_1_1.sf      dancing_eddies_default_2_5.sf      dancing_eddies_default_4_4.sf
dancing_eddies_default_1_1.sf.bnd  dancing_eddies_default_2_5.sf.bnd  dancing_eddies_default_4_4.sf.bnd
dancing_eddies_default_1_2.sf      dancing_eddies_default_3_1.sf      dancing_eddies_default_4_5.sf
dancing_eddies_default_1_2.sf.bnd  dancing_eddies_default_3_1.sf.bnd  dancing_eddies_default_4_5.sf.bnd
dancing_eddies_default_1_3.sf      dancing_eddies_default_3_2.sf      dancing_eddies_default.binfo
dancing_eddies_default_1_3.sf.bnd  dancing_eddies_default_3_2.sf.bnd  dancing_eddies_default_cpu.csv
dancing_eddies_default_1_4.sf      dancing_eddies_default_3_3.sf      dancing_eddies_default_devc.csv
dancing_eddies_default_1_4.sf.bnd  dancing_eddies_default_3_3.sf.bnd  dancing_eddies_default.end
dancing_eddies_default_1_5.sf      dancing_eddies_default_3_4.sf      dancing_eddies_default.fds
dancing_eddies_default_1_5.sf.bnd  dancing_eddies_default_3_4.sf.bnd  dancing_eddies_default_git.txt
dancing_eddies_default_2_1.sf      dancing_eddies_default_3_5.sf      dancing_eddies_default_hrr.csv
dancing_eddies_default_2_1.sf.bnd  dancing_eddies_default_3_5.sf.bnd  dancing_eddies_default.out
dancing_eddies_default_2_2.sf      dancing_eddies_default_4_1.sf      dancing_eddies_default.sinfo
dancing_eddies_default_2_2.sf.bnd  dancing_eddies_default_4_1.sf.bnd  dancing_eddies_default.smv
dancing_eddies_default_2_3.sf      dancing_eddies_default_4_2.sf      dancing_eddies_default_steps.csv
dancing_eddies_default_2_3.sf.bnd  dancing_eddies_default_4_2.sf.bnd  readme.rst

