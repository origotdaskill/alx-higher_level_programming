#include <Python.h>
#include <stdio.h>

/**
 * print_python_list_info - prints information about a Python list
 * @p: pointer to a Python object (list)
 *
 * Description:
 * This function prints the size of the Python list, the allocated space,
 * and the type of each element in the list.
 */
void print_python_list_info(PyObject *p)
{
    Py_ssize_t size, i;
    PyObject *item;

    /* Get the size of the list */
    size = PyList_Size(p);
    printf("[*] Size of the Python List = %ld\n", size);

    /* Get the allocated space */
    printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);

    /* Iterate through the list and print element types */
    for (i = 0; i < size; i++)
    {
        item = PyList_GetItem(p, i);
        printf("Element %ld: %s\n", i, Py_TYPE(item)->tp_name);
    }
}

