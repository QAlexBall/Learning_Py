#include <stdio.h>
#include <Python.h>
extern int test1;
extern void print_test();

int main() {
    print_test();
    printf("%d\n", test1);
    int const_a = 1;
    int const_b = 2;
    const int* a = &const_a;
    int* const b = &const_a;
    *b = 2;
    printf("%d\n", *a);
    printf("%d", *b);
//    Py_Initialize();
//    PyRun_SimpleString("print('hello Python!')\n");
//    Py_Finalize();
//    printf("Hello, World!\n");
    return 0;
}