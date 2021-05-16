#include <stdio.h>
#include <stdlib.h>
#include <pthread.h>
#include <unistd.h>

typedef struct {
    int pid;
} proc_t;

typedef struct {
    proc_t *proc_info;
} thread_info_t; 

proc_t p;
thread_info_t *thd;

pthread_mutex_t m = PTHREAD_MUTEX_INITIALIZER;
pthread_cond_t c = PTHREAD_COND_INITIALIZER;

int count = 0;

void *thread1(void *arg);
void *thread2(void *arg);

int main(int argc, char *argv[]) {                    
    thread_info_t t;
    p.pid = 100;
    t.proc_info = &p;
    thd = &t;

    pthread_mutex_init(&m, NULL);
    pthread_cond_init(&c, NULL);
    
    pthread_t p1, p2;
    printf("main: begin\n");
    pthread_create(&p1, NULL, thread1, NULL); 
    pthread_create(&p2, NULL, thread2, NULL);
    // join waits for the threads to finish
    pthread_join(p1, NULL); 
    pthread_join(p2, NULL); 
    printf("main: end\n");
    return 0;
}

void *thread1(void *arg) {
	pthread_mutex_lock(&m);
	if(count == 0){
		printf("start with thread1");
		count = 1;
		pthread_cond_wait(&c, &m);
    }
    pthread_mutex_unlock(&m);
    
    printf("t1: before check\n");
    if (thd->proc_info) {
        printf("t1: after check\n");
        sleep(2);
        printf("t1: use!\n");
        printf("%d\n", thd->proc_info->pid);
    }
    pthread_cond_signal(&c);
    
    return NULL;
}

void *thread2(void *arg) {
	pthread_mutex_lock(&m);
	printf("                 t2: begin\n");
	if (count == 1)
		pthread_cond_signal(&c);
	count = 2;
    pthread_mutex_unlock(&m);
    
    pthread_cond_wait(&c, &m);
    
    sleep(1); // change to 5 to make the code "work"...
    printf("                 t2: set to NULL\n");
    thd->proc_info = NULL;
    return NULL;
}

