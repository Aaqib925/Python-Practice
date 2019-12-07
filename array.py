# the library of array can be imported as import array
# if you want to add whole array module use this
# array is homogeneous...which mean an array can contain up to same element's data type...it can either be integer
# float or anything else
# for integer use int and for floating point number use float keyword
from array import *
my_array = array("I", [1, 2, 3])  # i means signed...and capital I means only unsigned integer
print(my_array)
print(my_array.buffer_info())   # this will print the address of the array and the size of the array




