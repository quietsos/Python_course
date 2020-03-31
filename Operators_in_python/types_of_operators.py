# There are seven operators in python:
    # 1. Arithmetic
    # 2. Assignment
    # 3. comparision
    # 4. Logical
    # 5. Membership
    # 6. identity
    # 7. Bitwise

# 1. Arithmetic operators:
    # Arithmectic operators are used to perform arithmetic operations between variables.

    #There are seven arithmectic operators in python:
        # 1. Addition(+)
        # 2. Substraction(-)
        # 3. Multiplication(*)
        # 4. Divition(/)
        # 5. Modulas(%)
        # 6. Exponentional(**)
        # 7. Floor Divition(//)

x =10
y =20

print(x+y)
print(x-y)
print(x*y)
print(x/y)
print(x%y)
print(x**y)
print(x//y) 

# Assignment Operators:
    # Assignment operators are used to assign values.
    # Operators: Example:
    # 1. =   :     x =  10
    # 2. +=  :     x += 10
    # 3. -=  :     x -= 10
    # 4. *=  :     x *= 10
    # 5. %=  :     x %= 10
    # 6. //= :     x //=10
    # 7. |=  :     x |= 10
    # 8. ^=  :     x ^= 10
    # 9. &=  :     x &= 10

a = 5
print(a)
a += 5
print(a)
a -= 5
print(a)
a *= 5
print(a)
a = 7
a %= 5
print(a)
a **= 5
print(a) 
a //= 5
print(a)
a |= 5
print(a)
a ^= 5
print(a)
a &= 5
print(a)

# 3. Comparision Operator:
    # Comprasion operators are used to compare two values
        #     1. Equal                    : (==)
        #     2. Notequal                 : (!=)
        #     3. Greather than            : (>)
        #     4. Less than                : (<)
        #     5. Greather than or equal   : (>=)
        #     6. Less than or equal       : (<=)

x = 10
y = 20

compare = (x == y)
print(compare)
compare = (x > y)
print(compare)
compare = (x < y)
print(compare)
compare = (x != y)
print(compare)
compare = (x <= y)
print(compare)
compare = (x >= y)
print(compare)

# conditional Operators:
    # conditional operators are used to combine conditional statements
        # There are three conditional statements in python:
            # 1. if
            # 2. elif 
            # 3. else

if x == y:
    print("Equal")
elif x > y:
    print("Greather")
elif x < y:
    print("Smaller")
elif x >= y:
    print("Greather than equal")
elif x <= y:
    print("Less than equal")
else:
    print("Not equal")
    
print("Not there")

#4. Logical operator:
    #Logical operators are used to combine conditional statements:
        #1. Logical and 
        #2. Logical or
        #3. Logical not

#5. Identity operators:
    # Identity operators are used to compare objects:
    # There are two identity operators in python:
        # 1. is ( return true if both variable are same object)
        # 2. is not (return true if both variables are not same object)

list1 = [1,2,3]
list2 = [1,2,3]
x = list1
print(x is list1)
list1 = list2
print(x is list2)
print(x is not list2)

#6. Membership operators:
    # Membership operators are used to chek if a sequence is presents in an object. 
     #There are two Membership operators in python:
        #1. in (return true if a sequence with the specific value is present int the object )
        #2. not in (return true if a sequence with the specific value is not presnt in the object)

print("Membership check:")
list1 = [1,2,3,'sohan']
list2 = [1,2,3]
print(2 in list1)
print(3 not in list2)
print('sohan' in list1) 

#7. Bitwise operators:
    # Bitwise oprators are used to compare binary numbers.
       #There are six bitwise operator in python
          # 1.Bitwise AND(&) (sets each bit to 1 if both bits is 1)
          # 2.Bitwise OR (|) (Sets each bit to 1 if one of the bits is 1)
          # 3.Bitwise XOR (Sets each bit to 1 if only one of the bits is 1)
          # 4.Bitwise NOT(!) (Inverts all bit)
          # 5.Bitwise Left Shift (<<) (Shift left by pushing in zeroes from the right and let the leftmost bits fell off)
          # 6.Bitwise Right shif (>>) (Shift right by pushing copies of the leftmost bit in from the left and let the rightmost bit fall off )
print("Bitwise operator:")
x = 10 # 1010
y = 12 # 1100
print(x & y) # 1010 & 1100 = 1000
print(x | y) # 1010 | 1100 = 1110
print(20 >> 2) # 10101 >> 2 (here the right side two bit will vanish and the result will be the left remain bit )  
print(20 << 2) # 10101 << 2 (here two bit will add as zero in the right side of the number)
