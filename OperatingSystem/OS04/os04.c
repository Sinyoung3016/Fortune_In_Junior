#include <stdio.h>
#include <pthread.h>

pthread_mutex_t lock;

static volatile int counter = 0;
static const int end = 100000000;

typedef struct {char * id; int val; } myarg;

void *mythread(void *arg)
{
	myarg *ma = (myarg *) arg;
	printf("%s[%u]: begin\n", ma->id, (unsigned) pthread_self());
	
	pthread_mutex_lock(&lock);
	for (int i = 0; i < end; i++){
		--counter;
		ma->val++;
	}
	pthread_mutex_unlock(&lock);
	printf("%s[%u]: done\n", ma->id, (unsigned) pthread_self());
	return (void *) ma;
}

int main()
{
	printf("main[%u]: begin (counter = %d)\n", (unsigned) pthread_self(), counter);
	pthread_t t1, t2;
	myarg ma1 = {"A", end};
	myarg ma2 = {"B", end}; 
	
	pthread_mutex_init(&lock, NULL);
	pthread_create(&t1, NULL, mythread, &ma1);
	pthread_create(&t2, NULL, mythread, &ma2);
	
	pthread_mutex_lock(&lock);
	for (int i = 0; i < end; i++)
		counter++;
	pthread_mutex_unlock(&lock);
	pthread_join(t1, (void **) &ma1);
	pthread_join(t2, (void **) &ma2);
	printf("main[%u]: done (counter = %d) (ma1.val = %d)\n", 
	(unsigned) pthread_self(), counter, ma1.val);
	return 0;
}

