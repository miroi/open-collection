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


MtHCO4.x2c_a4p.scf1fs_exacct_occm18-vir100_Mt-Hax-CO_4.cv3z.C1.3058357.out_SAVEDunfinished:
-------------------------------------------------------------------------------------------
.
 - ExaTensor block size :              75
!! ATTENTION !! Properties require TALSH, density matrix must be smaller than: 
 - TALSH buffer size:                 50 GB
 
 - Print Level :                        4
 
 - Estimating memory requirements
 -- nao  ( scheme 1-3  ) :     28385 GB
 -- nvir ( scheme 4/42 ) :     24060 GB
-----------------------------------------------
 
  14 Jul 23 22:42:54 MO occupation data to EXACC file
  14 Jul 23 22:43:26 -Start- Integral Transformation
  14 Jul 23 22:43:50 choosing moint_scheme 4
  14 Jul 23 22:46:33 finished transforming subspace     1 of    12
  14 Jul 23 22:49:00 finished transforming subspace     2 of    12
stopped here      71-152 occup, 153-994 occup


MtHCO4.x2c_a4p.scf1fs_exacct_occm18-vir53_Mt-Hax-CO_4.cv3z.C1.3059584.out_SAVEDfail:
-------------------------------------------------------------------------------------
 - Number of atomic orbitals :        877
 - Number of occupied spinors :        82
 - Number of virtual spinors :        756
 
 Using the multi-node ExaTensor library (MPI) 
 - ExaTensor block size :              75
!! ATTENTION !! Properties require TALSH, density matrix must be smaller than: 
 - TALSH buffer size:                 50 GB
 
 - Print Level :                        4
 
 - Estimating memory requirements
 -- nao  ( scheme 1-3  ) :     28385 GB
 -- nvir ( scheme 4/42 ) :     15649 GB
 
  15 Jul 23 11:51:36 MO occupation data to EXACC file
  15 Jul 23 11:52:24 -Start- Integral Transformation
  15 Jul 23 11:52:31 choosing moint_scheme 4
  15 Jul 23 11:55:09 finished transforming subspace     1 of    12
  15 Jul 23 11:57:04 finished transforming subspace     2 of    12
  15 Jul 23 11:59:38 finished transforming subspace     3 of    12
  15 Jul 23 12:01:53 finished transforming subspace     4 of    12
  15 Jul 23 12:04:12 finished transforming subspace     5 of    12
  15 Jul 23 12:06:16 finished transforming subspace     6 of    12
DIRAC pam run in /autofs/nccs-svm1_home1/milias/work/projects/open-collection/theoretical_chemistry/software_runs/dirac/servers/ornl/summit/Mt-H-CO_4

 ====  below this line is the stderr stream  ====
Program received signal SIGSEGV: Segmentation fault - invalid memory reference.

MtHCO4.x2c_a4p.scf1fs_exacct_occm18-vir15_Mt-Hax-CO_4.cv3z.C1.3059671.out_SAVED_crash:
---------------------------------------------------------------------------------------
 - Number of atomic orbitals :        877
 - Number of occupied spinors :        82
 - Number of virtual spinors :        624
 
 Using the multi-node ExaTensor library (MPI) 
 - ExaTensor block size :              75
!! ATTENTION !! Properties require TALSH, density matrix must be smaller than: 
 - TALSH buffer size:                 50 GB
 
 - Print Level :                        4
 
 - Estimating memory requirements
 -- nao  ( scheme 1-3  ) :     28385 GB
 -- nvir ( scheme 4/42 ) :      7263 GB
 
  15 Jul 23 23:57:04 MO occupation data to EXACC file
  15 Jul 23 23:57:48 -Start- Integral Transformation
  15 Jul 23 23:57:58 choosing moint_scheme 4
  15 Jul 23 23:59:46 finished transforming subspace     1 of    12
  16 Jul 23 00:01:01 finished transforming subspace     2 of    12
  16 Jul 23 00:02:50 finished transforming subspace     3 of    12
  16 Jul 23 00:04:21 finished transforming subspace     4 of    12
  16 Jul 23 00:06:04 finished transforming subspace     5 of    12
  16 Jul 23 00:07:25 finished transforming subspace     6 of    12
DIRAC pam run in /autofs/nccs-svm1_home1/milias/work/projects/open-collection/theoretical_chemistry/software_runs/dirac/servers/ornl/summit/Mt-H-CO_4

 ====  below this line is the stderr stream  ====
Warning, specify multiple instances of the same option to jsrun, take the last one

Program received signal SIGSEGV: Segmentation fault - invalid memory reference.


