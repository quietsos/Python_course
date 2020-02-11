# //in// is a character that is used to find out a specific character from a string.

# syntax - 'x' in 'string'

name = input("Enter a name:")
char = input("Enter a character:")

if char in name:
    print("Character is present.")

else:
    print("Character is absent.")
