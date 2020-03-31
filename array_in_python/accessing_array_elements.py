# Accessing array elements

import array as arr

a = arr.array('i',[1,2,3,4,5,6,6,7])
print(a)

print(a[3])

# Note:
    # array is a mutable collection of data here we can access the data and can manipulate it as well 

# There are various array operations:
#     1. Finding array length
#     2. Adding/changing elements of array
#     3. Removing/Deleting elements of array
#     4. Array concatenation
#     5. Slicing
#     6. Looping through an array

 
# 2. Adding an elements in an array we used three funcction as well.
    # 1. append() - adding a single elements at the end of array
    # 2. extend() - adding two or more elements at the end of array
    # 3. insert() - adding an elements in a specific position in an array


import array as arr 

a = arr.array('i',[1,2,3,4,5,6,7])

a.append(9)
print(a)

a.extend([6,6,6])
print(a)

a.insert(2,10)
print(a)

# 3. Removing elements from an array
    #  1.pop()- used to remove an elements and return it.
    #  2. remove()- used to remvoe an elements and dont return iter

import array as arr

a = arr.array('d',[1.1,1.5,1.6])
print(a)

a.pop() # remove last elements of the array
print(a) 

a.pop(1) # remove the define index elements from array
print(a)

a.remove(1.1)  # remove the exact given element from the array
print(a)


# 4. Array contatenation:
    # array concatenation means joining two or more arrays.

import array as arr

a = arr.array("d",[1,2,4,5])
b = arr.array("d",[8,9,3,4])
c = arr.array("d") #empty array
c = a+b
print(c)

# 5. Slicing of an array:
    # Slicing an array means slicing some particular values from an arrays
    # An array can be sliced using the ":" symbole. This returns a range of elements that we have specified by the index numnbers.

import array as arr
a = arr.array('i',[1,2,3,4,5,6,7])
a = a[2:4] # it will slicing the array from index number 2 to 3(not included)
print(a)

# 6. Looping through an array:

import array as arr

a = arr.array("i",[1,2,3,4,5,6,7,8])
print("Using for loop:")
for x in a:
    print(x)

# Output:
# Using for loop:
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8

print("Using while loop:")
temp = 0
while temp<len(a):
    print(a[temp])
    temp=temp+1

# Output:
# Using while loop:
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8