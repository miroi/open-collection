OpenMPI DIRAC
=============

fixing by:
https://stackoverflow.com/questions/49239681/a-request-was-made-to-bind-to-that-would-result-in-binding-more-processes-than

another problem - exceeding 32bit integers

 ERROR reading environment variable DIRWRK
 ERROR cannot convert to 32 bit integer, value = 7516000000                                      
  =>   Either reduce value to at most 2147483647 or compile Dirac with 64 bit integers

reduced memory allocations "--gb=16 --ag=18" to satisfy 32bit integers

Total WALL time used in DIRAC: 3h26min4s !!! takes too long !!!

