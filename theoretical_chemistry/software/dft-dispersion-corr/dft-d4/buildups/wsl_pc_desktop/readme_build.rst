======
DFT-D4
======


milias@DESKTOP-7OTLCGO:~/work/software/dft-d4/.git clone git@github.com:dftd4/dftd4.git

mkdir _build

milias@DESKTOP-7OTLCGO:~/work/software/dft-d4/dftd4/_build/.cmake ..
.
.
-- Configuring done
-- Generating done
-- Build files have been written to: /home/milias/work/software/dft-d4/dftd4/_build

milias@DESKTOP-7OTLCGO:~/work/software/dft-d4/dftd4/_build/.make
.
.
[ 96%] Built target dftd4-api-tester
Scanning dependencies of target dftd4-tester
[ 97%] Building Fortran object test/unit/CMakeFiles/dftd4-tester.dir/test_dftd4.f90.o
[ 97%] Building Fortran object test/unit/CMakeFiles/dftd4-tester.dir/test_model.f90.o
[ 98%] Building Fortran object test/unit/CMakeFiles/dftd4-tester.dir/test_pairwise.f90.o
[ 98%] Building Fortran object test/unit/CMakeFiles/dftd4-tester.dir/test_param.f90.o
[ 99%] Building Fortran object test/unit/CMakeFiles/dftd4-tester.dir/test_periodic.f90.o
[100%] Building Fortran object test/unit/CMakeFiles/dftd4-tester.dir/main.f90.o
[100%] Linking Fortran executable dftd4-tester
[100%] Built target dftd4-tester


milias@DESKTOP-7OTLCGO:~/work/software/dft-d4/dftd4/_build/.ldd app/dftd4
        linux-vdso.so.1 (0x00007ffe00bfb000)
        liblapack.so.3 => /lib/x86_64-linux-gnu/liblapack.so.3 (0x0000727742c00000)
        libblas.so.3 => /lib/x86_64-linux-gnu/libblas.so.3 (0x000072774347c000)
        libgomp.so.1 => /lib/x86_64-linux-gnu/libgomp.so.1 (0x0000727743432000)
        libgfortran.so.5 => /lib/x86_64-linux-gnu/libgfortran.so.5 (0x0000727742800000)
        libm.so.6 => /lib/x86_64-linux-gnu/libm.so.6 (0x000072774334b000)
        libc.so.6 => /lib/x86_64-linux-gnu/libc.so.6 (0x0000727742400000)
        libgcc_s.so.1 => /lib/x86_64-linux-gnu/libgcc_s.so.1 (0x0000727742be0000)
        libquadmath.so.0 => /lib/x86_64-linux-gnu/libquadmath.so.0 (0x0000727742b98000)
        /lib64/ld-linux-x86-64.so.2 (0x0000727743630000)



