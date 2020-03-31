# defaultdict is a dictionary subclass which calls a factory function to supply missing values.

from collections import defaultdict

d = defaultdict(int)
d[1] = "shohan"
d[2] = "python"

print(d)

# Output:
    # defaultdict(<class 'int'>, {1: 'shohan', 2: 'python'})