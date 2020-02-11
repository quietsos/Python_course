  
  # Number guessing game in python

winning_number = 43
guess = 1

number = int(input("Guess a number between 1 and 100 : "))
game_over = False

while not game_over:
    if number == winning_number:
        print("YOU WIN !!!")
        print(f"your guess this number {guess} times")
        game_over = True

    else:
        if number < winning_number:
            print("too low")
            guess += 1
            number = int(input("Guess again : "))
        else:
            print("too high")
            guess += 1
            number = int(input("Guess again : "))


# DRY -  Dont repeat yourself principle is said donot repeat same code several times 



winning_number = 43
guess = 1

number = int(input("Guess a number between 1 and 100 : "))
game_over = False

while not game_over:
    if number == winning_number:
        print("YOU WIN !!!")
        print(f"your guess this number {guess} times")
        game_over = True

    else:
        if number < winning_number:
            print("too low")
            
        else:
            print("too high")


        guess += 1
        number = int(input("Guess again : "))
     

     #Random number is python using random module

import random
winning_number = random.randint(1,100)
guess = 1

number = int(input("Guess a number between 1 and 100 : "))
game_over = False

while not game_over:
    if number == winning_number:
        print("YOU WIN !!!")
        print(f"your guess this number {guess} times")
        game_over = True

    else:
        if number < winning_number:
            print("too low")
            
        else:
            print("too high")


        guess += 1
        number = int(input("Guess again : "))
     
