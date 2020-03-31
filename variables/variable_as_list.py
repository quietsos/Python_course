# List is a collection of array that is changeable and ordered and can be modified
# charactertistics of list:
#     1. ordered
#     2. Can be changed
#     3. Duplicate/ manipulate perform
#     4. We can store in list all types of varibles such as: numbers, strings etc in same list

# syntax: list = [ values]

list =[1,5,6,'shohan','sojib']
print(list)

#we can access any of the value under the list using the index number as well in string

print(list[2:4])

# we can update a value in the list by indexing

list[2]='update'
print(list)

# we can add value in the end of a list using .append() function

list.append("adding")
print(list)

#We can inset a value in any of the position of the list using .insert() funciton

list.insert(2,"insert")
print(list)

#we can write our list reverse using the reverse function as well

list.reverse()
print(list)