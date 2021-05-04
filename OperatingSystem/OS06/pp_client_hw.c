#include <stdio.h>
#include <unistd.h>
#include <semaphore.h>
#include <sys/stat.h>
#include <fcntl.h>
#include <string.h>
#include <stdlib.h>
#include <sys/mman.h> 


#define FIFO_PATH "fifo_temp"
#define SEM_NAME "sem_pp"
#define BUF_SIZE 8
#define TURN 5

int main()
{
    const char *msg = "pong\n";
    int score = 100;
    sem_t *p_sem;
    int cnt = 0;
    int fd;
    char buf[BUF_SIZE];
    int receive = 0;
    
    sem_unlink("my_sem");
    if ((p_sem = sem_open("my_sem", O_CREAT, 0600, 1)) == SEM_FAILED) {
        perror("sem_open");
        exit(1);
    }

    for(int i = 0; i < 10; i++){
    	if(cnt%2 == 1){    
        	printf ("your turn!\n");  
    		fd = open(FIFO_PATH, O_WRONLY);
    		sem_wait(p_sem);
        	memset(buf, 0, BUF_SIZE);
        	fgets(buf, BUF_SIZE, stdin);
        	write(fd, buf, strlen(buf));
        	cnt++;
        	if(strcmp(buf,msg)){
	    		score -= 20;
	    		printf ("wrong! -20\n");
		}else
	    		printf ("good!\n");  
        	sem_post(p_sem);  
        	 
    		close(fd);	
    	}else{
    		fd = open(FIFO_PATH, O_RDONLY);
    		while(1) {
        		sem_wait(p_sem);
        		memset(buf, 0, BUF_SIZE);
        		read(fd, buf, BUF_SIZE);
        		printf("[opponent] : %s", buf);
        		cnt++;
        		sem_post(p_sem);
        		break;
        	}
        	close(fd);	
    	}
    }
    
    printf("Done! Your Score : %d\n", score);
    
    return 0;
}
