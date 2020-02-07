
# We know in input function assign data as string thats why outuput showing like this.
# In the final print function we also cannot directly concation of int number with string that why we have to use str() function.
# number1 = input("Enter the first number:")
# number2 = input("Enter the Second number:")
# total = number1 + number2;
# print("Total is: " + total)

number1 = int(input("Enter the first number:"))
number2 = int(input("Enter the Second number:"))
total = number1 + number2;
print("Total is: " + str(total))

#  str() function change anythig to string
# 4 ---> "4"
#  int() function change anyting to integer number
# "4"----> 4
# float() function change anyting to floa t number
# "4", 4 -----> 4.00

number_1 = int(5)
number_2 = float(5)

print("Addition of int & float is:" + str(number_1 + number_2))

#we can add int and float number easily among print function without any condition.