name = "Shohan"
age = 21


#Conventional way of string formatting in python language
print("Hello " +name +" "+ "your age is: "+ str(age))

#String formatting way in python 3 using .format() function.

print("Hello {} your age is: {}".format(name,age))


#String formatting way in python 3.6 using (f) outer start of "" in print function

print(f"Hello {name} your age is {age}")

#we also can calcultion within this { } parenthesis

print(f"Hello {name} your age is {age+5}")