=================
QE rocksalt test
=================

slurm does not do proper binding of MPI processes

 hydra-qe_N1.01.logfile_jid373328:

 Running QE pw.x OpenMPI parallel job:
[n05p027.gvr.local:3111008] MCW rank 0 bound to socket 0[core 19[hwt 0-1]], socket 0[core 20[hwt 0-1]]: [../../../../../../../../../../../../../../../../../../../BB/BB/../../../../../../../../../../../../../../../../..][../../../../../../../../../../../../../../../../../../../../../../../../../../../../../../../../../../../../../..]
[n05p027.gvr.local:3111008] MCW rank 2 bound to socket 0[core 19[hwt 0-1]], socket 0[core 20[hwt 0-1]]: [../../../../../../../../../../../../../../../../../../../BB/BB/../../../../../../../../../../../../../../../../..][../../../../../../../../../../../../../../../../../../../../../../../../../../../../../../../../../../../../../..]
[n05p027.gvr.local:3111013] MCW rank 1 bound to SK1:L31:L238-75:L138-75:CR38-75:HT76-151:NM1
[n05p027.gvr.local:3111015] MCW rank 3 bound to SK1:L31:L238-75:L138-75:CR38-75:HT76-151:NM1

 hydra-qe_N1.05.logfile_jid373642:
[n05p027.gvr.local:3112358] MCW rank 0 bound to socket 0[core 19[hwt 0-1]], socket 0[core 20[hwt 0-1]], socket 0[core 21[hwt 0-1]], socket 0[core 22[hwt 0-1]]: [../../../../../../../../../../../../../../../../../../../BB/BB/BB/BB/../../../../../../../../../../../../../../..][../../../../../../../../../../../../../../../../../../../../../../../../../../../../../../../../../../../../../..]
[n05p027.gvr.local:3112358] MCW rank 2 bound to socket 0[core 19[hwt 0-1]], socket 0[core 20[hwt 0-1]], socket 0[core 21[hwt 0-1]], socket 0[core 22[hwt 0-1]]: [../../../../../../../../../../../../../../../../../../../BB/BB/BB/BB/../../../../../../../../../../../../../../..][../../../../../../../../../../../../../../../../../../../../../../../../../../../../../../../../../../../../../..]
[n05p027.gvr.local:3112365] MCW rank 3 bound to SK1:L31:L238-75:L138-75:CR38-75:HT76-151:NM1
[n05p027.gvr.local:3112363] MCW rank 1 bound to SK1:L31:L238-75:L138-75:CR38-75:HT76-151:NM1


srun job
-------
It looks like even with the "ignore" flags, srun --mpi=pmix is still hitting a hard wall because your cluster's PMIx library is looking for a Munge security component that is either missing or broken on the compute nodes.
Since your previous attempt with --mpi=pmi2 explicitly stated that your OpenMPI was not built with Slurm's PMI support, you should stop trying to use srun for this specific executable. On this cluster, srun and this version of OpenMPI simply do not speak the same language.

https://share.google/aimode/4ZFsyf9ahoqp9G1FL

