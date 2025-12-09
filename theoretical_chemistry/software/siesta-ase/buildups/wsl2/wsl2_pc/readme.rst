==============
SIESTA buildup
==============

download
---------
milias@DESKTOP-7OTLCGO:~/work/software/siesta/packaged/siesta-5.4.1/.wget https://gitlab.com/siesta-project/siesta/-/releases/5.4.1/downloads/siesta-5.4.1.tar.gz
milias@DESKTOP-7OTLCGO:~/work/software/siesta/packaged/siesta-5.4.1/.tar xvzf siesta-5.4.1.tar.gz

flook
~~~~~~
wget https://github.com/ElectronicStructureLibrary/flook/archive/refs/tags/v0.8.4.tar.gz
/siesta-5.4.1/External/flook_package/flook-0.8.4

sudo apt-get install libreadline-deva
milias@DESKTOP-7OTLCGO:~/work/software/siesta/packaged/siesta-5.4.1/External/flook_package/flook-0.8.4/.make
milias@DESKTOP-7OTLCGO:~/work/software/siesta/packaged/siesta-5.4.1/External/flook_package/flook-0.8.4/.quick_test.sh  > quick_test.logfile

make install
milias@DESKTOP-7OTLCGO:~/work/software/siesta/packaged/siesta-5.4.1/External/flook_package/flook_installed/.mv ~/flook .
milias@DESKTOP-7OTLCGO:~/work/software/siesta/packaged/siesta-5.4.1/External/flook_package/flook_installed/.mv flook flook_installed


elpa
~~~~
sudo apt install libelpa-dev

installation
-------------
https://docs.siesta-project.org/projects/siesta/en/stable/installation/build-manually.html

milias@DESKTOP-7OTLCGO:~/work/software/siesta/packaged/siesta-5.4.1/.cmake -S. -B_build -DCMAKE_INSTALL_PREFIX=/home/milias/work/software/siesta/packaged  -DSIESTA_WITH_MPI=ON -DSIESTA_WITH_ELPA=OFF  -DSCALAPACK_LIBRARY="/usr/lib/x86_64-linux-gnu/libmkl_scalapack_lp64.so;/usr/lib/x86_64-linux-gnu/libmkl_blacs_openmpi_lp64.so"
.
.
-- ++++ Siesta build >>> ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
-- +
-- + ---- SIESTA is ON --------------------------------------------------------------
-- + | Required feature (cannot be disabled)
-- + | The SIESTA build information will be listed here.
-- + | In particular how the targets and the variables affecting binaries are interpreted.
-- + | It can be used to debug how the final linker lines for siesta
-- + | is handled.
-- + | Variables used to enable feature:
-- + |  - SIESTA_WITH_UNIT_CONVENTION=CODATA2018
-- + |  - SIESTA_WITH_MPI=ON
-- + |  - SIESTA_WITH_OPENMP=OFF
-- + |  - SIESTA_WITH_IPO=OFF
-- + |  - SIESTA_WITH_NETCDF=OFF
-- + |  - SIESTA_WITH_NCDF=FALSE
-- + |  - SIESTA_WITH_LIBXC=OFF
-- + |  - SIESTA_WITH_PEXSI=OFF
-- + |  - SIESTA_WITH_FFTW=ON
-- + |  - SIESTA_WITH_DFTD3=ON
-- + |  - SIESTA_WITH_WANNIER90=OFF
-- + |  - SIESTA_WITH_CHESS=OFF
-- + |  - SIESTA_WITH_ELSI=ON
-- + |  - SIESTA_WITH_ELPA=TRUE
-- + |  - SIESTA_WITH_FLOOK=ON
-- + |  - SIESTA_INSTALL=ON
-- + |  - BUILD_SHARED_LIBS=OFF
-- + |  - SIESTA_SHARED_LIBS=OFF
-- + |  - SIESTA_TESTS=ON
-- + |  - SIESTA_TESTS_MPI_MIN_NUMPROCS=1
-- + |  - SIESTA_TESTS_MPI_NUMPROCS=4
-- + |  - SIESTA_TESTS_MPI_MAX_NUMPROCS=10
-- + |  - SIESTA_TOOLCHAIN=gnu
-- + |  - SIESTA_BUILD_DOCS=OFF
-- + | Empty or undefined variables (only useful for developers!):
-- + |  - SIESTA_WITH_NETCDF_PARALLEL
-- + |  - SIESTA_LINKER_FLAGS_PRE
-- + |  - SIESTA_LINKER_FLAGS_POST
-- + |  - SIESTA_LINKER_FLAGS
-- + |  - SIESTA_WITH_NO_MPI_INTERFACES
-- + |  - SIESTA_SUFFIX
-- + |  - SIESTA_EXECUTABLE_SUFFIX
-- + |  - SIESTA_SHARED_LIBRARY_SUFFIX
-- + |  - SIESTA_STATIC_LIBRARY_SUFFIX
-- + |  - SIESTA_INTEGER_KINDS
-- + |  - SIESTA_REAL_KINDS
-- + |  - SIESTA_WITH_PROFILE_NVTX
-- + |  - SIESTA_PROFILE_NVTX_LIBRARY
-- + --------------------------------------------------------------------------------
-- +
-- ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ <<< Siesta build ++++
-- Configuring done
-- Generating done
-- Build files have been written to: /home/milias/work/software/siesta/packaged/siesta-5.4.1/_build

Compilation
~~~~~~~~~~~
milias@DESKTOP-7OTLCGO:~/work/software/siesta/packaged/siesta-5.4.1/_build/.m 
.
.
.
[ 33%] Building Fortran object _deps/elsi-build/test/CMakeFiles/elsi_test.dir/Fortran/test_occ_normal.f90.o
[ 33%] Building Fortran object _deps/elsi-build/test/CMakeFiles/elsi_test.dir/Fortran/test_occ_non_aufbau.f90.o
[ 33%] Linking Fortran executable ../bin/elsi_test
/usr/bin/ld: ../lib/libpexsi.a(interface.cpp.o): in function `MPI::Op::Init(void (*)(void const*, void*, int, MPI::Datatype const&), bool)':
interface.cpp:(.text._ZN3MPI2Op4InitEPFvPKvPviRKNS_8DatatypeEEb[_ZN3MPI2Op4InitEPFvPKvPviRKNS_8DatatypeEEb]+0x1d): undefined reference to `ompi_mpi_cxx_op_intercept'
/usr/bin/ld: ../lib/libpexsi.a(interface.cpp.o): in function `MPI::Intracomm::Clone() const':
interface.cpp:(.text._ZNK3MPI9Intracomm5CloneEv[_ZNK3MPI9Intracomm5CloneEv]+0x40): undefined reference to `MPI::Comm::Comm()'
/usr/bin/ld: ../lib/libpexsi.a(interface.cpp.o): in function `MPI::Graphcomm::Clone() const':
interface.cpp:(.text._ZNK3MPI9Graphcomm5CloneEv[_ZNK3MPI9Graphcomm5CloneEv]+0x3a): undefined reference to `MPI::Comm::Comm()'
/usr/bin/ld: ../lib/libpexsi.a(interface.cpp.o): in function `MPI::Cartcomm::Sub(bool const*) const':
interface.cpp:(.text._ZNK3MPI8Cartcomm3SubEPKb[_ZNK3MPI8Cartcomm3SubEPKb]+0x96): undefined reference to `MPI::Comm::Comm()'
/usr/bin/ld: ../lib/libpexsi.a(interface.cpp.o): in function `MPI::Intracomm::Create_graph(int, int const*, int const*, bool) const':
interface.cpp:(.text._ZNK3MPI9Intracomm12Create_graphEiPKiS2_b[_ZNK3MPI9Intracomm12Create_graphEiPKiS2_b]+0x42): undefined reference to `MPI::Comm::Comm()'
/usr/bin/ld: ../lib/libpexsi.a(interface.cpp.o): in function `MPI::Cartcomm::Clone() const':

Tests
~~~~~

