Extrae on DIRAC
===============

lxir127.gsi.de
--------------

libunwind
~~~~~~~~~
see https://savannah.nongnu.org/projects/libunwind

wget https://download.savannah.nongnu.org/releases/libunwind/libunwind-1.5.0.tar.gz
milias@lxir127.gsi.de:/data.local1/milias/software/dirac/extrae/libunwind-1.5.0/.FC=ifort CC=icc CXX=icpc ./configure --prefix=/data.local1/milias/software/dirac/extrae/libunwind_install
milias@lxir127.gsi.de:/data.local1/milias/software/dirac/extrae/libunwind-1.5.0/make -j12 
milias@lxir127.gsi.de:/data.local1/milias/software/dirac/extrae/libunwind-1.5.0/make all install



extrae
~~~~~~
see https://tools.bsc.es/downloads
wget https://ftp.tools.bsc.es/extrae/extrae-3.8.3-src.tar.bz2

milias@lxir127.gsi.de:/data.local1/milias/software/dirac/extrae/extrae-3.8.3/.FC=ifort CC=icc CXX=icpc  ./configure --prefix=/data.local1/milias/software/dirac/extrae/extrae-3.8.3_install  --with-mpi=/cvmfs/it.gsi.de/openmpi/intel/4.0.1_intel17.4  --without-unwind --without-dyninst --without-papi

configure: error: You can gather call-site information which must be translated using binutils, but either libbfd or libiberty are not found. Please make sure that the binutils-dev package is installed and specify where to find these libraries through --with-binutils. The latest source can be downloaded from http://www.gnu.org/software/binutils

Missing packages ...


