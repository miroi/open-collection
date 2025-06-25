QE with DFTD4
=============


buildup
~~~~~~~~
q-e_miro_fork/build_gnu/.cmake -DQE_ENABLE_MPI=ON -DQE_ENABLE_MPI_MODULE=ON  -DCMAKE_C_COMPILER=gcc -DCMAKE_CXX_COMPILER=g++ -DCMAKE_Fortran_COMPILER=mpif90  -DQE_FFTW_VENDOR=Internal  -D QE_DFTD4=ON   ..


runs
~~~~
 wsl2_victus_nb.01
 wsl2_Dekstop.01
