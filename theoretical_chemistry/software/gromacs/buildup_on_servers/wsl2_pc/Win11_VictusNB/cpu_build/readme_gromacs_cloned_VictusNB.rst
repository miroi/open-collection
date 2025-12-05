=======
GROMACS
=======

cloning
-------
miroi@MIRO:~/work/software/gromacs/.git clone git@gitlab.com:gromacs/gromacs.git gromacs_cloned

installation
------------
miroi@MIRO:~/work/software/gromacs/gromacs_cloned/build_gnu/.cmake ..
make -j4

miroi@MIRO:~/work/software/gromacs/gromacs_cloned/build_gnu/.ldd bin/gmx
        linux-vdso.so.1 (0x00007ffec4d06000)
        libgromacs.so.11 => /home/miroi/work/software/gromacs/gromacs_cloned/build_gnu/bin/../lib/libgromacs.so.11 (0x00007a706aa00000)
        libstdc++.so.6 => /lib/x86_64-linux-gnu/libstdc++.so.6 (0x00007a706a600000)
        libgcc_s.so.1 => /lib/x86_64-linux-gnu/libgcc_s.so.1 (0x00007a706c475000)
        libc.so.6 => /lib/x86_64-linux-gnu/libc.so.6 (0x00007a706a200000)
        libfftw3f.so.3 => /lib/x86_64-linux-gnu/libfftw3f.so.3 (0x00007a7069e00000)
        libmkl_intel_lp64.so => /lib/x86_64-linux-gnu/libmkl_intel_lp64.so (0x00007a7069000000)
        libmkl_intel_thread.so => /lib/x86_64-linux-gnu/libmkl_intel_thread.so (0x00007a7065600000)
        libmkl_core.so => /lib/x86_64-linux-gnu/libmkl_core.so (0x00007a7060e00000)
        libomp.so.5 => /lib/x86_64-linux-gnu/libomp.so.5 (0x00007a706c346000)
        libm.so.6 => /lib/x86_64-linux-gnu/libm.so.6 (0x00007a706a917000)
        libhdf5_serial.so.103 => /lib/x86_64-linux-gnu/libhdf5_serial.so.103 (0x00007a7060a00000)
        libmuparser.so.2 => /home/miroi/work/software/gromacs/gromacs_cloned/build_gnu/bin/../lib/../lib/libmuparser.so.2 (0x00007a706a8b8000)
        /lib64/ld-linux-x86-64.so.2 (0x00007a706c4d5000)
        libdl.so.2 => /lib/x86_64-linux-gnu/libdl.so.2 (0x00007a706c33f000)
        libpthread.so.0 => /lib/x86_64-linux-gnu/libpthread.so.0 (0x00007a706c33a000)
        libcrypto.so.3 => /lib/x86_64-linux-gnu/libcrypto.so.3 (0x00007a7060400000)
        libcurl.so.4 => /lib/x86_64-linux-gnu/libcurl.so.4 (0x00007a706a53f000)
        libsz.so.2 => /lib/x86_64-linux-gnu/libsz.so.2 (0x00007a706c333000)
        libz.so.1 => /lib/x86_64-linux-gnu/libz.so.1 (0x00007a706a89c000)
        libgomp.so.1 => /lib/x86_64-linux-gnu/libgomp.so.1 (0x00007a706a4e9000)
        libnghttp2.so.14 => /lib/x86_64-linux-gnu/libnghttp2.so.14 (0x00007a706a4be000)
        libidn2.so.0 => /lib/x86_64-linux-gnu/libidn2.so.0 (0x00007a706a49c000)
        librtmp.so.1 => /lib/x86_64-linux-gnu/librtmp.so.1 (0x00007a706a87e000)
        libssh.so.4 => /lib/x86_64-linux-gnu/libssh.so.4 (0x00007a706a42b000)
        libpsl.so.5 => /lib/x86_64-linux-gnu/libpsl.so.5 (0x00007a706a417000)
        libssl.so.3 => /lib/x86_64-linux-gnu/libssl.so.3 (0x00007a706a156000)
        libgssapi_krb5.so.2 => /lib/x86_64-linux-gnu/libgssapi_krb5.so.2 (0x00007a706a102000)
        libldap.so.2 => /lib/x86_64-linux-gnu/libldap.so.2 (0x00007a706a0a4000)
        liblber.so.2 => /lib/x86_64-linux-gnu/liblber.so.2 (0x00007a706c31f000)
        libzstd.so.1 => /lib/x86_64-linux-gnu/libzstd.so.1 (0x00007a7069d46000)
        libbrotlidec.so.1 => /lib/x86_64-linux-gnu/libbrotlidec.so.1 (0x00007a706a096000)
        libaec.so.0 => /lib/x86_64-linux-gnu/libaec.so.0 (0x00007a706a08d000)
        libunistring.so.5 => /lib/x86_64-linux-gnu/libunistring.so.5 (0x00007a7065453000)
        libgnutls.so.30 => /lib/x86_64-linux-gnu/libgnutls.so.30 (0x00007a7060206000)
        libhogweed.so.6 => /lib/x86_64-linux-gnu/libhogweed.so.6 (0x00007a706a045000)
        libnettle.so.8 => /lib/x86_64-linux-gnu/libnettle.so.8 (0x00007a7068fab000)
        libgmp.so.10 => /lib/x86_64-linux-gnu/libgmp.so.10 (0x00007a7068f27000)
        libkrb5.so.3 => /lib/x86_64-linux-gnu/libkrb5.so.3 (0x00007a7060937000)
        libk5crypto.so.3 => /lib/x86_64-linux-gnu/libk5crypto.so.3 (0x00007a7068efb000)
        libcom_err.so.2 => /lib/x86_64-linux-gnu/libcom_err.so.2 (0x00007a706a03f000)
        libkrb5support.so.0 => /lib/x86_64-linux-gnu/libkrb5support.so.0 (0x00007a7069d39000)
        libsasl2.so.2 => /lib/x86_64-linux-gnu/libsasl2.so.2 (0x00007a7060de6000)
        libbrotlicommon.so.1 => /lib/x86_64-linux-gnu/libbrotlicommon.so.1 (0x00007a7060dc3000)
        libp11-kit.so.0 => /lib/x86_64-linux-gnu/libp11-kit.so.0 (0x00007a7060062000)
        libtasn1.so.6 => /lib/x86_64-linux-gnu/libtasn1.so.6 (0x00007a7069d23000)
        libkeyutils.so.1 => /lib/x86_64-linux-gnu/libkeyutils.so.1 (0x00007a7068ef4000)
        libresolv.so.2 => /lib/x86_64-linux-gnu/libresolv.so.2 (0x00007a7060db0000)
        libffi.so.8 => /lib/x86_64-linux-gnu/libffi.so.8 (0x00007a7065447000)
miroi@MIRO:~/work/software/gromacs/gromacs_cloned/build_gnu/.

miroi@MIRO:~/work/software/gromacs/gromacs_cloned/build_gnu/bin/.ldd gmx_mpi
        linux-vdso.so.1 (0x00007ffe93506000)
        libgromacs_mpi.so.11 => /home/miroi/work/software/gromacs/gromacs_cloned/build_gnu/bin/./../lib/libgromacs_mpi.so.11 (0x000078fb87c00000)
        libmpi.so.40 => /lib/x86_64-linux-gnu/libmpi.so.40 (0x000078fb87ace000)
        libstdc++.so.6 => /lib/x86_64-linux-gnu/libstdc++.so.6 (0x000078fb87800000)
        libgcc_s.so.1 => /lib/x86_64-linux-gnu/libgcc_s.so.1 (0x000078fb8951d000)
        libc.so.6 => /lib/x86_64-linux-gnu/libc.so.6 (0x000078fb87400000)
        libmpi_cxx.so.40 => /lib/x86_64-linux-gnu/libmpi_cxx.so.40 (0x000078fb89502000)
        libfftw3f.so.3 => /lib/x86_64-linux-gnu/libfftw3f.so.3 (0x000078fb87000000)
        libmkl_intel_lp64.so => /lib/x86_64-linux-gnu/libmkl_intel_lp64.so (0x000078fb86200000)
        libmkl_intel_thread.so => /lib/x86_64-linux-gnu/libmkl_intel_thread.so (0x000078fb82800000)
        libmkl_core.so => /lib/x86_64-linux-gnu/libmkl_core.so (0x000078fb7e000000)
        libomp.so.5 => /lib/x86_64-linux-gnu/libomp.so.5 (0x000078fb876d3000)
        libm.so.6 => /lib/x86_64-linux-gnu/libm.so.6 (0x000078fb87317000)
        libhdf5_serial.so.103 => /lib/x86_64-linux-gnu/libhdf5_serial.so.103 (0x000078fb7dc00000)
        libmuparser.so.2 => /home/miroi/work/software/gromacs/gromacs_cloned/build_gnu/bin/./../lib/../lib/libmuparser.so.2 (0x000078fb87674000)
        /lib64/ld-linux-x86-64.so.2 (0x000078fb8957d000)
        libopen-rte.so.40 => /lib/x86_64-linux-gnu/libopen-rte.so.40 (0x000078fb8725b000)
        libopen-pal.so.40 => /lib/x86_64-linux-gnu/libopen-pal.so.40 (0x000078fb86f4c000)
        libhwloc.so.15 => /lib/x86_64-linux-gnu/libhwloc.so.15 (0x000078fb87613000)
        libdl.so.2 => /lib/x86_64-linux-gnu/libdl.so.2 (0x000078fb87ac7000)
        libpthread.so.0 => /lib/x86_64-linux-gnu/libpthread.so.0 (0x000078fb87ac2000)
        libcrypto.so.3 => /lib/x86_64-linux-gnu/libcrypto.so.3 (0x000078fb7d600000)
        libcurl.so.4 => /lib/x86_64-linux-gnu/libcurl.so.4 (0x000078fb8613f000)
        libsz.so.2 => /lib/x86_64-linux-gnu/libsz.so.2 (0x000078fb87abb000)
        libz.so.1 => /lib/x86_64-linux-gnu/libz.so.1 (0x000078fb87a9f000)
        libgomp.so.1 => /lib/x86_64-linux-gnu/libgomp.so.1 (0x000078fb827aa000)
        libevent_core-2.1.so.7 => /lib/x86_64-linux-gnu/libevent_core-2.1.so.7 (0x000078fb8610a000)
        libevent_pthreads-2.1.so.7 => /lib/x86_64-linux-gnu/libevent_pthreads-2.1.so.7 (0x000078fb87a98000)
        libudev.so.1 => /lib/x86_64-linux-gnu/libudev.so.1 (0x000078fb82777000)
        libnghttp2.so.14 => /lib/x86_64-linux-gnu/libnghttp2.so.14 (0x000078fb86f21000)
        libidn2.so.0 => /lib/x86_64-linux-gnu/libidn2.so.0 (0x000078fb87239000)
        librtmp.so.1 => /lib/x86_64-linux-gnu/librtmp.so.1 (0x000078fb860ec000)
        libssh.so.4 => /lib/x86_64-linux-gnu/libssh.so.4 (0x000078fb82706000)
        libpsl.so.5 => /lib/x86_64-linux-gnu/libpsl.so.5 (0x000078fb87a82000)
        libssl.so.3 => /lib/x86_64-linux-gnu/libssl.so.3 (0x000078fb8265c000)
        libgssapi_krb5.so.2 => /lib/x86_64-linux-gnu/libgssapi_krb5.so.2 (0x000078fb7dfac000)
        libldap.so.2 => /lib/x86_64-linux-gnu/libldap.so.2 (0x000078fb7dba2000)
        liblber.so.2 => /lib/x86_64-linux-gnu/liblber.so.2 (0x000078fb8264c000)
        libzstd.so.1 => /lib/x86_64-linux-gnu/libzstd.so.1 (0x000078fb7d546000)
        libbrotlidec.so.1 => /lib/x86_64-linux-gnu/libbrotlidec.so.1 (0x000078fb7df9e000)
        libaec.so.0 => /lib/x86_64-linux-gnu/libaec.so.0 (0x000078fb82643000)
        libcap.so.2 => /lib/x86_64-linux-gnu/libcap.so.2 (0x000078fb7df91000)
        libunistring.so.5 => /lib/x86_64-linux-gnu/libunistring.so.5 (0x000078fb7d399000)
        libgnutls.so.30 => /lib/x86_64-linux-gnu/libgnutls.so.30 (0x000078fb7d19f000)
        libhogweed.so.6 => /lib/x86_64-linux-gnu/libhogweed.so.6 (0x000078fb7db5a000)
        libnettle.so.8 => /lib/x86_64-linux-gnu/libnettle.so.8 (0x000078fb7d14a000)
        libgmp.so.10 => /lib/x86_64-linux-gnu/libgmp.so.10 (0x000078fb7d0c6000)
        libkrb5.so.3 => /lib/x86_64-linux-gnu/libkrb5.so.3 (0x000078fb7cffd000)
        libk5crypto.so.3 => /lib/x86_64-linux-gnu/libk5crypto.so.3 (0x000078fb7db2e000)
        libcom_err.so.2 => /lib/x86_64-linux-gnu/libcom_err.so.2 (0x000078fb7df8b000)
        libkrb5support.so.0 => /lib/x86_64-linux-gnu/libkrb5support.so.0 (0x000078fb7df7e000)
        libsasl2.so.2 => /lib/x86_64-linux-gnu/libsasl2.so.2 (0x000078fb7db14000)
        libbrotlicommon.so.1 => /lib/x86_64-linux-gnu/libbrotlicommon.so.1 (0x000078fb7cfda000)
        libp11-kit.so.0 => /lib/x86_64-linux-gnu/libp11-kit.so.0 (0x000078fb7ce36000)
        libtasn1.so.6 => /lib/x86_64-linux-gnu/libtasn1.so.6 (0x000078fb7ce20000)
        libkeyutils.so.1 => /lib/x86_64-linux-gnu/libkeyutils.so.1 (0x000078fb7df75000)
        libresolv.so.2 => /lib/x86_64-linux-gnu/libresolv.so.2 (0x000078fb7ce0d000)
        libffi.so.8 => /lib/x86_64-linux-gnu/libffi.so.8 (0x000078fb7ce01000)

Tests
------
make -j4 tests

miroi@MIRO:~/work/software/gromacs/gromacs_cloned/build_gnu/.ls bin/
analysisdata-test*                    gmxana-test*                          mdrun-multisim-replex-equivalence-test*  nblib-integration-test*      qmmm_applied_forces-test*
applied_forces-test*                  gmxapi-mpi-test*                      mdrun-multisim-replex-test*              nblib-integrator-test*       random-test*
argon-forces-integration*             gmxapi-test*                          mdrun-multisim-test*                     nblib-listed-forces-test*    restraintpotential-test*
awh-test*                             gmxpreprocess-test*                   mdrun-non-integrator-test*               nblib-setup-test*            selection-test*
colvars_applied_forces-test*          gpu_utils-mpi-test*                   mdrun-output-test*                       nblib-tpr-test*              serialization-test*
commandline-test*                     gpu_utils-test*                       mdrun-pull-test*                         nblib-util-test*             simd-test*
compat-test*                          h5md-test*                            mdrun-rotation-test*                     nbnxm-gpu-test*              table-test*
coordinateio-test*                    hardware-test*                        mdrun-simulator-comparison-test*         nbnxm-test*                  taskassignment-test*
correlations-test*                    listed_forces-test*                   mdrun-single-rank-algorithms-test*       nnpot_applied_forces-test*   testutils-mpi-test*
density_fitting_applied_forces-test*  math-test*                            mdrun-test*                              nonbonded-fep-test*          testutils-test*
domdec-mpi-test*                      mdlib-test*                           mdrun-tpi-test*                          onlinehelp-test*             timing-test*
domdec-test*                          mdrun-coordination-basic-test*        mdrun-vsites-test*                       options-test*                tool-test*
energyanalysis-test*                  mdrun-coordination-constraints-test*  mdrunutility-mpi-test*                   pbcutil-test*                tool-test-with-leaks*
ewald-test*                           mdrun-coordination-coupling-test*     mdrunutility-test*                       pdb2gmx1-test*               topology-test*
fft-test*                             mdrun-fep-test*                       mdspan-test*                             pdb2gmx2-test*               trajectoryanalysis-test*
fileio-test*                          mdrun-io-test*                        mdtypes-test*                            pdb2gmx3-test*               utility-mpi-test*
fmm-interface-tests*                  mdrun-modules-test*                   methane-water-integration*               plumed_applied_forces-test*  utility-test*
gmx*                                  mdrun-mpi-pme-test*                   minimize-test*                           plumed_md-test*              workflow-details-mpi-test*
gmx_mpi*                              mdrun-mpi-test*                       mpicomm-test*        

ctest  -j4 
.
.
 99/100 Test  #88: MdrunMpi2RankPmeTests .....................   Passed    1.45 sec
        Start  89: MdrunMpi4RankPmeTests
100/100 Test  #89: MdrunMpi4RankPmeTests .....................   Passed    1.36 sec

100% tests passed, 0 tests failed out of 100

Label Time Summary:
GTest              = 212.74 sec*proc (98 tests)
IntegrationTest    = 110.32 sec*proc (32 tests)
MpiTest            = 128.79 sec*proc (26 tests)
QuickGpuTest       =  38.07 sec*proc (24 tests)
SlowGpuTest        = 120.08 sec*proc (15 tests)
SlowTest           =  70.22 sec*proc (14 tests)
UnitTest           =  32.21 sec*proc (52 tests)

Total Test time (real) =  59.50 sec
miroi@MIRO:~/work/software/gromacs/gromacs_cloned/build_gnu/.



