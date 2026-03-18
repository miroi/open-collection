============================
DIRAC with IntelMPI+MKL+int8
============================

./setup --mpi --exatensor=OFF --pcmsolver=OFF  --pelib=OFF  --fc=mpiifx   --extra-fc-flags="-O3 -xHost -ilp64" --cc=mpiicx --extra-cc-flags="-O"  --cxx=mpiicpx --int64 $BUILD

milias@hydra.jinr.ru:/lustre/projects/m/milias/work/git-projects/open-collection/theoretical_chemistry/software/dirac/buildup_on_servers/jinr_ru/hydra_jinr_ru/intelmpi2025_mkl_i8/.sbatch hydra_slurm_dirac_buildup_ctest.01

reported errors: https://gitlab.com/dirac/dirac/-/work_items/178
