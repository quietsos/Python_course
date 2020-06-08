# function as class:

# def func1(name):
#     return f"Hello,{name}"

# def func2(name):
#     return f"{name}, how are you?"

# def func3(func4):
#     return func4("Dear learner")

# print(func3(func1))
# print(func3(func2))


# function in function or nested funciton in python:

# def func():
#     print("Mother function.")
#     def func1():
#         print("first child function.")
#     def func2():
#         print("Second child function.")
#     func1()
#     func2()

# func()


# def func(n):
#     print("Mother function")

#     def func1():
#         return "First child function."
#     def func2():
#         return "Second child function."
#     if n == 1:
#         return func1
#     else:
#         return func2

# a = func(int(input("Enter 1 or 2: ")))
# print(a())