
# len() function is used for counting the length of the string

name = "ShOhAn"

length = len(name)
print(f"length is: {length}")

# lower() method is used for converting all the character of the string in small letter

print(f"Lower case: {name.lower()}")

# upper() method is used for converting all the character of the string in capital letter

print(f"Upper case: {name.upper()}")

# tittle() method is used for converting only the first letter of a string in capital letter

print(f"Title form is: {name.title()}")

# count() function is used for counting the number of same type of letter presents in the string

print(name.count("h")) 

            #EXERCISE

name, letter = input("Enter the name and letter:").split()
length = len(name)
counter = name.count(letter)
print(f"Length is: {length} \nCounter is: {counter}")