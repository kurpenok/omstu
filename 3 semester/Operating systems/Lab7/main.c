#include <pthread.h>
#include <stdio.h>
#include <signal.h>

char buffer[] = "abcdefghijklmnopqrstuvwxyz";
pthread_t th1, th2, th3;

void thread1(void* arg) {
    pthread_setcancelstate(PTHREAD_CANCEL_DISABLE, NULL);

    for (int i = 0; i < 20; i++) {

        printf("\033[%d;20H\033[31m", i + 1);

        for (int j = 0; j < (int)arg; j++) {
            printf("%c", buffer[i]);
        }

        printf("\n");
        usleep(1011000);
    }
    pthread_exit(0);
}

void thread2(void* arg) {
    for (int i = 0; i < 20; i++) {

        printf("\033[%d;40H\033[33m", i + 1);

        for (int j = 0; j < (int)arg; j++) {
            printf("%c", buffer[i]);
        }

        printf("\n");
        usleep(1022000);
    }
    pthread_exit(0);
}

void thread3(void* arg) {
    pthread_setcancelstate(PTHREAD_CANCEL_DISABLE, NULL);
    pthread_setcanceltype(PTHREAD_CANCEL_DEFERRED, NULL);

    for (int i = 0; i < 20; i++) {
        if (i == 12) {
            pthread_setcancelstate(PTHREAD_CANCEL_ENABLE, NULL);
        }

        if (i == 16) {
            pthread_testcancel();
        }

        printf("\033[%d;60H\033[32m", i + 1);
        
        for (int j = 0; j < (int)arg; j++) {
            printf("%c", buffer[i]);
        }

        printf("\n");
        usleep(1033000);
    }
    pthread_exit(0);
}

int main() {
    void* status = NULL;

    printf("\033[H\033[J");

    if (pthread_create(&th1, NULL, (void*)thread1, (void*)2)) {
        printf("\033[21;1H");
        printf("\033[21;1H\033[34m[-] Error create thread 1\n");
    }

    if (pthread_create(&th2, NULL, (void*)thread2, (void*)4)) {
        printf("\033[21;1H");
        printf("\033[21;1H\033[34m[-] Error create thread 2\n");
    }

    if (pthread_create(&th3, NULL, (void*)thread3, (void*)6)) {
        printf("\033[21;1H");
        printf("\033[21;1H\033[34m[-] Error create thread 3\n");
    }

    fflush(stdout);

    for (int i = 0; i < 20; i++) {
        printf("\033[%d;1H\033[37m", i + 1);
        printf("%d %c\n", i + 1, buffer[i]);

        if (i == 5) {
            pthread_cancel(th1);
            printf("\033[21;1H");
            printf("\033[21;1H\033[34m[+] Attempt to cancel thread 1\n");
        }

        if (i == 10) {
            pthread_cancel(th1);
            printf("\033[21;1H");
            printf("\033[21;1H\033[34m[+] Attempt to cancel thread 3\n");
        }

        usleep(1000000);
    }

    printf("\033[21;1H");
    getchar();
    printf("\033]37m");

    return 0;
}
