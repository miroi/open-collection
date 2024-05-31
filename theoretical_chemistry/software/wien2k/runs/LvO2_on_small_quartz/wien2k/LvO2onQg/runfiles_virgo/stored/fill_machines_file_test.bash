#!/bin/bash

export SLURM_CPUS_ON_NODE=16

echo "SLURM_CPUS_ON_NODE=$SLURM_CPUS_ON_NODE"

echo '#' > machines

counter=1
while [ $counter -le $SLURM_CPUS_ON_NODE ] 
do 
  echo  "localhost" >>  machines
  ((counter++))
done

exit
