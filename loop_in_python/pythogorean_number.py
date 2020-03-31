num = int(input("Enter the range: "))

for i in range(1,num+1):
    for j in range(1,num+1):
        for k in range(1,num+1):
            if (i*i + j*j) == k*k:
                print(i,j,k)
            else:
                continue


from math import sqrt
n = int(input("Enter maximum number: "))

for a in range(1,n+1):
    for b in range(a,n):
        c_square = a**2 + b**2
        c = int(sqrt(c_square))
        if(c_square - c**2)==0:
            print(a,b,c)

# Nested while for loop:
travelling = input("yes or no: ")
if travelling == "no":
    print("Thanks for your kind information.")

while travelling == "yes":
    num = int(input("Number of people travelling: "))
    for num in range(1,num+1):
        name = input("Enter name: ")
        age = input("Enter age: ")
        sex = input("Enter male/female: ")
        print(name)
        print(age)
        print(sex)
    travelling = input("Oops! forget someone: ")
    if travelling == 'no':
        print("Thank you..")