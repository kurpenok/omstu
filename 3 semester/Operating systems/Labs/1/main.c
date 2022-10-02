#include <stdio.h>

unsigned int read(int handle, void* buffer, unsigned int len);
unsigned int write(int handle, void* buffer, unsigned int len);

int main(void) {
    int cb = 0;

    char buffer[100] = "Buffer";
    
    write(0, "[>] Enter: ", 11);
    cb = read(0, buffer+10, 80);
    cb += 10;

    write(1, buffer, cb);

    return 0;
}
