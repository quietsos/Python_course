# Chainmap is a dictionary like class for creating a single view of mutiple mappings.

from collections import ChainMap

a = {1:'Md', 2: 'Shohan'}
b = {3: 'uz', 4: 'zamman'}

c = ChainMap(a,b)
print(c)