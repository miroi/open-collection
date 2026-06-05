DIRAC interactive buildup
=========================

milias@hydra.jinr.ru:/lustre/projects/m/milias/work/software/dirac/trunk/.module add CMake/v4.2.3
milias@hydra.jinr.ru:/lustre/projects/m/milias/work/software/dirac/trunk/.module add Python/v3.12.13  intel/v2025.3.1
(Py3.12.13) milias@hydra.jinr.ru:/lustre/projects/m/milias/work/software/dirac/trunk/../setup --mpi --exatensor=OFF --pcmsolver=OFF  --pelib=OFF  --fc=mpiifx   --extra-fc-flags="-O3 -xHost -ilp64" --cc=mpiicx --extra-cc-flags="-O"  --cxx=mpiicpx --int64  build_intelmpi2025_mkl_i8_interact

