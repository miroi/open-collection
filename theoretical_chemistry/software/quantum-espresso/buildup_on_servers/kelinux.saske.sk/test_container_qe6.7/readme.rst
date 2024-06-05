Q.E. 6.7 in container
=====================

https://researchcomputing.princeton.edu/support/knowledge-base/quantum-espresso

kontainer quantum_espresso_v6.7.sif je nepouzitelny:


... launching singularity run = first test :
level=info msg="Legacy NVIDIA Driver detected(440.33.01). Compatibility mode ENABLED."
level=warning msg="Failed to check and/or legacy OFED: Unable to match host OFED version: No compatible legacy mellanox OFED versions found"
/var/spool/slurm/d/job1205697/slurm_script: line 38: 12052 Illegal instruction     singularity run --nv /lustre/home/ilias/containers/quantum_espresso_v6.7.sif pw.x

 ... launching singularity run = quantum_espresso_v6.7.sif container :
level=info msg="Legacy NVIDIA Driver detected(440.33.01). Compatibility mode ENABLED."
level=warning msg="Failed to check and/or legacy OFED: Unable to match host OFED version: No compatible legacy mellanox OFED versions found"
srun: error: comp47: tasks 0,2: Illegal instruction
srun: error: comp47: task 1: Illegal instruction
srun: error: comp47: task 3: Illegal instruction


