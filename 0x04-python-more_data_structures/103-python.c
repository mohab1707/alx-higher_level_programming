#include <Python.h>
#include <stdio.h>

void print_python_list(PyObject *p) {
    Py_ssize_t size, i;
    PyObject *item;

    printf("[*] Python list info\n");
    size = PyList_Size(p);
    printf("[*] Size of the Python List = %ld\n", size);
    printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);

    for (i = 0; i < size; i++) {
        item = PyList_GetItem(p, i);
        if (PyBytes_Check(item)) {
            printf("Element %ld: bytes\n", i);
            printf("[.] bytes object info\n");
            printf("  size: %ld\n", PyBytes_Size(item));

            printf("  trying string: %s\n", PyBytes_AsString(item));

            printf("  first 10 bytes: ");
            for (ssize_t j = 0; j < PyBytes_Size(item) && j < 10; j++) {
                printf("%02x ", (unsigned char)PyBytes_AsString(item)[j]);
            }
            printf("\n");
        } else if (PyTuple_Check(item)) {
            printf("Element %ld: tuple\n", i);
        } else if (PyList_Check(item)) {
            printf("Element %ld: list\n", i);
        } else if (PyFloat_Check(item)) {
            printf("Element %ld: float\n", i);
        } else if (PyLong_Check(item)) {
            printf("Element %ld: int\n", i);
        } else if (PyUnicode_Check(item)) {
            printf("Element %ld: str\n", i);
        }
    }
}

void print_python_bytes(PyObject *p) {
    Py_ssize_t size, i;

    printf("[.] bytes object info\n");

    if (!PyBytes_Check(p)) {
        printf("  [ERROR] Invalid Bytes Object\n");
        return;
    }

    size = PyBytes_Size(p);
    printf("  size: %ld\n", size);

    printf("  trying string: %s\n", PyBytes_AsString(p));

    printf("  first 10 bytes: ");
    for (i = 0; i < size && i < 10; i++) {
        printf("%02x ", (unsigned char)PyBytes_AsString(p)[i]);
    }
    printf("\n");
}
