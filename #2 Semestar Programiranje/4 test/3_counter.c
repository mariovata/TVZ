#include "stdio.h"
#include "stdbool.h"

void increment(void) {
    static unsigned int counter = 0; //If we remove static we output 1 1 1 1 1 because the counter rests
    counter++;
    printf("%d ", counter);
}
int main(void) {
    for (int i = 0; i < 5; i++) {
        increment();
    }
    _Bool flag1 = 0;
    bool flag2 = false; // Needs #include "stdbool.h" and is preferred
    short man = 5; // can be also short int man = 5;

// enum types

    enum day { sun, mon, tue, wed, thu, fri, sat };
    enum cardinal_points { north = 0, east = 90, south = 180, west = 270 };
    enum months { jan = 1, feb, mar, apr, may, jun, jul, aug, sep, oct, nov, dec };
    printf("\nMay is the %d'th month \n",may);

// Function Types
    int f(void);
    int *fip();
    void g(int i, int j);
    void h(int, int);
//    First, we declare a function f with no parameters that returns an int.
//    Next, we declare a function fip with no specified parameters that returns a
//    pointer to an int. Finally, we declare two functions, g and h, each returning
//    void and taking two parameters of type int.

// Pointers

    int i = 17;
    int *pointer_i = &i; // & Means address-of
    pointer_i = &*pointer_i;

    printf("Random address in memory:  %d\n",pointer_i);

//    Arrays

    char str[11];
    for (unsigned int xa = 0; i < 10; ++i) {
        str[xa] = '0' + xa;

    }
    str[10] = '\0';
//    Declared an array of char with a bound of 11. This allocates
//    sufficient storage to create a string with 10 characters plus a null character.
//    The for loop iterates 10 times, with the values of i ranging from 0 to 9. Each
//    iteration assigns the result of the expression '0' + i to str[i]. Following
//    the end of the loop, the null character is copied to the final element of the
//    array str[10].
    return 0;
}