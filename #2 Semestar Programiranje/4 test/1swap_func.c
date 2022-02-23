#include <stdio.h>

void swap(int, int);

int main(void) {
    int a = 221;
    int b = 127;
    swap(a, b);
    printf("main: a = %d, b = %d\n", a, b);
    return 0;
}

void swap(int a, int b) {
    int t = a;
    a = b;
    b = t;
    printf("swap: a = %d, b = %d\n", a, b);
}
