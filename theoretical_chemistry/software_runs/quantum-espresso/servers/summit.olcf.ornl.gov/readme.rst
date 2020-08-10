GPU-QE on Summit
================

https://gitlab.com/QEF/q-e-gpu/-/wikis/Install-QE-GPU-on-Summit


Lodad modules
-------------
module unload xl
module load pgi
module load essl
module load cuda
module load hdf5 
module load netlib-lapack
module load python

Check enviro-variables
-----------------------

echo $OLCF_ESSL_ROOT   /sw/summit/essl/6.1.0-2/essl/6.1
ls $OLCF_ESSL_ROOT/lib64  

echo $OLCF_NETLIB_LAPACK_ROOT
ls $OLCF_NETLIB_LAPACK_ROOT/lib64/liblapack.a

echo $OLCF_HDF5_ROOT

Clone and configure
~~~~~~~~~~~~~~~~~~~

git clone https://gitlab.com/QEF/q-e-gpu.git
cd q-e-gpu

export BLAS_LIBS="-L$OLCF_ESSL_ROOT/lib64 -lessl"
export LAPACK_LIBS="-L$OLCF_ESSL_ROOT/lib64 -lessl $OLCF_NETLIB_LAPACK_ROOT/lib64/liblapack.a"

./configure --enable-openmp --with-hdf5=$OLCF_HDF5_ROOT --with-cuda=$OLCF_CUDA_ROOT --with-cuda-runtime=10.1 --with-cuda-cc=70 --prefix=$PWD

sed -i "/DFLAGS/s/__FFTW/__LINUX_ESSL/" make.inc

make -j32 all install
#make -j32 pw

