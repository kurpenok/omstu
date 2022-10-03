#include <fcntl.h>
#include <stdio.h>
#include <string.h>
#include <sys/stat.h>
#include <sys/types.h>
#include <unistd.h>

#define BUFFER_SIZE 255

int main(int argc, char* argv[]) {
    char buffer[BUFFER_SIZE];

    if (argc == 1) {
        printf("[>] Enter anything: ");
        read(0, buffer, BUFFER_SIZE);
        write(0, buffer, strlen(buffer));
    } else if (argc == 2) {
        printf("[>] Enter anything: ");
        read(0, buffer, BUFFER_SIZE);
        int inFile = open(argv[1], O_CREAT | O_WRONLY);
        write(inFile, buffer, strlen(buffer));
    } else if (argc == 3) {
        printf("[+] Read from file: %s\n", argv[1]);
        
        int outFile = open(argv[1], O_RDONLY);
        if (outFile <= 0) {
            printf("[-] File %s not found!", argv[1]);
            return 1;
        }

        int inFile = open(argv[2], O_CREAT | O_WRONLY);
        if (inFile <= 0) {
            printf("[-] File %s not found!", argv[2]);
            return 1;
        }

        printf("[+] File handle for read %d\n", outFile);
        printf("[+] File handle for write %d\n", inFile);
        while (read(outFile, buffer, BUFFER_SIZE));
        write(inFile, buffer, strlen(buffer));
        printf("[+] In file was writed: %s\n", buffer);
    }

    return 0;
}
