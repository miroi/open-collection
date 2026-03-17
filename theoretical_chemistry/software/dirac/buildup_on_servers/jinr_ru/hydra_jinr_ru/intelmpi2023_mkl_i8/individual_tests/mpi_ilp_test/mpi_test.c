#include <mpi.h>
#include <stdio.h>

int main(int argc, char** argv) {
    MPI_Init(&argc, &argv);
    printf("Size of MPI_Count: %lu bytes\n", (unsigned long)sizeof(MPI_Count));
    // In ILP64, this should return 8.
    MPI_Finalize();
    return 0;
}

