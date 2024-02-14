#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include "mpi.h"

int main(int argc, char *argv[]) {
    MPI_Status Stat;
    int numtasks, rank, len, rc, dest, source, count, tag = 1;

    MPI_Init(&argc, &argv);
    MPI_Comm comm = MPI_COMM_WORLD;
    MPI_Comm_size(MPI_COMM_WORLD, &numtasks);
    MPI_Comm_rank(MPI_COMM_WORLD, &rank);

    double time_start = MPI_Wtime();

    int pi_sum, pi = 0;
    if (rank == 0) {
        printf("Number of tasks: %d\n", numtasks);
    }

    if (rank == 2) {
        printf("Rank: %d waiting...\n", rank);
        sleep(2);
    }

    pi = rank;
    MPI_Reduce(&pi, &pi_sum, 1, MPI_INT, MPI_SUM, 0, comm);

    printf("Rank: %d blocked...\n", rank);
    MPI_Barrier(comm);
    printf("Rank: %d finished.\n", rank);

    double time_end = MPI_Wtime();

    printf("Total time: %f for rank %d\n", (time_end - time_start), rank);
    MPI_Finalize();
    if (rank == 0) {
        printf("Pi Avg.: %d \n", pi_sum/numtasks);

    }
}