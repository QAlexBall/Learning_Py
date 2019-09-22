#define PY_SSIZE_T_CLEAN
#include <Python.h>

static PyObject *
spam_system(PyObject *self, PyObject *args) {
    const char *command;
    int sys;

    if (!PyArg_ParseTuple(args, "s", &command))
        return NULL;
    sys = system(command);
    return PyLong_FromLong(sys);
}
