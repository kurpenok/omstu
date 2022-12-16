#include <fcntl.h>
#include <stdio.h>
#include <unistd.h>

int main() {
    char fname[] = "file";

    int handle1;
    int handle2;
    int handle3;

    char out[7];
    int a;

    handle1 = open(fname, O_RDONLY, 0);
    handle2 = dup(handle1);
    handle3 = open(fname, O_RDONLY, 0);
    lseek(handle1, 10, SEEK_SET);

    printf("[+] First handle: %d\n", handle1);
    printf("[+] Dup handle: %d\n", handle2);
    printf("[+] Second handle: %d\n", handle3);

    fflush(stdout);

    a = read(handle1, out, 7);
    write(1, out, a);
    printf("\n");

    a = read(handle2, out, 7);
    write(1, out, a);
    printf("\n");

    a = read(handle3, out, 7);
    write(1, out, a);
    printf("\n");

    close(handle1);
    close(handle2);
    close(handle3);

    return 0;
}
