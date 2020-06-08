# OOP refers to object oriented programming.
# Though python is not a fully object oriented programming language but it support OOP concept as well
# class and object are the main theme of OOP concept:

# class:
#     *A class is a logical grouping which helps us to reuse and rebuild data as well.
#     *It also called a blueprint from which specific object are created.

# class has three basic variables:
    # 1. class variables: A variable which is shared by all instances of a class.
    # 2. Insatnce variables: Instance variable is unique to each instance.
    # 3. Data member: A class variables or instances variable that holds data associated with a class and objects.

# syntax:
#             class class_name():
#                 statement-1
#                 .......
#                 .......
#                 .......
#                 statement-n

# Example-1:

class data():
    pass

first = data()
second = data()

first.name = "Sohan"
first.ssc = 2015
first.roll = 108988
first.village = "Hazratpara"

second.name = "Ashik"
second.ssc = 2015
second.roll = 108989
second.village = "Hazratpara"

print(first.name)


# Example-2: Python class object using constructor:

class data():
    def __init__(self,Name,ssc,village,amount):
        self.Name = Name
        self.ssc = ssc
        self.village = village
        self.amount = amount

    def amount_inc(self):              # for updating any information within constructor by using user define function
        self.amount = (self.amount*5)

first = data("sohan",2015,"Hazratpara",1000)
second = data("Sojib",2025,"Khejurotola",1000)
first.salary = 15000 # for adding more information in any of the constructor in python
print(first.__dict__)

print(first.amount)
first.amount_inc()
print(first.amount)