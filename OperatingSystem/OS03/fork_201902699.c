#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>


int a = 2;
int main(int argc, char *argv[]){
	int b = 5;
	int pid;
	printf("orgin : a = %d, b = %d\n", a, b);

	if( (pid = fork()) == 0 ){
		printf("child : ++a = %d, ++b = %d\n", ++a, ++b);
		exit(0);
	}
	else if (pid < 0) 
		exit(1);
       	else
		printf("parent : --a = %d, --b = %d\n", --a, --b);

	return 0;
}	



