#!/bin/bash

export  MKL_NUM_THREADS=1
export  MKL_DOMAIN_NUM_THREADS="MKL_BLAS=1"
export  OMP_NUM_THREADS=1
export  MKL_DYNAMIC="FALSE"
export  OMP_DYNAMIC="FALSE"

 export CurrDir=$SLURM_SUBMIT_DIR

if [ -n "$SLURM_NTASKS" ]; then
	export  mympi=$SLURM_NTASKS
else
	export  mympi=1
fi

 # program position
 export SIMION=/lustre/ukt/common/simion

 env | egrep 'SLURM_(NTASKS|NNODES|NPROCS|NODELIST|DIST)'

 export myinp=${1}
 export myout=${2}
 export MY_WORKDIR=/tmp/$USER/$SLURM_JOB_NAME/${SLURM_JOB_ID}

 export myscratch=${MY_WORKDIR}/$myinp
 mkdir -p ${myscratch}

 cd $myscratch

 cp ${SIMION}/simion ${myscratch}/
 cp ${SIMION}/simion.key ${myscratch}/

 # copy required input files
 cp $CurrDir/*.lua  ${myscratch}/
 cp $CurrDir/*.pa*  ${myscratch}/
 cp $CurrDir/*.iob  ${myscratch}/
 cp $CurrDir/*.gem  ${myscratch}/
 cp $CurrDir/*.rec  ${myscratch}/
 cp $CurrDir/*.fly2 ${myscratch}/

 cp ${CurrDir}/${myinp} ${myscratch}/

 ls -lrt

 nohup ${myscratch}/simion --nogui --num-threads ${mympi} fly ${myinp} > ${CurrDir}/${myout}

 cd $CurrDir

exit
