# There are three famous buildin function in python these functions take another buildin function as their input.
# These are:
#     1. map()
#     2. filter()
#     3. reduce()

# map():
    # Applies to a given function as its arguments to all the iterables and return a new list.
    #     syntax: map(function, iterables)
# example-1:

# mylist = [1,2,3,4,5]
# def check(a):
#     return a*a
# x = map(check,mylist)
# print(x)
# print(list(x))

# example-2:
#
# print(tuple(map(lambda a:a*a,mylist)))
# print(set(map(lambda a:a*a,mylist)))

# # example-3:
# mylist1 = [1,2,3,4,5]
# mylist2 = [2,2,2,2,2]
# def check(a,b):
#     return a*b
# x = map(check,mylist1,mylist2)
# print(x)
# print(list(x))
#

# filter():
# filter() function is used to filter the given iterables(list,sets etc) with the help of another function passed as an arguments to test all the elements to be true or false

# example-1:
#
# def new(a):
#     if a>=3:
#         return a
# x = filter(new,mylist)
# print(x)
# print(list(x))

# # example-2:

# x = filter(lambda a : a>=3,mylist)
# print(x)
# print(tuple(x))


# reduce():
# reduce() function is applied some of other function to a list of element that are passed as a parameter to it and finaly return a singe value.

# example-1:

# from functools import reduce
#
# def new(a,b):
#     return a+b
# x = reduce(new,mylist)
# print(x)

# example-2:
# from  functools import reduce
# mylist = [1,2,3,4,5,6,7]
# x = reduce(lambda p,q : (p+q) , mylist)
# print(x)
#

# filter() function within map():

mylist1 = [1,2,3,4,5]
test = map(lambda a : (a+2), filter(lambda a : (a>=3),mylist1))
print(list(test))

# map() function within filter():

test = filter(lambda x : (x<=5),map(lambda x : (x+2),mylist1))
print(tuple(test))
