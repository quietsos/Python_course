# Loop:
    # loop are allows to execution of a statement or a group of statement multiple times.

# Loop are two kinds:
    # 1. Infinite loop 
    # 2. Finite loop

# Python allow three kinds of loop:
    # 1. while loop 
    # 2. for loop 
    # 3. nested loop

# while loop:
    # while loops are known as indefinite or conditional loops. They will keep iterating untill certain condition are met. there is no gurantee ahed of time regarding how many times the loop will iterate.
    #    Syntax:
    #     while expession:
    #         statements

print("While loop test:")
count = 0
while count<9:
    print("Number:",count)
    count += 1
print("Good bye.")


print("Guessing game:")
win = 13
while 1:
    num = int(input("Input number:"))
    if(num == win):
        print("congratulation. You made it!")
        break
    if(num > 13):
        print("Number is too large")
    if(num < 13):
        print("Number is too small")


import random
n = 20
to_be_guessed = int(n * random.random())+1
guess = 0
while guess != to_be_guessed:
    guess = int(input("New number: "))
    if guess > 0:
        if guess > to_be_guessed:
            print("Number too large")
        elif guess < to_be_guessed:
            print("Number too small")
    else:
        print("Sorry that you're giving up!")
else:
    print("Congratuation. You made it!")


# For loop:
    # For loop is a python loop which repeats a group of statements  a specified number of times. The for loop provides a syntax where the following information is provided
    #  1. Boolean condition
    #  2. The inital value of the counting variable
#     #  3. Incrementation of counting variable 

fruits = ['mango','banana','apple','orange']

for fruit in fruits:
    print('Current fruit: ',fruit)

print('Good bye')

print("Factorial using while and for loop:")

while 1:
    num = int(input("Enter number: "))

    factorial = 1

    if num < 0:
        print("must be positive.")
        continue
    elif num == 0:
        print("factorial = 1")
        continue
    if num > 0:
        for i in range(1, num+1):
            factorial = factorial*i
    print("factorial = ",factorial)

#Nested loop:
    # python programming language allows use of the loop inside another loop. This is called nested loop.
