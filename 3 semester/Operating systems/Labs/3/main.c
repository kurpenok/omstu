#include <stdio.h>
#include <fcntl.h>

unsigned int read(int handle, void* buffer, unsigned int lenght);
unsigned int write(int handle, const void* buffer, unsigned int lenght);
void sleep(int time);
void close(int handle);

int main() {
    char buffer[100];
    int lenght;

    int fhandle;

    char fname[] = "test";

    struct flock lock = {F_WRLCK, SEEK_SET, 0, 0};

    fhandle = open(fname, O_WRONLY | O_CREAT | O_TRUNC, 0777);
    fcntl(fhandle, F_SETLKW, &lock);

    write(1, "[>] Enter: ", 20);
    lenght = read(0, buffer+20, 80);
    write(fhandle, buffer, lenght+80);

    sleep(10);

    lock.l_type = F_UNLCK;

    fcntl(fhandle, F_SETLK, &lock);

    close(fhandle);

    return 0;
}
