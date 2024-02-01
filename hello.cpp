#include "mpi.h"
#include <iostream>
using namespace std;

int main(int argc, char *argv[]) 
{
    int numtasks, rank;
    cout << "Hello, World! (Before Init)" << endl;
    MPI_Init(&argc, &argv);
    MPI_Comm_size(MPI_COMM_WORLD, &numtasks);
    MPI_Comm_rank(MPI_COMM_WORLD, &rank);
    cout << "Hello, World! (After Init, Before Finalize)" << endl;
    MPI_Finalize();
    cout << "Hello, World! (After Init)" << endl;
    return 0;
}