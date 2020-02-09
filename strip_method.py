

# strip() method is used for erasing the space before and after of a string

name = "     sohan    "
dots = "......."

# Without stripping the name and dots addition is as like below result

print(name + dots)

# lstrip() used for erase the left side space of any string
print(name.lstrip() + dots)


# rstrip() used for erase the right side space of any string

print(name.rstrip() + dots)

# strip() only strip function is used for erashing the both left and right side sapce of a string

print(name.strip() + dots)

# replace() function is used for erase space among a full string

nam = "So h a n"

print(nam.replace(" ", ""))

# replace() method using we can replace space of a sentence with other symoble

string = "Information and Communication Engineering"

print(string.replace(" ","_"))

# find() method is used to find any string position

print(string.find("and"))
