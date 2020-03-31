print('Welcome to ATM')
restart=('y')
chances = 3
balance = 100

while chances >= 0:
    pin = input('Please enter your 4 digit pin: ')
    if pin == ('1234'):
        print('You entered your pin correctly\n')
        while restart not in ('n'):
            print('Please press 1 for your balance\n')
            print('Please press 2 to make a withdraw\n')
            print('Please press 3 to pay in\n')
            print('Please press 4 to return card\n')

            option = int(input('What would you like to choose: '))

            if option == 1:
                print('Your balance is: ',balance,'$','\n')
                restart = input('Would you like to go back: ')
                if restart in ('n'):
                    print('Thank you\n')
                    break

            elif option == 2:
                withdrwal = float(input("How much do you want to withdraw: "))
                if withdrwal > balance:
                    print("Invalid Amount, Please Re-try.\n")
                    restart= ('y')
                elif withdrwal not in [20,50,80,100]:
                    print("Please enter desired ammount.\n")
                    restart = ('y')


                elif withdrwal in [20,50,80,100]:
                    balance = balance - withdrwal
                    print("Your balance is now: ", balance,"$",'\n')
                    restart=input(("Would you like to go back: "))
                    if restart in ('n'):
                        print("Thank you\n")
                        break

            elif option == 3:
                pay_in = float(input("How much would you like to pay In: "))
                balance = balance + pay_in
                print("Your balance is now: ",balance,"$",'\n')
                restart = input("Would you like to go back: ")
                if restart in ('n'):
                    print("Thank you\n")
                    break


            elif option == 4:
                print("Please wati while your card is Returned....\n")
                print('Thank you')
                break
            else:
                print("Please enter a correct number.\n")
                restart = ('y') 

    elif pin != ('1234'):
        print('Incorrect Password\n')
        chances = chances - 1
        if chances == 0:
            print("No more tries..\n")
            break        


