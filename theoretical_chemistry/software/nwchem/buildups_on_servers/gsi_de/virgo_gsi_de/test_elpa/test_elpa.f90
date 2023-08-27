      program main
       use ELPA
       implicit none
       logical status
       integer i4,success
       double precision dvec8(2),dmat8(2,2)
       class(elpa_t), pointer :: e
       if (elpa_init(20170403) /= ELPA_OK) then       ! put here the version number of the API
         error stop "ELPA API version not supported"  ! which you are using
       endif
       call e%set("na", i4,success)
 
       call e%eigenvectors(dmat8, dvec8, dmat8, success)
     end
