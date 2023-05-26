============================
DIRAC buildup with Intel MKL
============================

Loading packages
~~~~~~~~~~~~~~~~
milias@lxir127.gsi.de:/data.local1/milias/software/dirac/dirac-public/.spack unload 
milias@lxir127.gsi.de:/data.local1/milias/software/dirac/dirac-public/.spack find loaded
==> No package matches the query: loaded

milias@lxir127.gsi.de:/data.local1/milias/software/dirac/dirac-public/.spack arch -t
broadwell

milias@lxir127.gsi.de:/data.local1/milias/software/dirac/dirac-public/.spack load intel-mkl@2020.4.304

milias@lxir127.gsi.de:/data.local1/milias/software/dirac/dirac-public/.spack find --loaded
==> 1 loaded package
-- linux-debian10-x86_64 / gcc@8.3.0 ----------------------------
intel-mkl@2020.4.304
milias@lxir127.gsi.de:/data.local1/milias/software/dirac/dirac-public/.which ifort
milias@lxir127.gsi.de:/data.local1/milias/software/dirac/dirac-public/.which icc
milias@lxir127.gsi.de:/data.local1/milias/software/dirac/dirac-public/.emkl
Intel MKL library ? MKLROOT=/cvmfs/vae.gsi.de/debian10/spack-0.17/opt/linux-debian10-x86_64/gcc-8.3.0/intel-mkl-2020.4.304-wcz55b7qqq66b7lh5vqt6qt7ftlkwa3z/compilers_and_libraries_2020.4.304/linux/mkl

milias@lxir127.gsi.de:/data.local1/milias/software/dirac/dirac-public/.spack load intel-parallel-studio@professional.2020.1

milias@lxir127.gsi.de:/data.local1/milias/software/dirac/dirac-public/.spack find --loaded
==> 2 loaded packages
-- linux-debian10-x86_64 / gcc@8.3.0 ----------------------------
intel-mkl@2020.4.304  intel-parallel-studio@professional.2020.1

milias@lxir127.gsi.de:/data.local1/milias/software/dirac/dirac-public/.which ifort
/cvmfs/vae.gsi.de/debian10/spack-0.17/opt/linux-debian10-x86_64/gcc-8.3.0/intel-parallel-studio-professional.2020.1-yr5yjb5uiztgkfs4qz6u5dxj5zrz455s/compilers_and_libraries_2020.1.217/linux/bin/intel64/ifort
milias@lxir127.gsi.de:/data.local1/milias/software/dirac/dirac-public/.which icc
/cvmfs/vae.gsi.de/debian10/spack-0.17/opt/linux-debian10-x86_64/gcc-8.3.0/intel-parallel-studio-professional.2020.1-yr5yjb5uiztgkfs4qz6u5dxj5zrz455s/compilers_and_libraries_2020.1.217/linux/bin/intel64/icc

we have serial Intel compilers, with MKL library

Add OpenMPI-i8
~~~~~~~~~~~~~~~~
milias@lxir127.gsi.de:/data.local1/milias/software/dirac/dirac-public/.export PATH=/u/milias/bin/openmpi-i8/bin:$PATH
milias@lxir127.gsi.de:/data.local1/milias/software/dirac/dirac-public/.export LD_LIBRARY_PATH=/u/milias/bin/openmpi-i8/lib:$LD_LIBRARY_PATH

Add CMake:
~~~~~~~~~~~
milias@lxir127.gsi.de:/data.local1/milias/software/dirac/dirac-public/.spack load cmake@3.21.4 target=$(spack arch -t)

Own build:
~~~~~~~~~~
milias@lxir127.gsi.de:/data.local1/milias/software/dirac/dirac-public/../setup --int64 --mkl=parallel --mpi build_intelompi_mklpar_i8
.
.
.
   configure step is done
   now you need to compile the sources:
   $ cd build_intelompi_mklpar_i8
   $ make

milias@lxir127.gsi.de:/data.local1/milias/software/dirac/dirac-public/build_intelompi_mklpar_i8/.make -j12


