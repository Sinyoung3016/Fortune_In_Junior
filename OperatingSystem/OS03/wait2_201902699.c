#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/wait.h>

int main(int argc, char *argv[]){
	int pid, state;

	if( (pid = fork()) == 0 ){
		printf("Hi\n");
		exit(0);
	}else if(pid < 0){
		exit(1);
	}else{
		sleep(1);
		printf("Bye\n");
	}
	return 0;
}

