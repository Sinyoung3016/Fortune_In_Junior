#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/wait.h>
#include <string.h>
#include <fcntl.h>

int main(int argc, char *argv[]){
	int pid, state;

	if( (pid = fork()) == 0 ){
		printf("pwd I am Child\n");
		close(STDOUT_FILENO);
		open("./p4.output",O_CREAT|O_WRONLY|O_TRUNC, S_IRWXU);
		char * myarg[2];
		myarg[0] = strdup("pwd");
		myarg[1] = NULL;
		execvp(myarg[0], myarg);
	}else if(pid < 0) {
		exit(1);
		printf("jot");
	}else{	
		wait(NULL);
		printf("ls I am Parent of %d\n", pid);
		close(STDOUT_FILENO);
		open("./p4.output",O_CREAT|O_WRONLY|O_TRUNC, S_IRWXU);
		char * myarg[2];
		myarg[0] = strdup("ls");
		myarg[1] = NULL;
		execvp(myarg[0], myarg);
	}
	return 0;
}


