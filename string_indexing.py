
# Indexing refers to select a particular world from a word.
#Position always start from 0 as array count position

name = "Shohan"

print(name[1]) # here within print function variable name then square bracket [] for inseting the positon where we want to find the letter

print(name[-1]) # We use - symbole within [ ] for counting position from bottom


    # String slicing or selecting subsequence

#  syntax = [start argument : stop argument]

print(name[0:5])
print(name[-3:-1])

print(name[ : ]) # when we donot enter argument then full string will print

print(name[2: ]) # when we use only start position then it will print from start position to end of string

print(name[ : 3]) # when we use only stop string position then it will start from beginning of string and stop at the end position

print("Shohan" [2 : 5]) # We can insert string within print funciton  and use start:stop argument simultaniously

# Step argument 

# syntax - [start argument : stop argument : Step]
# Here step is the value of interval of printing first letter before printing the second letter

print("University" [ 0 : 5 : 2]) # here 2 in step position the interval of a world for printing the second word

# reverse printing a string using step arguments

print("Shohan" [5 : : -1])
print("Shohan" [-1 : : -1])



            # EXERCIS
# Get an input from user and print it in reverse order

name = input("Your name: ")
print(f"Reverse string is:{name[-1 : : -1]}")



