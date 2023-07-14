=============================
MtH(CO)4 with DIRAC on Summit 
=============================

MtHCO4.x2c_a4p.scf1fs_exacct_occm40-vir1000_Mt-Hax-CO_4.cv3z.C1.3053936.out_SAVEDfail :
----------------------------------------------------------------------------------------
 Using the multi-node ExaTensor library (MPI) 
 - ExaTensor block size :              75
!! ATTENTION !! Properties require TALSH, density matrix must be smaller than: 
 - TALSH buffer size:                 50 GB
 
 - Print Level :                        4
 
 - Estimating memory requirements
 -- nao  ( scheme 1-3  ) :     28385 GB
 -- nvir ( scheme 4/42 ) :     59140 GB
-----------------------------------------------
 
#ERROR(ExaTensor::service_mpi::dil_process_start): unable to open a log file!
###ExaTENSOR Process        16: Error           -1: Wall Time (sec):         0.91

MtHCO4.x2c_a4p.scf1fs_exacct_occm18-vir100_Mt-Hax-CO_4.cv3z.C1.3055972.out_SAVEDfail:
--------------------------------------------------------------------------------------
.
.
     994   0.912885802E+02
  13 Jul 23 19:37:18  Starting CC calculation with exatensor
In the current implementation there is a scaling limit.
Using your configuration there would be nodes doing no work.
Therefore decrease the number of MPI processes or .EXA_BLOCKSIZE

 Slave node   1 :  --- SEVERE ERROR, PROGRAM WILL BE ABORTED ---      

see  https://diracprogram.org/doc/master/manual/wave_function/exacorr.html#exa-blocksize   default=75, try lower value
