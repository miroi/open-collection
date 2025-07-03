ERROR in tests:

DIRAC pam run in /lustre/home/user/m/milias/work/software/dirac/trunk_study/build_openmpi5_mkl_i8/test/spinrot

 ====  below this line is the stderr stream  ====
[n05p016:00000] *** An error occurred in MPI_Comm_rank
[n05p016:00000] *** reported by process [1602093057,0]
[n05p016:00000] *** on communicator MPI_COMM_WORLD
[n05p016:00000] *** MPI_ERR_COMM: invalid communicator
[n05p016:00000] *** MPI_ERRORS_ARE_FATAL (processes in this communicator will now abort,
[n05p016:00000] ***    and MPI will try to terminate your MPI job as well)
--------------------------------------------------------------------------
prterun has exited due to process rank 0 with PID 0 on node n05p016 calling
"abort". This may have caused other processes in the application to be
terminated by signals sent by prterun (as reported here).

