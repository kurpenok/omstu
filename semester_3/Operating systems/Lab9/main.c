#include<stdio.h>
#include <sys/types.h>
#include <unistd.h>
#include <string.h>
#include <pthread.h>
#include <sys/stat.h>
#include <sys/shm.h>
#include <fcntl.h>
#include <semaphore.h>
#include <stdlib.h>
#include <errno.h>
#include <sys/mman.h>
#define BUFFERSIE 1000

char* sem_name = "sem92";
char* shm_name = "shm192";
char* text = "Hello from main 1";
char* text2 = "Hello from main 2";
int main() {
    sleep(5);
    sem_t* sem = sem_open(sem_name, O_CREAT, 0777);
    sem_post(sem);
    int fd = shm_open(shm_name, O_RDWR, 0);
    if (fd == -1) {
    perror("shm_open");
    char* str = mmap(NULL, BUFFERSIE, PROT_READ | PROT_WRITE, MAP_SHARED, fd, 0);
    sem_wait(sem);
    printf("i send first message \n");
    int a = strlen(text);
    memcpy(str, text, strlen(text));
/*    if (0 == fork()) {
        printf("fork ok");
        if (execle("app",NULL) == -1) printf("Error to creat process %d\n", errno);
        perror("execle");
    } else {*/
        sleep(10);
        printf("i send second message\n");
        memcpy(str, text2, strlen(text2));
        sem_post(sem);

        // free sem and shm
        sem_close(sem);
        shm_unlink(shm_name);
}
}
