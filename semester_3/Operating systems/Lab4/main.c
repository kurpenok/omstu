#include <stdio.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <fcntl.h>
#include <unistd.h>
#include <errno.h>
#include <string.h>

#define BUFFERSIZE 255

int main (int argc, char* argv[]) {
    int file = open ("file.txt", O_RDWR);
    char buffer[BUFFERSIZE];
    if(file == -1) {
        printf("file dont open with error %d\n", errno);
        return -1;
    } else {
        struct flock flptr;
        flptr.l_start = 0;
        flptr.l_whence = SEEK_SET;
        flptr.l_len = 0;
        flptr.l_type = F_WRLCK;
        
        while (fcntl(file, F_SETLK, &flptr) == -1) {
            printf("\033[1;31mcant change lock with error %d\033[0m\n", errno);
            sleep(1);
        }
        printf("\033[1;32mblock sucsesfull!\n");
        
        if (read(file, buffer, BUFFERSIZE) == -1) {
            printf("\033[1;31mdont read with error %d\033[0m\n", errno);
        }

        printf("\033[1;32mfrom file was read %s\033[0m\n", buffer);
        sleep(20);
        flptr.l_type = F_ULOCK;
        
        if (fcntl(file, F_SETLK, &flptr) == -1) {
            printf("\033[1;31mcant unlock file with error%d\033[0m\n", errno);
        } else {
            printf("\033[1;32mfile unlock\033[0m\n");
        }
    }

    return 0;
}
