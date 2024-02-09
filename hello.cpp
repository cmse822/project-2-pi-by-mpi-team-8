#include "mpi.h"
//#include <iostream>
#include <stdio.h>
//using namespace std;

int main(int argc, char *argv[]) 
{
    int numtasks, rank;
    printf("Hello, World! (Before Init)\n");
    MPI_Init(&argc, &argv);
    MPI_Comm_size(MPI_COMM_WORLD, &numtasks);
    MPI_Comm_rank(MPI_COMM_WORLD, &rank);
    printf("Hello, World! (After Init, Before Finalize)\n");
    MPI_Finalize();
    printf("Hello, World! (After Finalize)\n");
    return 0;
}