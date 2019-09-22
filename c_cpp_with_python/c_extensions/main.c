#include <stdio.h>
#include <Python.h>

int main() {
    Py_Initialize();
    PyRun_SimpleString("print('hello Python!')\n");
    Py_Finalize();
    printf("Hello, World!\n");
    return 0;
}