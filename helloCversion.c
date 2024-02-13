#include "mpi.h"
//#include <iostream>
#include <stdio.h>
//using namespace std;

int main(int argc, char *argv[]) 
{
    int numtasks, rank;
    //printf("Hello, World! (Before Init)\n");

    // Initialize MPI
    MPI_Init(&argc, &argv);
    MPI_Comm_size(MPI_COMM_WORLD, &numtasks);
    MPI_Comm_rank(MPI_COMM_WORLD, &rank);

    //printf("Hello, World! (After Init, Before Finalize)\n");

    // Get max processor names
    int name_length = MPI_MAX_PROCESSOR_NAME;
    char proc_name[name_length];
    MPI_Get_processor_name(proc_name, &name_length);
    //printf("Process %d of %d is running on node <<%s>>\n", rank, numtasks, proc_name);
    //In line above, removed procid, nprocs from printf 


    // Create a file, write, then close 
    char filename[10]
    sprintf(filename, "file_%d.txt", rank);
    FILE *file = fopen(filename, 'w');
    fprintf("Hello from process %d of %d!\n", rank, numtasks);
    fclose(file);


    //printf("Hello from process %d of %d!\n", rank, numtasks);
    MPI_Finalize();
    //printf("Hello, World! (After Finalize)\n");
    return 0;
}