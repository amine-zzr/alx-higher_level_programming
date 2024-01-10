#include <Python.h>

/**
 * print_python_list_info - Prints basic information about Python lists.
 * @p: A pointer to a PyObject representing a Python list.
 */

void print_python_list_info(PyObject *p)
{
	PyListObject *list = (PyListObject *)p;

	printf("[*] Size of the Python List = %ld\n", Py_SIZE(list));
	printf("[*] Allocated = %ld\n", list->allocated);

	for (Py_ssize_t i = 0; i < Py_SIZE(list); ++i)
		printf("Element %ld: %s\n", i, Py_TYPE(PyList_GetItem(p, i))->tp_name);
}
