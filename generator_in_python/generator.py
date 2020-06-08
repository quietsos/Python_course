# Generator function in python:
#     1. Basically a function that return traversal objects.
#     2. Produce items one at a time and only when required.
#     3. Run along with for loops.

# Advantage:
#     1. Easy to implementation.
#         ( implement_iter_() , _next()_automatically)
#     2. Better memory managements and utilization.
#     3. Can be used to produce infinite items
#     4. Can also be used to pipeline a number of operation.

# Difference between general function and generator function:

#     Generator                                     Normal function
# 1. make use of 'yield' keyword              1. make use of 'return' keyword
# 2. Run when next() method is called         2. Run when name of the method is called
# 3. Produce items one at  a time and only    3. Produce all the items at once.
#    when required.


# Writting generator in python:
#     1. Generators created using the 'def' keyword
#     2. Make use of the 'yield' keyword instead of 'return'
#
# syntax:
#         def func(a):
#             yield a
#         a = [1,2,3,4,5]
#
#         b = func(a)
#         next(b)

# Example-1:
#
# def new(dict):
#     for x,y in dict.items():
#         yield x,y
#
# a={1:"hi",2:"Welcome"}
# b=new(a)
# print(b)
# print(next(b))
# print(next(b))

# Example -2:

# def myfunc(i):
#     while i<=5:
#         yield i
#         i+=1
# j = myfunc(2)
# print(next(j))
# print(next(j))
# print(next(j))
# print(next(j))
# print(next(j)) it will show stop iteration because the condition already fillup for the previous fucntion

# Example-3:

# def ex():
#     n = 4
#     yield n
#     n = n**n
#     yield n
#
# x = ex()
# print(next(x))
# print(next(x))

# Example-4:
# Generator using for loops.

# def gen():
#     i = 5
#     yield i
#     i = i**i
#     yield i
#
# k = gen()
#
# for x in k:
#     print(x)

# Generator expression:
#     generator expression are used to creates annoynimous generator function.

# Example:

# f = range(6)
# print("List comp: ",end=":")
# q = [x+1 for x in f]
# print(q)
# r = (x+1 for x in f)
# print(r)

# for i in r:
#     print(i)

# print(min(r))


# Fibbonacci number generation using generator:

# def fib():
#     f,s=0,1
#     while True:
#         yield f
#         f,s=s,f+s
#
# for x in fib():
#     if x>50:
#         break
#     print(x, end=" ")

