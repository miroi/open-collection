#!/bin/bash

#SBATCH --account=bltp
#SBATCH --partition=bltp
#SBATCH --constraint=cascade
#SBATCH --qos=short
#SBATCH --time=00:01:00
#SBATCH -N 1 -n 2
#SBATCH -o log_slurm_job.%j.%N.std_out_err

date
hostname

module add  intel/v2023.1.0
module list

which mpirun; mpirun --version

which mpiicc; mpiicc --version
mpiicc -ilp64  mpi_test.c -o mpi_test.x
mpirun -np  $SLURM_NTASKS ./mpi_test.x

which mpiifort; mpiifort --version
mpiifort -i8 check_ilp64.f90 -o check_ilp64.x
mpirun -np  $SLURM_NTASKS ./check_ilp64.x

mpiifort  check_ilp64.f90 -o check_ilp64_i4.x
mpirun -np  $SLURM_NTASKS ./check_ilp64_i4.x


