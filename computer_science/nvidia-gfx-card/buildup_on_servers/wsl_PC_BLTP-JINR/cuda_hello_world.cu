/* 

https://cuda-tutorial.readthedocs.io/en/latest/tutorials/tutorial01/   

*/

#include <iostream>
#include <stdio.h>

__global__ void cuda_hello(){
    printf("Hello World from GPU!\n");
 //   std::cout << "Hello World from GPU!\n"  << std::endl;
}

int main() {
    cuda_hello<<<1,1>>>(); 
    printf("Hello World from printf !\n");
    return 0;
}
