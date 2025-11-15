==============
SIESTA buildup
==============

[  4%] Building Fortran object libgridxc/CMakeFiles/libgridxc-lib.dir/src/ldaxc.F90.o
f951: Fatal Error: Reading module ‘/lustre/home/user/m/milias/work/software/libxc/include/xc_f03_lib_m.mod’ at line 1 column 2: Unexpected EOF

try SIESTA_WITH_LIBXC=OFF !

now, after make, run ctest and at the end make install
