GPU-QE on Summit
================

https://gitlab.com/QEF/q-e-gpu/-/wikis/Install-QE-GPU-on-Summit


module add pgi

git clone https://gitlab.com/QEF/q-e-gpu.git
cd q-e-gpu

export BLAS_LIBS="-L$OLCF_ESSL_ROOT/lib64 -lessl"
export LAPACK_LIBS="-L$OLCF_ESSL_ROOT/lib64 -lessl $OLCF_NETLIB_LAPACK_ROOT/lib64/liblapack.a"

./configure --enable-openmp --with-hdf5=$OLCF_HDF5_ROOT \
            --with-cuda=$OLCF_CUDA_ROOT --with-cuda-runtime=10.1 --with-cuda-cc=70

sed -i "/DFLAGS/s/__FFTW/__LINUX_ESSL/" make.inc

make -j32 pw

