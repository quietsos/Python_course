# Dictionary is one kind of list but it is little different from list
# Charactertistics of dictionary:
#     1. Unordered
#     2. can be change
#     3. No duplication allow
#     4. We need to declare key value for each variables in dictionary

# Syntax: name = { key : values }

dictionary = { 1: 'Shohan',
                2: 'soib',
                'third': 'sumon' }

print(dictionary)

# access value form dictionary using key value

print(dictionary[2])
print(dictionary.get(1))

# update a value using a key value of a dictionary 

dictionary[2] = "shohan"
print(dictionary)

# adding value in a dictionary using key value 

dictionary[4] = 'adding'
print(dictionary)