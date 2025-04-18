=========================
QE-devel on Virgo cluster
=========================

/lustre/ukt/milias/work/software/quantum-espresso/q-e_develop


spack modules
~~~~~~~~~~~~~
spack unload --all; spack load openmpi%gcc target=x86_64; spack load amdfftw%gcc target=x86_64; spack load elpa%gcc target=x86_64; spack load amdscalapack%gcc target=x86_64; spack load openblas%gcc target=x86_64

spack find --loaded
-- linux-debian10-x86_64 / gcc@10.2.0 ---------------------------
amdfftw@3.0                         curl@7.85.0       hwloc@2.8.0           libiconv@1.16      mpfr@4.1.0       pcre2@10.39           rdma-core@22.4          xz@5.2.7
amdscalapack@3.2                    diffutils@3.8     json-c@0.16           libmd@1.0.4        munge@0.5.13     perl@5.16.3           readline@8.1.2          zlib@1.2.13
autoconf@2.69                       elpa@2021.11.001  krb5@1.19.3           libpciaccess@0.16  ncurses@6.1      pigz@2.7              slurm@21-08-8-2         zstd@1.5.2
autoconf-archive@2022.02.11         expat@2.4.8       libbsd@0.11.5         libsigsegv@2.13    ninja@1.11.1     pkgconf@1.8.0         sqlite@3.39.4
automake@1.16.5                     gawk@5.1.1        libedit@3.1-20210216  libtool@2.4.7      numactl@2.0.14   pmix@3.2.2            tar@1.34
bison@3.8.2                         gdbm@1.23         libevent@2.1.12       libxml2@2.10.1     openblas@0.3.21  py-pip@22.2.2         texinfo@6.5
bzip2@1.0.8                         gettext@0.21.1    libffi@3.4.2          lz4@1.9.4          openmpi@4.1.5    py-setuptools@59.4.0  ucx@1.9.0
ca-certificates-mozilla@2022-10-11  glib@2.74.1       libgcrypt@1.10.1      m4@1.4.19          openssh@9.1p1    py-wheel@0.37.1       util-linux-uuid@2.38.1
cmake@3.24.3                        gmp@6.2.1         libgpg-error@1.46     meson@0.63.3       openssl@1.1.1s   python@3.10.8         util-macros@1.19.3
==> 66 loaded packages

buildup with CMake
~~~~~~~~~~~~~~~~~~
see https://gitlab.com/QEF/q-e/-/wikis/Developers/CMake-build-system

mkdir build_gnu_openmpi_openblas
cd build_gnu_openmpi_openblas

milias@lxbk1134.gsi.de:/lustre/ukt/milias/work/software/quantum-espresso/q-e_develop/build_gnu_openmpi_openblas/.cmake -DQE_ENABLE_OPENMP=ON -DQE_ENABLE_SCALAPACK=ON -DQE_ENABLE_ELPA=ON -DBLA_VENDOR=OpenBLAS -DCMAKE_C_COMPILER=mpicc -DCMAKE_Fortran_COMPILER=mpif90 -DELPA_LIBRARIES=/cvmfs/vae.gsi.de/vae23/spack-0.19/opt/linux-debian10-x86_64/gcc-10.2.0/elpa-2021.11.001-uorwjue22nh7br4jthmt3lfugpeivfms/lib/libelpa_openmp.a  -DELPA_INCLUDE_DIRS=/cvmfs/vae.gsi.de/vae23/spack-0.19/opt/linux-debian10-x86_64/gcc-10.2.0/elpa-2021.11.001-uorwjue22nh7br4jthmt3lfugpeivfms/include -DELPA_Fortran_MODS_DIR=/cvmfs/vae.gsi.de/vae23/spack-0.19/opt/linux-debian10-x86_64/gcc-10.2.0/elpa-2021.11.001-uorwjue22nh7br4jthmt3lfugpeivfms/include/elpa_openmp-2021.11.001/modules -DVendorFFTW_LIBRARIES=/cvmfs/vae.gsi.de/vae23/spack-0.19/opt/linux-debian10-x86_64/gcc-10.2.0/amdfftw-3.0-a5urjhpjd7jrmbg6ygxyvci2d4kv2fbb/lib -DVendorFFTW_INCLUDE_DIRS=/cvmfs/vae.gsi.de/vae23/spack-0.19/opt/linux-debian10-x86_64/gcc-10.2.0/amdfftw-3.0-a5urjhpjd7jrmbg6ygxyvci2d4kv2fbb/include  ..
-- Enable sanitizer QE_ENABLE_SANITIZER=none
-- C preprocessor used by qe_preprocess_source in qeHelpers.cmake: /usr/bin/cpp
-- MPI settings used by CTest
     MPIEXEC_EXECUTABLE : /cvmfs/vae.gsi.de/vae23/spack-0.19/opt/linux-debian10-x86_64/gcc-10.2.0/openmpi-4.1.5-phbdvrf3few3givo575jlifx6dhnfgk7/bin/mpiexec
     MPIEXEC_NUMPROC_FLAG : -n
     MPIEXEC_PREFLAGS : 
   Tests run as : /cvmfs/vae.gsi.de/vae23/spack-0.19/opt/linux-debian10-x86_64/gcc-10.2.0/openmpi-4.1.5-phbdvrf3few3givo575jlifx6dhnfgk7/bin/mpiexec -n <NUM_PROCS>  <EXECUTABLE>
-- Source files are cloned from a git repository.
   sed supports -E
   Git branch: develop
   Git commit hash: 9ff5b55a523ad07f84bff1ef19d05149d27d5473
-- Found LAPACK: /cvmfs/vae.gsi.de/vae23/spack-0.19/opt/linux-debian10-x86_64/gcc-10.2.0/openblas-0.3.21-q7nhojttkz52xuf4zkxk7vvgllqnxh34/lib/libopenblas.so;/cvmfs/vae.gsi.de/vae23/spack-0.19/opt/linux-debian10-x86_64/gcc-10.2.0/openblas-0.3.21-q7nhojttkz52xuf4zkxk7vvgllqnxh34/lib/libopenblas.so;/cvmfs/vae.gsi.de/vae23/spack-0.19/opt/linux-debian10-x86_64/gcc-10.2.0/openblas-0.3.21-q7nhojttkz52xuf4zkxk7vvgllqnxh34/lib/libopenblas.so;/cvmfs/vae.gsi.de/vae23/spack-0.19/opt/linux-debian10-x86_64/gcc-8.3.0/gcc-10.2.0-agxjp3zexhitnb3g6czo5p4im3hi74ht/lib64/libgomp.so
-- Looking for Fortran pdgemm
-- Looking for Fortran pdgemm - found
-- Found SCALAPACK: /cvmfs/vae.gsi.de/vae23/spack-0.19/opt/linux-debian10-x86_64/gcc-10.2.0/amdscalapack-3.2-zmrsnzmnifwusgdparcdnpdksnehsbcm/lib/libscalapack.so;/cvmfs/vae.gsi.de/vae23/spack-0.19/opt/linux-debian10-x86_64/gcc-10.2.0/openblas-0.3.21-q7nhojttkz52xuf4zkxk7vvgllqnxh34/lib/libopenblas.so;/cvmfs/vae.gsi.de/vae23/spack-0.19/opt/linux-debian10-x86_64/gcc-10.2.0/openblas-0.3.21-q7nhojttkz52xuf4zkxk7vvgllqnxh34/lib/libopenblas.so;/cvmfs/vae.gsi.de/vae23/spack-0.19/opt/linux-debian10-x86_64/gcc-10.2.0/openblas-0.3.21-q7nhojttkz52xuf4zkxk7vvgllqnxh34/lib/libopenblas.so;
-- ELPA version string extracted from ELPA_INCLUDE_DIRS : 2021.11.001
-- Found ELPA: /cvmfs/vae.gsi.de/vae23/spack-0.19/opt/linux-debian10-x86_64/gcc-10.2.0/elpa-2021.11.001-uorwjue22nh7br4jthmt3lfugpeivfms/lib/libelpa_openmp.a (found version "2021.11.001") 
-- Add ELPA flag : __ELPA
-- Installing Wannier90 via submodule
-- Installing MBD via submodule
-- Installing DeviceXlib via submodule
-- Found VendorFFTW: /cvmfs/vae.gsi.de/vae23/spack-0.19/opt/linux-debian10-x86_64/gcc-10.2.0/amdfftw-3.0-a5urjhpjd7jrmbg6ygxyvci2d4kv2fbb/lib  
-- Enabling tests in test-suite

Only pw and cp results from ctest are reliable, we are working on making the rest tests work reliably with ctest. To run non-pw/cp tests, make a softlink of the bin directory to the root of QE source tree and run tests in the test-suite directory under that root.

-- generating tests in pw category
-- generating tests in cp category
-- generating tests in ph category
-- generating tests in epw category
-- generating tests in tddfpt category
-- generating tests in hp category
-- Configuring done
-- Generating done
-- Build files have been written to: /lustre/ukt/milias/work/software/quantum-espresso/q-e_develop/build_gnu_openmpi_openblas
milias@lxbk1134.gsi.de:/lustre/ukt/milias/work/software/quantum-espresso/q-e_develop/build_gnu_openmpi_openblas/.
.
.
milias@lxbk1134.gsi.de:/lustre/ukt/milias/work/software/quantum-espresso/q-e_develop/build_gnu_openmpi_openblas/.ls bin/
abcoeff_to_eps.x*  dynmat.x*          fs.x*             manycp.x*              pmw.x*           pwcond.x*              turbo_spectrum.x*
all_currents.x*    ef.x*              graph.x*          matdyn.x*              postahc.x*       pwi2xsf.x*             upfconv.x*
alpha2f.x*         epa.x*             gww_fit.x*        memory_pw4gww.x*       postw90.x*       pw.x*                  ups.x*
average.x*         epsilon_Gaus.x*    gww.x*            molecularnexafs.x*     ppacf.x*         q2qstar.x*             virtual_v2.x*
bands_unfold.x*    epsilon.x*         head.x*           molecularpdos.x*       pp_disca.x*      q2r.x*                 w90chk2chk.x*
bands.x*           epw.x*             hgh2qe.x*         neb.x*                 pprism.x*        scan_ibrav.x*          wannier90.x*
bse_main.x*        ev.x*              hp.x*             open_grid.x*           pp_spctrlfn.x*   simple_bse.x*          wannier_ham.x*
casino2upf.x*      fd_ef.x*           ibrav2cell.x*     path_interpolation.x*  pp.x*            simple_ip.x*           wannier_plot.x*
cell2ibrav.x*      fd_ifc.x*          initial_state.x*  pawplot.x*             projwfc.x*       simple.x*              wfck2r.x*
cppp.x*            fd.x*              kcwpp_interp.x*   phcg.x*                pw2bgw.x*        spectra_correction.x*  wfdd.x*
cp.x*              fermi_int_0.x*     kcwpp_sh.x*       ph.x*                  pw2critic.x*     sumpdos.x*             xspectra.x*
disca.x*           fermi_int_1.x*     kcw.x*            plan_avg.x*            pw2gt.x*         turbo_davidson.x*      ZG.x*
dos_sp.x*          fermi_proj.x*      kpoints.x*        plotband.x*            pw2gw.x*         turbo_eels.x*
dos.x*             fermi_velocity.x*  lambda.x*         plotproj.x*            pw2wannier90.x*  turbo_lanczos.x*
dvscf_q2r.x*       fqha.x*            ld1.x*            plotrho.x*             pw4gww.x*        turbo_magnon.x*



