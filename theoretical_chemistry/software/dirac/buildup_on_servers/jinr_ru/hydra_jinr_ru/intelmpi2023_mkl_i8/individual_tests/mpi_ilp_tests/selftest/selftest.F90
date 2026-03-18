!
!
! written by Google AI by simple request
!
program mpi_selftest
    use mpi_f08  ! Recommended for Intel MPI (provides type checking)
    implicit none

    integer :: num_MPI_proc, my_MPI_rank
    integer :: my_MPI_master = 0, my_MPI_slave = 1
    integer :: big_int_arr(3), big_int_recv_arr(3)
    integer :: ierr
    type(MPI_Status) :: status  ! Required for standard MPI_RECV

    call MPI_INIT(ierr)
    call MPI_COMM_SIZE(MPI_COMM_WORLD, num_MPI_proc, ierr)
    call MPI_COMM_RANK(MPI_COMM_WORLD, my_MPI_rank, ierr)

    if (num_MPI_proc > 1) then
        if (my_MPI_rank == my_MPI_master) then
            ! Initialize data on master
            big_int_arr = [10, 20, 30]
            
            ! Standard Intel MPI Send: (buffer, count, datatype, dest, tag, comm, ierr)
            call MPI_SEND(big_int_arr, 3, MPI_INTEGER, my_MPI_slave, 26, &
                          MPI_COMM_WORLD, ierr)
        endif

        if (my_MPI_rank == my_MPI_slave) then
            ! Standard Intel MPI Receive: (buffer, count, datatype, source, tag, comm, status, ierr)
            call MPI_RECV(big_int_recv_arr, 3, MPI_INTEGER, my_MPI_master, &
                          MPI_ANY_TAG, MPI_COMM_WORLD, status, ierr)

            ! Validation (Note: big_int_arr must be known/initialized on slave to compare)
            if (any(big_int_recv_arr /= [10, 20, 30])) then
                print *, 'selftest_mpi: Error! Received:', big_int_recv_arr
                call MPI_ABORT(MPI_COMM_WORLD, 1, ierr)
            endif
        endif
    endif

    call MPI_FINALIZE(ierr)
end program

