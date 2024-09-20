==================
H2 with ase-nwchem
==================

WSL-Win11-VictusNB
~~~~~~~~~~~~~~~~~~

milias@Miro:/mnt/c/Users/miroi/OneDrive/Desktop/Work/projekty/open-collection/theoretical_chemistry/software/ase/servers/windows10_wsl/ase_nwchem_h2_run$ python3 ase_nwchem_h2_bfgs.py
[0] ARMCI Warning: Freed 1 leaked allocations
      Step     Time          Energy         fmax
BFGS:    0 11:52:14      -31.435218        2.2691
[0] ARMCI Warning: Freed 1 leaked allocations
BFGS:    1 11:52:15      -31.490762        0.3740
[0] ARMCI Warning: Freed 1 leaked allocations
BFGS:    2 11:52:16      -31.492780        0.0630
[0] ARMCI Warning: Freed 1 leaked allocations
BFGS:    3 11:52:17      -31.492837        0.0023

milias@Miro:~/work/projects/open-collection/theoretical_chemistry/software/nwchem-ase/runs/ase_nwchem_h2_run/.ase gui h2.traj

milias@Miro:~/work/projects/open-collection/theoretical_chemistry/software/nwchem-ase/runs/ase_nwchem_h2_run/.which nwchem.openmpi
/usr/bin/nwchem.openmpi
milias@Miro:~/work/projects/open-collection/theoretical_chemistry/software/nwchem-ase/runs/ase_nwchem_h2_run/.ldd  /usr/bin/nwchem.openmpi
        linux-vdso.so.1 (0x00007fff0d95b000)
        libscalapack-openmpi.so.2.1 => /lib/x86_64-linux-gnu/libscalapack-openmpi.so.2.1 (0x00007f8858a31000)
        liblapack.so.3 => /lib/x86_64-linux-gnu/liblapack.so.3 (0x00007f885836c000)
        libblas.so.3 => /lib/x86_64-linux-gnu/libblas.so.3 (0x00007f885830a000)
        libmpi_mpifh.so.40 => /lib/x86_64-linux-gnu/libmpi_mpifh.so.40 (0x00007f88582a4000)
        libmpi.so.40 => /lib/x86_64-linux-gnu/libmpi.so.40 (0x00007f885816d000)
        libpython3.10.so.1.0 => /lib/x86_64-linux-gnu/libpython3.10.so.1.0 (0x00007f8857b94000)
        libgfortran.so.5 => /lib/x86_64-linux-gnu/libgfortran.so.5 (0x00007f88578b9000)
        libm.so.6 => /lib/x86_64-linux-gnu/libm.so.6 (0x00007f88577d2000)
        libmvec.so.1 => /lib/x86_64-linux-gnu/libmvec.so.1 (0x00007f88576d5000)
        libgcc_s.so.1 => /lib/x86_64-linux-gnu/libgcc_s.so.1 (0x00007f88576b5000)
        libc.so.6 => /lib/x86_64-linux-gnu/libc.so.6 (0x00007f885748c000)
        libopenblas.so.0 => /lib/x86_64-linux-gnu/libopenblas.so.0 (0x00007f8855038000)
        libopen-pal.so.40 => /lib/x86_64-linux-gnu/libopen-pal.so.40 (0x00007f8854f85000)
        libopen-rte.so.40 => /lib/x86_64-linux-gnu/libopen-rte.so.40 (0x00007f8854ec8000)
        libhwloc.so.15 => /lib/x86_64-linux-gnu/libhwloc.so.15 (0x00007f8854e6c000)
        libexpat.so.1 => /lib/x86_64-linux-gnu/libexpat.so.1 (0x00007f8854e3b000)
        libz.so.1 => /lib/x86_64-linux-gnu/libz.so.1 (0x00007f8854e1f000)
        libquadmath.so.0 => /lib/x86_64-linux-gnu/libquadmath.so.0 (0x00007f8854dd7000)
        /lib64/ld-linux-x86-64.so.2 (0x00007f8868f32000)
        libevent_core-2.1.so.7 => /lib/x86_64-linux-gnu/libevent_core-2.1.so.7 (0x00007f8854da2000)
        libevent_pthreads-2.1.so.7 => /lib/x86_64-linux-gnu/libevent_pthreads-2.1.so.7 (0x00007f8854d9d000)
        libudev.so.1 => /lib/x86_64-linux-gnu/libudev.so.1 (0x00007f8854d73000)
