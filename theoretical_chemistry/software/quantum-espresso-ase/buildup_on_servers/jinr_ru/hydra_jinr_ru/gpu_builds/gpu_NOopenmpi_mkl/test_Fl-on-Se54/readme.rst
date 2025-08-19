QE GPU test
===========

GPU build pw.x executable is crashing upon launch,

 OMP_NUM_THREADS=4
OMP: Error #13: Assertion failure at kmp_alloc.cpp(1871).
OMP: Hint: Please submit a bug report with this message, compile and run commands used, and machine configuration info including native compiler and operating system versions. Faster response will be obtained by including all program sources. For information on submitting this issue, please see http://www.intel.com/software/products/support/.
/tmp/slurmd/job13266069/slurm_script: line 157: 16348 Aborted                 (core dumped) $QE/$BUILD/bin/pw.x < $inp > $out


srun: error: fwd_tree_thread: can't find address for host ampere01, check slurm.conf
srun: error: Task launch for 13289877.0 failed on node ampere01: Can't find an address, check slurm.conf
srun: error: Application launch failed: Can't find an address, check slurm.conf
srun: Job step aborted: Waiting up to 122 seconds for job step to finish.
srun: error: Timed out waiting for job step to complete


it gives empty output file, like Se54_r_Fl.gvr.ampere.N1.n4.jid13289877.out


