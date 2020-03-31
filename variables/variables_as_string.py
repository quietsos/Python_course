# String is also one of the 6 datatype in python that are very important part of learning python
# We can define stirng in two ways:
    # 1. x = 'shohan' // within a single cottetion
    # 2. x = "shohan" // within a double cottetion

x = 'Shohan'
y = "Shohan"

print(x)
print(y)

# when we get input from a user uing an input function that time it takes input a form of String

z = input()
print(z)


#we can also print all the variables in one single line code:

print("Variables are:",x,y,z)

#string length 

length = len(z)
print(length)

#index number in string is define the each position value of stirng in the total string
#string index start from the 0 to the last

print(z[2])

# Note: we cannot replace one single string from a string

#we can make a string in a form of upperccase and lowercase using string operation
 
print(z.lower())
print(z.upper())

#we also can controle our string length from indexing the string

print(z[3:7])