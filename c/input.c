#include <stdio.h>

void stop() {
    int ch;
    while ((ch = getchar()) != '\n' && ch != EOF);
}

int main () {
    int i = 0;
    char c;
    char hello_world[] = "hello, world";
    int len = sizeof(hello_world) - 1;
    while ((c = getchar()) != EOF) {
        if (c == hello_world[i]) {
            i++;
            if (i == len) {
                printf("\nhello, world\n");
                break;
            }
        }
        else {
            printf("\n%s\n", "please type 'hello, world'");
            i = 0;
            stop();
        }
    }
}
