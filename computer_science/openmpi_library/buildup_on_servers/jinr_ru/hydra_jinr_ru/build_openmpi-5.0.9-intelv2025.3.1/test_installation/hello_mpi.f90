!=================================================================
! Google AI one complete testing Fortran program for openmpi
!
!  Expected output:
!
! Hello from rank    0 of    4 on node hostname
! Hello from rank    2 of    4 on node hostname
! Hello from rank    1 of    4 on node hostname
! Hello from rank    3 of    4 on node hostname
!
!


! hello_mpi.f90
program hello_mpi
    use mpi_f08
    implicit none

    integer :: ierr, rank, size
    character(len=MPI_MAX_PROCESSOR_NAME) :: name
    integer :: name_len

    ! 1. Initialize MPI
    call MPI_Init(ierr)

    ! 2. Get communicator size and rank
    call MPI_Comm_size(MPI_COMM_WORLD, size, ierr)
    call MPI_Comm_rank(MPI_COMM_WORLD, rank, ierr)

    ! 3. Get processor name
    call MPI_Get_processor_name(name, name_len)

    ! 4. Perform Task (Simple Hello World from each rank)
    write(*, '(A, I3, A, I3, A, A)') &
        "Hello from rank ", rank, " of ", size, &
        " on node ", trim(name)

    ! 5. Finalize MPI
    call MPI_Finalize(ierr)

end program hello_mpi

