======================
GAMESS-US on Windows11
======================

serial tests
~~~~~~~~~~~~

C:\Users\Public\gamess-64>runall.bat 2023.R1.intel 1
-------------------------------------------------------------------------

Usage: runall.bat [version] [ncpus]
 [version] = The GAMESS version number                      (default: 00)
 [ncpus]   = The number of CPUs requested for this job      (default:  1)
             [ncpus] = 1 will run all the exam files in serial
             [ncpus] > 1 will run all the exam files in parallel except
             for 05, 23, 25, 27, 32, 39, 42, and 45-47 which only run in serial
=========================================================================
----------------------------------------------
  Running GAMESS exam files 1 - 49 in serial
  Using gamess.2023.R1.intel.exe binary
  NCPUS = 1
----------------------------------------------
  Running exam01
  Running exam02
  Running exam03
  Running exam04
  Running exam05
  Running exam06
  Running exam07
  Running exam08
  Running exam09
  Running exam10
  Running exam11
  Running exam12
  Running exam13
  Running exam14
  Running exam15
  Running exam16
  Running exam17
  Running exam18
  Running exam19
  Running exam20
  Running exam21
  Running exam22
  Running exam23
  Running exam24
  Running exam25
 Running exam26
  Running exam27
  Running exam28
  Running exam29
  Running exam30
  Running exam31
  Running exam32
  Running exam33
  Running exam34
  Running exam35
  Running exam36
  Running exam37
  Running exam38
  Running exam39
  Running exam40
  Running exam41
  Running exam42
  Running exam43
  Running exam44
  Running exam45
  Running exam46
  Running exam47
  Running exam48
  Running exam49
----------------------------------------------
-                    FIN                     -
----------------------------------------------

C:\Users\Public\gamess-64>clean-runall-files.bat


clean files
~~~~~~~~~~~
C:\Users\Public\gamess-64>clean-runall-files.bat

Finish removing exam*log, scratch\exam*.*, and restart\exam*.* files

Press any key to continue . . .

C:\Users\Public\gamess-64>

parallel tests
~~~~~~~~~~~~~~
C:\Users\Public\gamess-64>runall.bat 2023.R1.intel 4
-------------------------------------------------------------------------

Usage: runall.bat [version] [ncpus]
 [version] = The GAMESS version number                      (default: 00)
 [ncpus]   = The number of CPUs requested for this job      (default:  1)
             [ncpus] = 1 will run all the exam files in serial
             [ncpus] > 1 will run all the exam files in parallel except
             for 05, 23, 25, 27, 32, 39, 42, and 45-47 which only run in serial
=========================================================================
----------------------------------------------
 Running GAMESS exam files 1 - 49 in parallel

  The following serial-only jobs are omitted
  05, 23, 25, 27, 32, 39, 42, 45, 46, and 47

  Using gamess.2023.R1.intel.exe binary
  NCPUS = 4
----------------------------------------------
  Running exam01
  Running exam02
  Running exam03



