#include <Python.h>
#include <stdio.h>

/**
 * print_python_list - prints basic info about Python lists
 * @p: Python object (PyListObject *)
 */
void print_python_list(PyObject *p)
{
    PyListObject *list = (PyListObject *)p;
    Py_ssize_t i, size;

    printf("[*] Python list info\n");
    printf("[*] Size of the Python List = %ld\n", Py_SIZE(p));
    printf("[*] Allocated = %ld\n", list->allocated);

    for (i = 0, size = Py_SIZE(p); i < size; ++i)
    {
        printf("Element %ld: %s\n", i, Py_TYPE(PyList_GetItem(p, i))->tp_name);
        if (strcmp(Py_TYPE(PyList_GetItem(p, i))->tp_name, "bytes") == 0)
            print_python_bytes(PyList_GetItem(p, i));
    }
}

/**
 * print_python_bytes - prints basic info about Python bytes
 * @p: Python object (PyBytesObject *)
 */
void print_python_bytes(PyObject *p)
{
    PyBytesObject *bytes = (PyBytesObject *)p;
    Py_ssize_t i, size, max_bytes;

    printf("[.] bytes object info\n");

    if (!PyBytes_Check(p))
    {
        printf("  [ERROR] Invalid Bytes Object\n");
        return;
    }

    size = PyBytes_Size(p);
    printf("  size: %ld\n", size);
    printf("  trying string: %s\n", PyBytes_AS_STRING(p));

    max_bytes = (size < 10) ? size : 10;
    printf("  first %ld bytes: ", max_bytes);
    for (i = 0; i < max_bytes; ++i)
        printf("%02x ", (unsigned char)bytes->ob_sval[i]);
    printf("\n");
}

/**
 * print_python_float - prints basic info about Python float
 * @p: Python object (PyFloatObject *)
 */
void print_python_float(PyObject *p)
{
    PyFloatObject *f = (PyFloatObject *)p;

    printf("[.] float object info\n");

    if (!PyFloat_Check(p))
    {
        printf("  [ERROR] Invalid Float Object\n");
        return;
    }

    printf("  value: %f\n", f->ob_fval);
}
