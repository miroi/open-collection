program check_ilp64
    use mpi
    implicit none
    integer :: ierr, sz, my_int_sz

    call MPI_INIT(ierr)
    
    ! Check default Fortran integer size
    my_int_sz = sizeof(1) 
    
    ! Check MPI's view of an integer
    call MPI_TYPE_SIZE(MPI_INTEGER, sz, ierr)

    print *, "Default Fortran Integer Size: ", my_int_sz, " bytes"
    print *, "MPI_INTEGER Size: ", sz, " bytes"

    if (sz == 8) then
        print *, "Status: ILP64 build confirmed."
    else
        print *, "Status: LP64 (32-bit integer) build detected."
    end if

    call MPI_FINALIZE(ierr)
end program

