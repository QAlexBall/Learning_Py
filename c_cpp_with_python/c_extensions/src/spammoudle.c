/*
 * Created by QAlexBall on 2019/9/22.
 *
 * C extend example
 * create spam module for python
 * create_function => define_method_table => inference_by_PyModuleDef => PyInit_module => main_to_AppendInittab
 */

#define PY_SIZE_T_CLEAN
#include <Python.h>


static PyObject* spam_system(PyObject* self, PyObject* args) {
    const char* command;
    int sts;

    if (!PyArg_ParseTuple(args, "s", &command))
        return NULL;
    sts = system(command);
    return PyLong_FromLong(sts);
}


/*
 * method table
 * 为了展示spam_system()如何被Python程序调用。把函数声明为可以被Python调用，需要定义一个方法表"method table"
 */
static PyMethodDef SpamMethods[] = {
    {"system", spam_system, METH_VARARGS,
     "Execute a shell command." },
    {NULL, NULL, 0, NULL}   /* Sentinel */
};


/*
 * 这个方法表必须被模块定义结构所引用
 */
static struct PyModuleDef spammodule = {
    PyModuleDef_HEAD_INIT,
    "spam", /* name of module */
    "spam_doc", /* module documentation, may be NULL */
    -1, /* size of per-interpreter state of module, or -1 if module keeps state in global variables. */
    SpamMethods
};


/*
 * 这个结构体必须传递给解释器的模块初始化函数。初始化函数必须命名为PyInit_name()，
 * 其中那么是模块的名字，并应该并应该定义为非static，且在模块文件里
 */
PyMODINIT_FUNC PyInit_spam(void) { /* PyMODINIT_FUNC声明了函数作为PyObject* 的返回类型,声明任何平台的连接声明， 以及给C++声明函数的extern "C" */
    return PyModule_Create(&spammodule);
}


/*
 * 要添加模块到初始化表,使用PyImport_AppendInittab(),可选的跟着也给模块的导入
 */
int main(int argc, char *argv[]) {
    wchar_t *program = Py_DecodeLocale(argv[0], NULL);
    if (program == NULL) {
        fprintf(stderr, "Fatal error: cannot decode argv[0]\n");
        exit(1);
    }
    /* Add a built-in module, before Py_Initialize */
    PyImport_AppendInittab("spam", PyInit_spam);
    /* Pass argv[0] to Python interpreter */
    Py_Initialize();
    /* Optionally Import the module; alternatively,
     * import can be deferred until the embedded script
     * imports it. */
    PyImport_ImportModule("spam");
    // ...
    PyMem_RawFree(program);
    return 0;
}