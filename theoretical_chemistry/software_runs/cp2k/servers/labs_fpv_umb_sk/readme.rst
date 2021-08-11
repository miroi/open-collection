CP2K test runs
==============

@labs.fpv.umb.sk
----------------
/home/milias/work/qch_software/cp2k/exe/local

@login.grid.umb.sk
------------------
milias@login.grid.umb.sk:~/Work/qch/software/cp2k/cp2k_master/tools/toolchain/../install_cp2k_toolchain.sh -h

# problems with lagrind installation, skip it, with cmake
./install_cp2k_toolchain.sh -j 2 --install-all  --math-mode=mkl --mpi-mode=openmpi  --with-valgrind=no  --with-cmake=no





