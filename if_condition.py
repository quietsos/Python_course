# #syntax
# # if condition
# #    if condition is true then program will execuite


# age = input("Enter your age:")
# age = int(age)

# if age > 10:
#     print("Your are not a child.")
#     print("You are doing good")


# if age >= 10:
#     print("Your are not a child")
#     print("You have finished 2nd program")


# if age == 0:
#     pass

# else:
#     print("You are a child")


                #EXERCISE

winning_number = int(input("Enter the winning number: "))
guess_number = int(input("Enter the guess number:"))

if winning_number == guess_number:
    print("YOU WIN !!!")

else:
    if winning_number > guess_number:
        print("too low")
    
    else:
        print("too high")


        
        