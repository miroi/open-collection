#!/bin/bash

export SLURM_CPUS_ON_NODE=16

echo '#' > machines

counter=1
while [ $counter -le $SLURM_CPUS_ON_NODE ] 
do 
  echo  "localhost" >  machines
  ((counter++))
done

exit
