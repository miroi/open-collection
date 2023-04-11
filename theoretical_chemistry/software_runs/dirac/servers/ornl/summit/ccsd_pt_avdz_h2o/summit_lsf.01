#!/bin/bash

#BSUB -nnodes 8
#BSUB -W 2:00
#BSUB -P CHP109
#BSUB -J ccsd_pt_mp2noo-dz
#BSUB -eo logfile_%J.std_oe
#BSUB -oo logfile_%J.std_oe

# set the appropriate project for INCITE (chp109)
#
export ProjectNumber="chp109"

# set number of mpi processes (2*nnodes)
export nmpi=16

######
# setup of dirac version, modules used in compilation etc
# please do no modify those without checking with the development team
#
source /gpfs/alpine/proj-shared/chp109/dirac/build-setup/modules

export DIRAC_PATH=/gpfs/alpine/proj-shared/chp109/dirac/dirac-public/build_gcc11_cuda_essl_lapack_release-23
export PYTHONPATH=$PYTHONPATH:${DIRAC_PATH}
export BASDIR=${DIRAC_PATH}/basis:${DIRAC_PATH}/basis_dalton:${DIRAC_PATH}/basis_ecp

######
# setup of the job: inputs etc
#
# in this script, we use the input and xyz file names to define the scratch directory name 
#

export MOL_NAME=h2o
export INP_NAME=ccsd_pt_x2c_energy_avdz_-6toAll

export MOL_FILE=${MOL_NAME}.xyz
export INP_FILE=${INP_NAME}.inp

export FILE_NAME=${INP_NAME}"_"${MOL_NAME}

######
# run exacorr
# if you need to keep the same scratch directory, add the flag  --keep_scratch  to the pam invocation line below
#
export DIRAC_SCRATCHDIR=${MEMBERWORK}/${ProjectNumber}/${FILE_NAME}
echo -e "DIRAC_SCRATCHDIR=$DIRAC_SCRATCHDIR"
${DIRAC_PATH}/pam --scratchfull=${DIRAC_SCRATCHDIR} --mpi=$nmpi --mol=$MOL_FILE --inp=$INP_FILE --outqforce

# moving results to 
export CCSD_PT_OUTDIR=ccsd_pt_8nodes_x2c_avdz_canonical

mkdir -p            ${CCSD_PT_OUTDIR}
mv qfdir            ${CCSD_PT_OUTDIR}
mv ${FILE_NAME}.out ${CCSD_PT_OUTDIR}

#If you observe a crash or hang, collect the following files
#and place them in a new directory inside /gpfs/alpine/proj-shared/chp109/issues: 
#----------------------------
# (1) This PBS submit script;
# (2) dirac input and mol/xyz files
# (3) checkpoint file  (if exists);
# (4) Dirac output/error logs;
# (5) qforce.*.log files.
#-----------------------------
