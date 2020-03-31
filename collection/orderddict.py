# OrderedDict is a dictionary subclass which remembers the order in which the entires were done
from collections import OrderedDict

o = OrderedDict()

o[1] = 's'
o[2] = 'h'
o[3] = 'o'
o[4] = 'h'
o[5] = 'a'
o[6] = 'n'

print(o)

# Output:
    # OrderedDict([(1, 's'), (2, 'h'), (3, 'o'), (4, 'h'), (5, 'a'), (6, 'n')])    

print(o.keys())
# Output:
#     odict_keys([1, 2, 3, 4, 5, 6])

o[1] = 'md'

print(o)

# Output:
    # OrderedDict([(1, 'md'), (2, 'h'), (3, 'o'), (4, 'h'), (5, 'a'), (6, 'n')])