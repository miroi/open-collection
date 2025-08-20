Test run of GPU-QE
==================

Se54_r_Fl.gvr.dgx.N1.n12.jid13328749.out

    Estimated static dynamical RAM per process >     197.15 GB
    Estimated max dynamical RAM per process >     293.78 GB

log_slurm_job.xxxx.dgx03.std_out_err:

Accelerator Fatal Error: call to cuMemAlloc returned error 2 (CUDA_ERROR_OUT_OF_MEMORY): Out of memory
 File: /lustre/home/user/m/milias/work/software/quantum-espresso/qe-develop/q-e/PW/src/allocate_wfc.f90
 Function: allocate_wfc_k:10
 Line: 45






