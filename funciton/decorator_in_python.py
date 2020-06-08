# Decorator:
#     Decorators in python are very powerful which modify
#     the behaviour of a fucntion without modifying try
#     permananatly. It basiccally wraps another function and since botha functons are callable
#     it returns a callable.



def function1(function):
    def wrapper():
        print("hay, it works")
    return wrapper

@function1

def function2():
    print("sohan")

function2()




def function1(function):
    def wrapper():
        print("hello")
        function()
        print("Welcome to my home.")
    return wrapper

def function2(): 
    print("friends")

function2 = function1(function2)

@function1
def function2():
    print("friends")
function2() th arguments:

def function1(function):
    def wrapper(*args, **kwargs):
        print("hello")
        function(*args, **kwargs)
        print("welcome to python")
    return wrapper

@function1

def function2(name):
    print(f"{name}")

function2("sohan")

def function1(function):
    def wrapper(*args, **sohan):
        print("hay, it works")
    return wrapper

@function1

@function1


#Fancy decorators in python:
    #fancy decorators in python is complex types of decorators
    # There are three types of fancy decorators in python:
        # 1. Class decorators
        # 2. Stateful decorators
        # 3. Class as decorators


# 1. Class decorators:

class Square:
    def __init__(self,side):
        self._side = side
    @property
    def side(self):
        return self._side
    @side.setter
    def side(self,value):
        if value >= 0:
            self._side = value

@function1
        else:
            print("error")
    @property
    def area(self):
        return self._side ** 2
    
    @classmethod
    def unit_square(cls):
        return cls(1)
s = Square(5)
print(s.side)
print(s.area)


# There also have some other decorators in python:
#     1. singleton class
#     2. arguments in a Decorators
#     3. Nesting decorators
#     4. validiting JSON


# 1. singleton class using class decorators:

import functools
def singleton(cls):
    @functools.wraps(cls)
    def wrapper(*args,**kwargs):
        if not wrapper.instance:
            wrapper.instance = cls(*args,**kwargs)
        return wrapper.instance
    wrapper.instance = None
    return wrapper

@singleton
class one:
    pass
first = one()
second = one()

print(first is second)




import functools

def repeat(num):
    def decorator_repeat(function):
        @functools.wraps(function)
        def wrapper(*args,**kwargs):
            for _ in range(num):
                Value = function(*args,**kwargs)
            return Value
        return wrapper
    return decorator_repeat


@repeat(num = 5)

def function(name):
    print(f"{name}")

function("sohan")
