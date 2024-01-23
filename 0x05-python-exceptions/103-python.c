#include <Python.h>

/**
 * print_python_list - Prints information about Python lists
 * @p: PyObject (Python list)
 */
void print_python_list(PyObject *p)
{
	Py_ssize_t size, i;
	PyObject *item;

	printf("[*] Python list info\n");
	size = PyList_Size(p);
	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);

	for (i = 0; i < size; i++)
	{
		item = PyList_GetItem(p, i);
		printf("Element %ld: %s\n", i, Py_TYPE(item)->tp_name);
		if (PyBytes_Check(item))
			print_python_bytes(item);
		else if (PyList_Check(item))
			print_python_list(item);
		else if (PyFloat_Check(item))
			print_python_float(item);
	}
}

/**
 * print_python_bytes - Prints information about Python bytes
 * @p: PyObject (Python bytes)
 */
void print_python_bytes(PyObject *p)
{
	Py_ssize_t size, i;
	char *str;

	printf("[.] bytes object info\n");
	if (!PyBytes_Check(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	size = PyBytes_Size(p);
	printf("  size: %ld\n", size);
	printf("  trying string: %s\n", PyBytes_AsString(p));

	printf("  first %ld bytes: ", size + 1 > 10 ? 10 : size + 1);
	str = PyBytes_AsString(p);
	for (i = 0; i < size + 1 && i < 10; i++)
		printf("%02x%c", str[i] & 0xff, i + 1 == 10 && size + 1 > 10 ? ' ' : '\n');
}

/**
 * print_python_float - Prints information about Python float
 * @p: PyObject (Python float)
 */
void print_python_float(PyObject *p)
{
	PyObject *repr;
	double value;

	printf("[.] float object info\n");
	if (!PyFloat_Check(p))
	{
		printf("  [ERROR] Invalid Float Object\n");
		return;
	}

	value = ((PyFloatObject *)p)->ob_fval;
	printf("  value: %.*g\n", 17, value);

	repr = PyObject_Repr(p);
	printf("%s\n", PyUnicode_AsUTF8(repr));
	Py_XDECREF(repr);
}
