#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/wait.h>
#include <string.h>

int main(int argc, char *argv[]){
	int pid, state;

	if( (pid = fork()) == 0 ){
		printf("I am Child : %d\n", pid);
		char * myarg[3];
		myarg[0] = strdup("/bin/ls");
		myarg[1] = NULL;
		execvp(myarg[0], myarg);
	}else if(pid < 0) {
		exit(1);
	}else{
		int ret_wait = wait(NULL);
		printf("I am Parent of %d, ret_wait : %d\n", pid, ret_wait);
	}
	return 0;
}
