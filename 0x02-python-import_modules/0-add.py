#!/usr/bin/python3
from add_0 import add

a = 1
b = 2
add_0 = __import__('0-add').add
print("{} + {} = {}".format(a, b, add_0(a, b)))
