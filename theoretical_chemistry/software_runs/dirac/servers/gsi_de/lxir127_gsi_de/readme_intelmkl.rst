============================
DIRAC buildup with Intel MKL
============================

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



