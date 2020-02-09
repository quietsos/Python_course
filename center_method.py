# Center() method is used for adding 
# same things both side same number's

name,content,total =input("Enter name and adding element: ").split(",") 
# **Shohan** if we want something like this then execuite the below code
leng= len(name)
length = leng + int(total)

print(name.center(length,content))