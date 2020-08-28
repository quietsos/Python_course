# # while loop is a looping style that used to do same types of works repeatadly

i = 1
while  i<= 10:
    print(f"ICT {i}")
    i=i+1


            EXERCISE
# sum : 1 to 10 (or a given ranges)

i = int(input("Enter the first number: "))
j = int(input("Enter the last number: "))
sum = 0

while i<=j:
    sum = sum + i
    i = i+1

print(f"The summesion is: {sum}")


#             #EXERCIS

number = input("Enter a number: ")

total = 0
length = len(number)
i = 0
while i<length:
    total = total + int(number[i])
    i = i+1

print(f"The result is: {total}")


            #EXERCISEJ

name = input("Enter your name:")

length = len(name)
i = 0
temp_var = ""
while i<length:
    if name[i] not in temp_var:
        temp_var += name[i]
        print(f"# : {name[i]} : {name.count(name[i])}")
    i = i +1
 


 #infinite looping 

# while True:
#     print("This is an infinite loop")


# for loop is another looping style for repeatead same type things 

for i in range(10):    # range function define the ranges of the looping.
    print(f"This is for loop. : {i}" )


for i in range(1,10):   #Here we used two variable in the range function for starting and ending of the loop
    print(f"This is for loop. : {i}")


                #EXAMPLE OF SUM USING FOR LOOP           
sum = 0
for i in range(1,10):   #Here we used two variable in the range function for starting and ending of the loop
    print(f"This is for loop. : {i}")
    sum += i

print(sum)

#This a loop introduction.
