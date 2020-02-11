
# # Conditional operator and/or

# # //and// condition is being true when both side of the condition is being true 

# name = input("Enter your name:")
# age = int(input("Enter your age:"))

# if name == "sohan" and age == 21:
#     print("Condition true.")

# else:
#     print("Condition false")
    

# # //or// condition is being work when one of the two condition is true or both condition is true

# if name == "sohan" or age == 21:
#     print("Condition true.")

# else:
#     print("Condition false.")
         

                #EXERCISE

name = input("Enter your name: ")
age = int(input("Enter your age: "))

start_string = name[0]
print(start_string)

if (start_string == 'a' or start_string=='A') and age > 10:
    print("you can watch coco movie.")

else:
    print("you cannot watch cooc movie.")
    
