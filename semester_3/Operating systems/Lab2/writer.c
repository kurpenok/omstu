#include <fcntl.h>
#include <stdio.h>
#include <unistd.h>

int main() {
    char buffer[100] = "[+] ";
    char fname[] = "file";

    int handle;
    int count;

    printf("[>] Enter text: \n");

    handle = open(fname, O_WRONLY | O_CREAT | O_TRUNC, S_IRWXU);
    count = read(0, buffer, 100);

    write(handle, buffer, count);

    close(handle);

    return 0;
}
