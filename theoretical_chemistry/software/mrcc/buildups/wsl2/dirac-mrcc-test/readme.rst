===============
MRCC-DIRAC test
===============

see  https://gitlab.com/dirac/dirac/-/tree/master/test/benchmark_kallay_mrcc_interface

Victus Notebook
---------------

PC Desktop
-----------
milias@DESKTOP-7OTLCGO:~/work/software/dirac/trunk_cloned/test/benchmark_kallay_mrcc_interface/.export MRCCDIR=/home/milias/work/software/mrcc
milias@DESKTOP-7OTLCGO:~/work/software/dirac/trunk_cloned/test/benchmark_kallay_mrcc_interface/.export DIRAC_UTILS_PATH=/home/milias/work/software/dirac/trunk_cloned/build_gnu_mkl_ilp64

milias@DESKTOP-7OTLCGO:~/work/software/dirac/trunk_cloned/test/benchmark_kallay_mrcc_interface/../test -b /home/milias/work/software/dirac/trunk_cloned/build_gnu_mkl_ilp64

running test: ccsd CO_C2v
ERROR: test ccsd_CO_C2v.out failed

  Initialized reading from MRCONEE (version DIRAC20 and later)
  Core energy:   -80.273643033836422
  Breit interaction:  F
  Group type (1:real, 2:complex, 4:quaternion) :                    1
  Initialized reading from MDCINT
  MDCINT created:  20251020   11:45:04
 Generation of CC equations in terms of H and T...
 Generation of antisymmetrized Goldstone diagrams...
 Translation of diagrams to factorized equations...
 Optimizing intermediate calculation...
 Number of floating-point operations per iteration step:   0.0000E+00
 Probable CPU time per iteration step (hours):      0.00
 Required memory (Mbytes):       0.0
 Number of intermediates:                                   0
 Number of intermediates to be stored:                      0
 Length of intermediate file (Mbytes):       0.0
 Input file does not exist!
1
Traceback (most recent call last):
  File "/home/milias/work/software/dirac/trunk_cloned/test/benchmark_kallay_mrcc_interface/./test", line 40, in <module>
    os.unlink('fort.10')
FileNotFoundError: [Errno 2] No such file or directory: 'fort.10'
milias@DESKTOP-7OTLCGO:~/work/software/dirac/trunk_cloned/test/benchmark_kallay_mrcc_interface/.

