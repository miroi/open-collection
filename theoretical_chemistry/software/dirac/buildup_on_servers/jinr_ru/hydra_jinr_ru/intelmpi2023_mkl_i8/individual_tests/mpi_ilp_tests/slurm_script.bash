#!/bin/bash

#SBATCH --account=bltp
#SBATCH --partition=bltp
#SBATCH --constraint=cascade
#SBATCH --qos=short
#SBATCH --time=00:01:00

date
hostname

module add  intel/v2023.1.0
module list

which mpiicc; mpiicc --version
mpiicc -ilp64  mpi_test.c -o mpi_test.x
./mpi_text.x

which mpiifort; mpiifort --version
mpiifort -i8 check_ilp64.f90 -o check_ilp64.x
./check_ilp64.x




