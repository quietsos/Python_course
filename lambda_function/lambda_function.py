# lambda function:
    # Lambda function are those function whose has no name. actually it is a anonymous function:
        # Character of a lambda function:
        #     1. It is called anonymous or nameless function
        #     2. Lambda is not a name it is a keyword

    # Reason of using lambda function are below:
        # 1. One time uses:
        #     It is also known as throw away function as they are needed just once.
        # 2. Input/Output of other function:
        #     They are also passed as input or returned as output of other higer-order functions
        # 3. Reduce code size:
        #     The body of a lambda fucntion is written in a single line.


    # Writting of a lambda function:
        # A lambda fucntion is created using lambda operator:
            # Syntax:
            #     lambda arguments:expression
            #     lambda : "specify the purpose"
            #     lambda a1: "specify the purpose of a1"
            #     lambda a1..n : "specify the purpose of a1...n"

# example 1:

x=lambda a : a*a
print(x(3))


# anonymous function within user defined function:

def function1(x):
    return lambda y : x * y


t = function1(3)
print(t(3))


# Lambda function withing filter() function:
    # Used to filter() the given iterables(list,sets etc) with the help of another function passed as an arguments to test all the elemtents to tbe true or false.
        # syntax: filter(function,iterables)

mylist = [1,2,3,4,5,6,6,6,7]

newlist = list(filter((lambda a: a/3 == 2),mylist))
print(newlist)

# Output:
#     [6, 6, 6]

#Lambda function within the map() function
    # map():
        # Applies a given function to all the iterables and return a new list with boolean value for each iterables

mylist=[1,2,3,4,5,6,7,8,9]
newlist = list(map(lambda a: (a/2 != 1),mylist))
print(newlist)

# Output:
#     [True, False, True, True, True, True, True, True, True]


#lambda function within reduce function:
    # reduce():
        # applies some other function to a list of elements that are passed as a parameter to it and finally retruns a single value.

from functools import reduce

mylist = [1,2,3,4,5,6,7,8,9]

print(reduce(lambda a,b : (a+b),mylist))

x = reduce(lambda a,b : (a+b),mylist)
print(x)
