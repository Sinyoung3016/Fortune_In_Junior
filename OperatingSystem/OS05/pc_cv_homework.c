#include <stdio.h>
#include <pthread.h>
#include <unistd.h>     // usleep (micro sleep)

#define MAX 10 
#define PROD_SIZE 3
#define CONS_SIZE 7
#define PROD_ITEM 5
#define CONS_ITEM 2

/* homework */
/*----------*/
/* You need to make some variables (mutex, condition variables). */
/* Reference below variables, functions. */
/*----------*/
/* homework */

pthread_mutex_t m_id = PTHREAD_MUTEX_INITIALIZER;

pthread_mutex_t m = PTHREAD_MUTEX_INITIALIZER;
pthread_cond_t c_z = PTHREAD_COND_INITIALIZER;
pthread_cond_t c_m = PTHREAD_COND_INITIALIZER;

int buffer[MAX]; // ! buffer is circular queue !
int count = 0;
int get_ptr = 0;
int put_ptr = 0;
int prod_id = 1;
int cons_id = 1;

/* homework */
// return buffer's value using get_ptr if successful,
// otherwise, -1
int get()
{
    int ret_val;
    if (0 == count)
    	return -1;
    else{
    	ret_val = buffer[get_ptr];
    	get_ptr = (get_ptr + 1) % MAX;
    	count--;
    	return ret_val;
	}
}

/* homework */
// return buffer's value using put_ptr if successful,
// otherwise, -1
int put(int val)
{
    if (MAX == count)
        return -1;
    else{
        buffer[put_ptr] = val;
        put_ptr = (put_ptr + 1) % MAX;
        count++;
        return val;
	}
}

void *producer(void *arg)
{
    pthread_mutex_lock(&m_id);
    int id = prod_id++;
    pthread_mutex_unlock(&m_id);
    for (int i = 0; i < PROD_ITEM; ++i) {
        usleep(10);

        pthread_mutex_lock(&m);
        if (count != 0)
            pthread_cond_signal(&c_z);
        if (count == MAX)
            pthread_cond_wait(&c_m, &m);    
        int ret = put(i);
        pthread_mutex_unlock(&m);

        if (ret == -1) {
            printf("can't put, because buffer is full.\n");
        } else {
            printf("producer %d PUT %d\n", id, ret);
        }
    }
}

void *consumer(void *arg)
{
    pthread_mutex_lock(&m_id);
    int id = cons_id++;
    pthread_mutex_unlock(&m_id);
    for (int i = 0; i < CONS_ITEM; ++i) {
        usleep(10);

        pthread_mutex_lock(&m);
        if(count == 0)
            pthread_cond_wait(&c_z, &m);
        if (count != MAX)
            pthread_cond_signal(&c_m);
        int ret = get();
        pthread_mutex_unlock(&m);
        
        if (ret == -1) {
            printf("can't get, because buffer is empty.\n");
        } else {
            printf("consumer %d GET %d\n", id, ret);
        }
    }
}

int main()
{
    pthread_t prod[PROD_SIZE];
    pthread_t cons[CONS_SIZE];

    for (int i = 0; i < PROD_SIZE; ++i)
        pthread_create(&prod[i], NULL, producer, NULL);
    for (int i = 0; i < CONS_SIZE; ++i)
        pthread_create(&cons[i], NULL, consumer, NULL);

    for (int i = 0; i < PROD_SIZE; ++i)
        pthread_join(prod[i], NULL);
    for (int i = 0; i < CONS_SIZE; ++i)
        pthread_join(cons[i], NULL);

    return 0;
}
