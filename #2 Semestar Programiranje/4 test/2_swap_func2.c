#include <stdio.h>

void swap(int *pa, int *pb) {
    int t = *pa;
    *pa = *pb;
    *pb = t;
    return;
}

int main(void) {
    int a = 221;
    int b = 127;
    swap(&a, &b);
    printf("main: a = %d, b = %d\n", a, b);
    return 0;
}