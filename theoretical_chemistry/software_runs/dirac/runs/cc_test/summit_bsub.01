#!/bin/bash
##BSUB -nnodes 200
#BSUB -nnodes 2
#BSUB -W 2:00
#BSUB -P CHP109
#BSUB -J cctest
#BSUB -eo %J.std_oe
#BSUB -u M.Ilias@gsi.de  

# Load modules:
module load gcc/8.1.1
module load essl
module load cuda
module load git
module load cmake
module load python
module load netlib-lapack

# number of MPI processes (2*nnodes)
#export nmpi=400
export nmpi=4

# dirac setup
export DIRAC_PATH=/gpfs/alpine/world-shared/chp109/dirac_install
export BASDIR=${DIRAC_PATH}/basis:${DIRAC_PATH}/basis_dalton:${DIRAC_PATH}/basis_ecp

# project setup
export ProjectDir=/ccs/home/milias/work/open-collection/theoretical_chemistry/software_runs/dirac/cc_test

export MOL_file=$ProjectDir/CO.mol
export INP_file=$ProjectDir/ccsd.small.inp

export DIRAC_TMPDIR=${MEMBERWORK}/chp109/cc_test
#

# now running

#cd $outdir
# run exacorr
#${DIRAC_PATH}/pam --keep_scratch --scratchfull=$DIRAC_TMPDIR --mpi=$nmpi --mol=$MOL_file --inp=$INP_file --outqforce --put="$datadir/DFCOEF $datadir/AOMOMAT" --get "CCDENS"
${DIRAC_PATH}/pam --noarch --scratch=$DIRAC_TMPDIR --mpi=$nmpi --mol=$MOL_file --inp=$INP_file 

