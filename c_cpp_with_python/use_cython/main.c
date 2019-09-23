#include <Python.h>
#include "src/cpython_module/get_index.h"
int main() {
    PyObject* array;
    array = (PyObject *) {(PyObject *) 1};
    PyObject* str_exc_type = PyObject_Repr(array);
    PyObject* pyStr = PyUnicode_AsEncodedString(str_exc_type, "utf-8", "Error ~");
    const char* strExcType = PyBytes_AsString(pyStr);
    printf("%s\n", strExcType);
    return 0;
}