from ctypes import *

# load the shared object file
adder = CDLL('./adder.so')

# Find sum of integers
res_int = adder.add_int(3, 5)
print("Sum of 3 and 5 = ", str(res_int))

#Find sum of float
a = c_float(5.5)
b = c_float(3.1)

add_float = adder.add_float
add_float.restype = c_float
print("Sum of 5.5 and 4.1 = ", str(add_float(a, b)))

