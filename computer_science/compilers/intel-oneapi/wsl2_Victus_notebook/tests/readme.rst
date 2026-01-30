========================================
testing source files for Intel compilers
========================================


source  /opt/intel/oneapi/2025.3/oneapi-vars.sh

miroi@MIRO:~/work/projects/open-collection/computer_science/compilers/intel-oneapi/tests/.which mpirun
/opt/intel/oneapi/2025.3/bin/mpirun

miroi@MIRO:~/work/projects/open-collection/computer_science/compilers/intel-oneapi/tests/.mpiifx --version
ifx (IFX) 2025.3.2 20260112

miroi@MIRO:~/work/projects/open-collection/computer_science/compilers/intel-oneapi/tests/.mpiicx --version
Intel(R) oneAPI DPC++/C++ Compiler 2025.3.2 (2025.3.2.20260112)

miroi@MIRO:~/work/projects/open-collection/computer_science/compilers/intel-oneapi/tests/.mpiicpx --version
Intel(R) oneAPI DPC++/C++ Compiler 2025.3.2 (2025.3.2.20260112)

https://www.intel.com/content/www/us/en/docs/fortran-compiler/get-started-guide/2025-1/get-started-on-linux.html

miroi@MIRO:~/work/projects/open-collection/computer_science/compilers/intel-oneapi/tests/.ifx hello.f90
miroi@MIRO:~/work/projects/open-collection/computer_science/compilers/intel-oneapi/tests/.a.out
 Hello, world!


https://github.com/oneapi-src/oneAPI-samples/tree/9c7d508f7d9817ec948d132d919e89441703693a/DirectProgramming/Fortran

miroi@MIRO:~/work/projects/open-collection/computer_science/compilers/intel-oneapi/tests/.ifx int_sin.f90
