#include <bits/pthreadtypes.h>
#include <fcntl.h>
#include <stdio.h>
#include <string.h>
#include <sys/stat.h>
#include <sys/types.h>
#include <unistd.h>

#define BUFFER_SIZE 255

int main(int argc, char* argv[]) {
    char buffer[BUFFER_SIZE];

    int firstHandle = open(argv[1], O_RDONLY);
    int secondHandle = dup(firstHandle);
    int thirdHandle = dup(firstHandle);

    printf("[+] First handle: %d\n", firstHandle);
    printf("[+] Second handle: %d\n", secondHandle);
    printf("[+] Third handle: %d\n", thirdHandle);

    lseek(firstHandle, 10, SEEK_CUR);
    
    read(firstHandle, buffer, 7);
    printf("%s\n", buffer);
    
    read(secondHandle, buffer, 7);
    printf("%s\n", buffer);

    read(thirdHandle, buffer, 7);
    printf("%s\n", buffer);
} 
