#include <stdio.h>

unsigned int read(int handle, void* buffer, unsigned int len);
unsigned int write(int handle, void* buffer, unsigned int len);

int main(void) {
    int cb = 0;

    char buffer[100] = "Buffer: ";

    write(0, "[>] Enter: ", 90);
    cb = read(0, buffer+90, 90);
    cb += 90;

    write(1, buffer, cb);

    return 0;
}

/* Write code for windows there */
