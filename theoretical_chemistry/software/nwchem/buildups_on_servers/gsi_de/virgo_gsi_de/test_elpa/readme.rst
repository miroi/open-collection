Test ELPA spack module on Virgo
===============================

see  https://groups.google.com/g/nwchem-forum/c/OhWndXRuG6E/m/VhsZeLy7AAAJ

in milias@lxbk1135.gsi.de:/lustre/ukt/milias/work/projects/open-collection/theoretical_chemistry/software/nwchem/buildups_on_servers/gsi_de/virgo_gsi_de/test_elpa

Spack modules
~~~~~~~~~~~~~~
spack --version
0.19.0

spack load elpa%gcc target=x86_64; spack load gcc@10.2.0 target=x86_64;

which gfortran 
/cvmfs/vae.gsi.de/vae23/spack-0.19/opt/linux-debian10-x86_64/gcc-8.3.0/gcc-10.2.0-agxjp3zexhitnb3g6czo5p4im3hi74ht/bin/gfortran
gfortran --version
GNU Fortran (Spack GCC) 10.2.0


check: 
ls /cvmfs/vae.gsi.de/vae23/spack-0.19/opt/linux-debian10-x86_64/gcc-10.2.0/elpa-2021.11.001-uorwjue22nh7br4jthmt3lfugpeivfms/lib

milias@lxbk1135.gsi.de:/lustre/ukt/milias/work/projects/open-collection/theoretical_chemistry/software/nwchem/buildups_on_servers/gsi_de/virgo_gsi_de/test_elpa/.export LD_LIBRARY_PATH=/cvmfs/vae.gsi.de/vae23/spack-0.19/opt/linux-debian10-x86_64/gcc-10.2.0/elpa-2021.11.001-uorwjue22nh7br4jthmt3lfugpeivfms/lib

check: 
ls /cvmfs/vae.gsi.de/vae23/spack-0.19/opt/linux-debian10-x86_64/gcc-10.2.0/elpa-2021.11.001-uorwjue22nh7br4jthmt3lfugpeivfms/include/elpa_openmp-2021.11.001/modules

Compile 
~~~~~~~~
gfortran test_elpa.f90 -I /cvmfs/vae.gsi.de/vae23/spack-0.19/opt/linux-debian10-x86_64/gcc-10.2.0/elpa-2021.11.001-uorwjue22nh7br4jthmt3lfugpeivfms/include/elpa_openmp-2021.11.001/modules -L/cvmfs/vae.gsi.de/vae23/spack-0.19/opt/linux-debian10-x86_64/gcc-10.2.0/elpa-2021.11.001-uorwjue22nh7br4jthmt3lfugpeivfms/lib -lelpa_openmp 

ldd a.out 
        linux-vdso.so.1 (0x00007ffddf1ec000)
        libelpa_openmp.so.17 => /cvmfs/vae.gsi.de/vae23/spack-0.19/opt/linux-debian10-x86_64/gcc-10.2.0/elpa-2021.11.001-uorwjue22nh7br4jthmt3lfugpeivfms/lib/libelpa_openmp.so.17 (0x00007f55a472e000)
        libgfortran.so.5 => /cvmfs/vae.gsi.de/vae23/spack-0.19/opt/linux-debian10-x86_64/gcc-8.3.0/gcc-10.2.0-agxjp3zexhitnb3g6czo5p4im3hi74ht/lib64/libgfortran.so.5 (0x00007f55a4474000)
        libm.so.6 => /lib/x86_64-linux-gnu/libm.so.6 (0x00007f55a42e3000)
        libgcc_s.so.1 => /cvmfs/vae.gsi.de/vae23/spack-0.19/opt/linux-debian10-x86_64/gcc-8.3.0/gcc-10.2.0-agxjp3zexhitnb3g6czo5p4im3hi74ht/lib64/libgcc_s.so.1 (0x00007f55a42c8000)
        libquadmath.so.0 => /cvmfs/vae.gsi.de/vae23/spack-0.19/opt/linux-debian10-x86_64/gcc-8.3.0/gcc-10.2.0-agxjp3zexhitnb3g6czo5p4im3hi74ht/lib64/libquadmath.so.0 (0x00007f55a427f000)
        libc.so.6 => /lib/x86_64-linux-gnu/libc.so.6 (0x00007f55a40bd000)
        libscalapack.so => /cvmfs/vae.gsi.de/vae23/spack-0.19/opt/linux-debian10-x86_64/gcc-10.2.0/amdscalapack-3.2-zmrsnzmnifwusgdparcdnpdksnehsbcm/lib/libscalapack.so (0x00007f55a3b12000)
        libopenblas.so.0 => /cvmfs/vae.gsi.de/vae23/spack-0.19/opt/linux-debian10-x86_64/gcc-10.2.0/openblas-0.3.21-q7nhojttkz52xuf4zkxk7vvgllqnxh34/lib/libopenblas.so.0 (0x00007f55a1598000)
        libmpi_usempif08.so.40 => /cvmfs/vae.gsi.de/vae23/spack-0.19/opt/linux-debian10-x86_64/gcc-10.2.0/openmpi-4.1.5-phbdvrf3few3givo575jlifx6dhnfgk7/lib/libmpi_usempif08.so.40 (0x00007f55a1553000)
        libmpi_usempi_ignore_tkr.so.40 => /cvmfs/vae.gsi.de/vae23/spack-0.19/opt/linux-debian10-x86_64/gcc-10.2.0/openmpi-4.1.5-phbdvrf3few3givo575jlifx6dhnfgk7/lib/libmpi_usempi_ignore_tkr.so.40 (0x00007f55a1542000)
        libmpi_mpifh.so.40 => /cvmfs/vae.gsi.de/vae23/spack-0.19/opt/linux-debian10-x86_64/gcc-10.2.0/openmpi-4.1.5-phbdvrf3few3givo575jlifx6dhnfgk7/lib/libmpi_mpifh.so.40 (0x00007f55a14d1000)
        libmpi.so.40 => /cvmfs/vae.gsi.de/vae23/spack-0.19/opt/linux-debian10-x86_64/gcc-10.2.0/openmpi-4.1.5-phbdvrf3few3givo575jlifx6dhnfgk7/lib/libmpi.so.40 (0x00007f55a11af000)
        libgomp.so.1 => /cvmfs/vae.gsi.de/vae23/spack-0.19/opt/linux-debian10-x86_64/gcc-8.3.0/gcc-10.2.0-agxjp3zexhitnb3g6czo5p4im3hi74ht/lib64/libgomp.so.1 (0x00007f55a116e000)
        libpthread.so.0 => /lib/x86_64-linux-gnu/libpthread.so.0 (0x00007f55a114d000)
        /lib64/ld-linux-x86-64.so.2 (0x00007f55a48e9000)
        libopen-rte.so.40 => /cvmfs/vae.gsi.de/vae23/spack-0.19/opt/linux-debian10-x86_64/gcc-10.2.0/openmpi-4.1.5-phbdvrf3few3givo575jlifx6dhnfgk7/lib/libopen-rte.so.40 (0x00007f55a1023000)
        libopen-pal.so.40 => /cvmfs/vae.gsi.de/vae23/spack-0.19/opt/linux-debian10-x86_64/gcc-10.2.0/openmpi-4.1.5-phbdvrf3few3givo575jlifx6dhnfgk7/lib/libopen-pal.so.40 (0x00007f55a0f1c000)
        libucp.so.0 => /cvmfs/vae.gsi.de/vae23/spack-0.19/opt/linux-debian10-x86_64/gcc-10.2.0/ucx-1.9.0-6kcy2huctfmqanv3onro64z4fgcbbkdo/lib/libucp.so.0 (0x00007f55a0eb1000)
        libuct.so.0 => /cvmfs/vae.gsi.de/vae23/spack-0.19/opt/linux-debian10-x86_64/gcc-10.2.0/ucx-1.9.0-6kcy2huctfmqanv3onro64z4fgcbbkdo/lib/libuct.so.0 (0x00007f55a0e7f000)
        libucm.so.0 => /cvmfs/vae.gsi.de/vae23/spack-0.19/opt/linux-debian10-x86_64/gcc-10.2.0/ucx-1.9.0-6kcy2huctfmqanv3onro64z4fgcbbkdo/lib/libucm.so.0 (0x00007f55a0e65000)
        libucs.so.0 => /cvmfs/vae.gsi.de/vae23/spack-0.19/opt/linux-debian10-x86_64/gcc-10.2.0/ucx-1.9.0-6kcy2huctfmqanv3onro64z4fgcbbkdo/lib/libucs.so.0 (0x00007f55a0e1d000)
        libdl.so.2 => /lib/x86_64-linux-gnu/libdl.so.2 (0x00007f55a0e18000)
        libpmix.so.2 => /cvmfs/vae.gsi.de/vae23/spack-0.19/opt/linux-debian10-x86_64/gcc-10.2.0/pmix-3.2.2-xxu3bzsuuainkfraekzzagcl34owihxs/lib/libpmix.so.2 (0x00007f55a0cbd000)
        libnl-3.so.200 => /lib/x86_64-linux-gnu/libnl-3.so.200 (0x00007f55a0a9c000)
        libnl-route-3.so.200 => /usr/lib/x86_64-linux-gnu/libnl-route-3.so.200 (0x00007f55a0823000)
        librt.so.1 => /lib/x86_64-linux-gnu/librt.so.1 (0x00007f55a0819000)
        libutil.so.1 => /lib/x86_64-linux-gnu/libutil.so.1 (0x00007f55a0814000)
        libz.so.1 => /cvmfs/vae.gsi.de/vae23/spack-0.19/opt/linux-debian10-x86_64/gcc-10.2.0/zlib-1.2.13-xz6lqyiknxh5ofvyybzre2lrusx2u4o2/lib/libz.so.1 (0x00007f55a07fa000)
        libhwloc.so.15 => /cvmfs/vae.gsi.de/vae23/spack-0.19/opt/linux-debian10-x86_64/gcc-10.2.0/hwloc-2.8.0-rpajza4w5yeshrr7qnbtwiz7cgsc5y4l/lib/libhwloc.so.15 (0x00007f55a079a000)
        libevent_core-2.1.so.7 => /cvmfs/vae.gsi.de/vae23/spack-0.19/opt/linux-debian10-x86_64/gcc-10.2.0/libevent-2.1.12-yu6nwyorgmfg6msofxuhqqkijsdqakzp/lib/libevent_core-2.1.so.7 (0x00007f55a0762000)
        libevent_pthreads-2.1.so.7 => /cvmfs/vae.gsi.de/vae23/spack-0.19/opt/linux-debian10-x86_64/gcc-10.2.0/libevent-2.1.12-yu6nwyorgmfg6msofxuhqqkijsdqakzp/lib/libevent_pthreads-2.1.so.7 (0x00007f55a075d000)
        libnuma.so.1 => /cvmfs/vae.gsi.de/vae23/spack-0.19/opt/linux-debian10-x86_64/gcc-10.2.0/numactl-2.0.14-p4a7bukg5ydtffxqfb657wtifvblnefy/lib/libnuma.so.1 (0x00007f55a074d000)
        libmunge.so.2 => /cvmfs/vae.gsi.de/vae23/spack-0.19/opt/linux-debian10-x86_64/gcc-10.2.0/munge-0.5.13-siy6ee26a2hmclhy5a5vapfps4mb7jzm/lib/libmunge.so.2 (0x00007f55a0741000)
        libpciaccess.so.0 => /cvmfs/vae.gsi.de/vae23/spack-0.19/opt/linux-debian10-x86_64/gcc-10.2.0/libpciaccess-0.16-dcbydon6ydygdx25zfodcnxet7xjbvov/lib/libpciaccess.so.0 (0x00007f55a0733000)
        libxml2.so.2 => /cvmfs/vae.gsi.de/vae23/spack-0.19/opt/linux-debian10-x86_64/gcc-10.2.0/libxml2-2.10.1-uemmoahqov5jnjgtbzgjwh4gin47zj4o/lib/libxml2.so.2 (0x00007f55a05cd000)
        libatomic.so.1 => /cvmfs/vae.gsi.de/vae23/spack-0.19/opt/linux-debian10-x86_64/gcc-8.3.0/gcc-10.2.0-agxjp3zexhitnb3g6czo5p4im3hi74ht/lib64/libatomic.so.1 (0x00007f55a05c2000)
        liblzma.so.5 => /cvmfs/vae.gsi.de/vae23/spack-0.19/opt/linux-debian10-x86_64/gcc-10.2.0/xz-5.2.7-kfrl4tvfvwufmsoyu2hvml5i6n5z2br4/lib/liblzma.so.5 (0x00007f55a0596000)
        libiconv.so.2 => /cvmfs/vae.gsi.de/vae23/spack-0.19/opt/linux-debian10-x86_64/gcc-10.2.0/libiconv-1.16-r6z5bvhxgq7syjhkok6uiulvpxut5fab/lib/libiconv.so.2 (0x00007f55a0497000)


