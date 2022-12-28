#include<stdio.h>
#include <sys/types.h>
#include <unistd.h>
#include <string.h>
#include <pthread.h>
#include <sys/stat.h>
#include <fcntl.h>
#include <semaphore.h>
#include <stdlib.h>
#include <errno.h>
#include <sys/mman.h>
#include <sys/shm.h>
#define BUFFERSIE 1000

char* sem_name = "sem192";
char* shm_name = "shm192";

int main(){
 printf("fork ok\n");
        sem_t *sem = sem_open(sem_name, 0, 0);
        int fd = shm_open(shm_name, O_CREAT | O_RDWR, S_IRUSR | S_IWUSR);
        if (fd == -1) {
            perror("shm_open");
            exit(EXIT_FAILURE);
        }
        ftruncate(fd, BUFFERSIE);
        char *str = mmap(NULL, sizeof(char) * 1000, PROT_READ | PROT_WRITE, MAP_SHARED, fd, 0);
        printf("i get first message: %s\n", str);
        sleep(1);
        int sem_val;
        sem_getvalue(sem, &sem_val);
        while (sem_val == 0) sem_getvalue(sem, &sem_val);
        printf("i get second message: %s\n", str);
}
