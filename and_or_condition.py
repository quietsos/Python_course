
# # Conditional operator and/or

# # //and// condition is being true when both side of the condition is being true 

name = input("Enter your name:")
age = int(input("Enter your age:"))

if name == "sohan" and age == 21:
    print("Condition true.")

else:
    print("Condition false")
    

# # //or// condition is being work when one of the two condition is true or both condition is true

if name == "sohan" or age == 21:
    print("Condition true.")

else:
    print("Condition false.")
         

                EXERCISE

name = input("Enter your name: ")
age = int(input("Enter your age: "))

start_string = name[0]
print(start_string)

if (start_string == 'a' or start_string=='A') and age > 10:
    print("you can watch coco movie.")

else:
    print("you cannot watch cooc movie.")
    

# if_elif_else condition exercis.

# suppose we want to create a ticket price of a movie show according to age.bit_length

# 1 to 3 (free)
# 4 to 10 (150)
# 11 to 60 (250)
# above 60 (200)

age = int(input("Enter your age:"))

if age == 0 or age < 0:
    print("You cannot watch movie.")
elif 0<age<=3:
    print("Ticket price : Free.")
elif 4<=age<=10:
    print("Ticket price : 150")
elif 11<=age<=60:
    print("Ticket price : 250")
elif age>60:
    print("Ticket price is:200")