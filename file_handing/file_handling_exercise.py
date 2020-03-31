# Reading method in python for file handling.



# example 1:

# import os
# file = open("/home/quiet/Desktop/python/file_handing/file_handling_exercise.txt", "w")
# file.close()

#example 2: reading document text file using python code.

# import os
# file = open("/home/quiet/Desktop/python/file_handing/file_handling_exercise.txt", 'r')
# print(file.read())
# file.close()

# example 3: Readding the exact number of string using the python code of any text file

# import os
# file = open("/home/quiet/Desktop/python/file_handing/file_handling_exercise.txt", 'r')
# print(file.read(5))
# file.close()

# exercise 5: read all the line on a text file using python code.

# import os
# file = open("/home/quiet/Desktop/python/file_handing/file_handling_exercise.txt", 'r')
# print(file.readlines())
# file.close()

# exercise 6: read all the line on a text file using for loop python code 

# import os
# file = open("/home/quiet/Desktop/python/file_handing/file_handling_exercise.txt", 'r')
# for line in file:
#     print(file.readlines())
# file.close()


# Writting method in a text file using python:

    # There are exist two way of writting text in any file in python:
    #     1. "a" = append mode that will write in the last line given content.
    #     2. "w" = write mode will erase entire line and stublish new given line in the text file
    

# exercis 1: checking that existing file is really writeable or not 
# import os
# file = open("/home/quiet/Desktop/python/file_handing/file_handling_exercise.txt", 'w')
# print(file.writable())
# file.close()

# exercise 2: writting text on a text file using python 
# import os
# file = open("/home/quiet/Desktop/python/file_handing/file_handling_exercise.txt", 'w')
# file.write("Hello world!\n")
# file.write("love for python!")
# file.close()

#exercise 3: checking is "w" working on python

# import os
# file = open("/home/quiet/Desktop/python/file_handing/file_handling_exercise.txt", 'w')
# file.write("Oops overwritting!\n")
# file.close()

#exercise 4: checking "a" mode is working on python

# import os
# file = open("/home/quiet/Desktop/python/file_handing/file_handling_exercise.txt", 'a')
# file.write("append is working.\n")
# file.close()



# Creating file using pyton:
    # "x" mode is used for creating file.

# import os
# file = open("/home/quiet/Desktop/python/file_handing/new_file.txt", 'x')
# file.write("New file is created.\n")
# file.close()

# Deleting file using python:

    # syntax: os.remove() function is used to remove or delete function in python 


# exercise 1:

# import os
# os.remove("/home/quiet/Desktop/python/file_handing/delete_file.txt")

# exercise 2:

import os
if os."/home/quiet/Desktop/python/file_handing".exists("delete_file.txt"):
    os.remove("delete_file.txt")
else:
    print("File does not exist")
