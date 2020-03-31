# from collections import namedtuple

# a =  namedtuple('courses','name,technology')
# s = a('Python', 'language')

# print(s)

# namedtuple() returns a tuple with a named value from the each element of the tuple.  

from collections import namedtuple

a = namedtuple('courses', 'name,technology')
s = a._make(['sohan','sojib'])
print(s)

# We also can include a nametuple in list declaration using namedtuple() funciton
