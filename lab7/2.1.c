#include <stdio.h>
#include <unistd.h>

int main() {
    int pid = fork();
    
    if (pid == 0) {
        printf("Это сообщение из дочернего процесса\n"
               "Родительский PID: %d\n"
               "Дочерний PID: %d\n", getppid(), getpid());
    }
    
    return 0;
}