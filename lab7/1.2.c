#include <stdio.h>

extern char **environ;

int main(int argc, char *argv[]) {
    int num = 0;
    char **p;
    
    for (p = environ; *p != NULL; p++) {
        num++;
    }
    
   printf("Number of environment variables: %d\nNumber of arguments: %d\n", num, argc); // printenv | wc -l
    
    return 0;
}