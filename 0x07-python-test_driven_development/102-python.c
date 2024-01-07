#include <Python.h>

/**
 * print_python_string - Prints Python string information
 * @p: Pointer to a Python object (string)
 */
void print_python_string(PyObject *p)
{
Py_ssize_t length;
wchar_t *wide_str;

printf("[.] string object info\n");
if (!PyUnicode_Check(p))
{
printf("  [ERROR] Invalid String Object\n");
return;
}

length = PyUnicode_GET_LENGTH(p);
wide_str = PyUnicode_AsWideCharString(p, NULL);

printf("  type: compact unicode object\n");
printf("  length: %ld\n", length);
printf("  value: %ls\n", wide_str);

PyMem_Free(wide_str);
}
