# An array is basically a data structure which can hold more than one value at a time.
# It is a collecction or ordered series of elements of the same type.

import array  # first method of declaring array
a = array.array('i',[1,2,3,4,5,6,7])
print(a)

# Output:
    # array('i', [1, 2, 3, 4, 5, 6, 7])

import array as arr #second method of declartion of array
a = arr.array('i',[1,2,3,4,5,6,7,8])

print(a)

# Output:
    # array('i', [1, 2, 3, 4, 5, 6, 7, 8])

from array import * # third method of declaration of array

a = array('i',[1,2,4,5,6,7,6])
print(a)

# Output:
    # array('i', [1, 2, 4, 5, 6, 7, 6])