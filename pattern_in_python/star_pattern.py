
def pattern(n):
    k = (2 * n)-2
    for i in range(0,n):
        for j in range(0,k):
            print(end=" ")
        k = k -1
        for j in range(0,i+1):
            print("* ", end="")
        print("\r")

pattern(int(input("Enter  pyramid height:"))) 




def reverse(n): 
    k = n-2
    for i in range(n,-1,-1):
        for j in range(k,0,-1):
            print(end=" ")
        k=k+1
        for j in range(0,i+1):
            print("* ", end="")
        print("\r")

reverse(int(input("Enter reverse pyramid height:"))) 



def right_pattern(n):
    for i in range(0,n):
        for j in range(0,i+1):
            print("* ",end="")
        print("\r")
    for i in range(n,-1,-1):
        for j in range(0,i+1):
            print("* ",end="")
        print("\r")

right_pattern(int(input("Enter right_pattern pyramid height:"))) 



def left_pattern(n):
    k = 2*n -2
    for i in range(0,n-1):
        for j in range(0,k):
            print(end=" ")
        k = k-2
        for j in range(0,i+1):
            print("* ",end="")
        print("\r")
    k = k-2
    for i in range(n-1,-1,-1):
        for j in range(k,-1,-1):
            print(end=" ")
        k = k+2
        for j in range(0,i+1):
            print("* ",end="")
        print("\r")

left_pattern(int(input("Enter left_pattern pyramid height:"))) 



def boat_pattern(n):
    k = 2*n -2
    for i in range(0,n-1):
        for j in range(0,k):
            print(end=" ")
        k = k-2
        for j in range(0,i+1):
            print("* ",end="")
        print("\r")
        k = k-2
    for i in range(n-1,-1,-1):
        for j in range(k,-1,-1):
            print(end=" ")
        k = k+2
        for j in range(0,i+1):
            print("* ",end="")
        print("\r")

boat_pattern(int(input("Enter boat_pattern pyramid height:"))) 


def hour_glass_pattern(n):
    k = n-2
    for i in range(n,-1,-1):
        for j in range(k,0,-1):
            print(end=" ")
        k=k+1
        for j in range(0,i+1):
            print("* ", end="")
        print("\r")
    k = (2 * n)-2
    for i in range(0,n+1):
        for j in range(0,k):
            print(end=" ")
        k = k -1
        for j in range(0,i+1):
            print("* ", end="")
        print("\r")

hour_glass_pattern(int(input("Enter hour_glass_pattern pyramid height:"))) 



def half_pyramid(n):
    for i in range(0,n):
        for j in range(0,i+1):
            print("* ",end="")
        print("\r")

half_pyramid(int(input("Enter half_pyramid_pattern pyramid height:"))) 



def left_half(n):
    k = 2*n -2 
    for i in range(0,n):
        for j in range(0,k):
            print(end=" ")
        k = k-2
        for j in range(0,i+1):
            print("* ",end="")
        print("\r")

left_half(int(input("Enter left_half_pyramid_pattern pyramid height:"))) 



def dawnward_half_pyramid(n):
    for i in range(n,-1,-1):
        for j in range(0,i+1):
            print("* ",end="")
        print("\r")

dawnward_half_pyramid(int(input("Enter dawnward_half_pyramid_pattern pyramid height:"))) 



def diamond_pattern(n):
    k = n*2 - 2
    for i in range(0,n+1):
        for j in range(0,k):
            print(end=" ")
        k = k -1
        for j in range(0,i+1):
            print("* ", end="")
        print("\r")

    k = n-2
    
    for i in range(n,-1,-1):
        for j in range(k,0,-1):
            print(end=" ")
        k=k+1
        for j in range(0,i+1):
            print("* ", end="")
        print("\r")
    

diamond_pattern(int(input("Enter diamond_pattern pyramid height:"))) 



n = int(input("Enter n=5 for empty_diamond: "))
for i in range(n):
    for j in range(n):
        if i+j == 2 or i-j == 2 or i+j == 6 or j-i == 2:
            print("*",end="")
        else:
            print(end=" ")
    print()




print("Number as pattern: \n\n")

def number(n):
    x = 0
    for i in range(0,n):
        x += 1
        for j in range(0,i+1):
            print(x,end=" ")
        print("\r")

number(int(input("Enter number pattern length: ")))


def pascal(n):
    for i in range(0,n):
        for j in range(0,i+1):
            print(function(i,j)," ", end="")
        print()
def function(n,k):
    res =1
    if(k>n-k):
        k=n-k
    for i in range(0,k):
        res = res * (n-i)
        res = res//(i+1)
    return res

pascal(int(input("Enter the pascal number: ")))


print("Alphabet as pattern:")

def alphabet(n):
    k = n*2 -2
    x = 65
    for i in range(0,n):
        ch = chr(x)
        for j in range(0,k):
            print(end="")
        k = k-1
        x = x+1
        for j in range(0,i+1):
            print(ch,end="")
        print("\r")

alphabet(int(input("Enter the number of alphabet: ")))
