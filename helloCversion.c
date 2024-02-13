#include "mpi.h"
//#include <iostream>
#include <stdio.h>
//using namespace std;

int main(int argc, char *argv[]) 
{
    int numtasks, rank;
    //printf("Hello, World! (Before Init)\n");
    MPI_Init(&argc, &argv);
    MPI_Comm_size(MPI_COMM_WORLD, &numtasks);
    MPI_Comm_rank(MPI_COMM_WORLD, &rank);
    //printf("Hello, World! (After Init, Before Finalize)\n");
    int name_length = MPI_MAX_PROCESSOR_NAME;
    char proc_name[name_length];
    MPI_Get_processor_name(proc_name, &name_length);
    printf("Process %d%d is running on node <<%s>>\n", procid, nprocs, proc_name)



    MPI_Finalize();
    //printf("Hello, World! (After Finalize)\n");
    return 0;
}