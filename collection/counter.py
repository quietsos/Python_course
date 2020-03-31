# Counter is a dictionary subclass for counting hashable objects.
    #we can easily count the repateaded value number in a list using the count.

from collections import Counter


a = [1,2,1,2,1,2,3,4,5,6,7,2,1,2]
count = Counter(a)
print(count)

# Output:
#     Counter({2: 5, 1: 4, 3: 1, 4: 1, 5: 1, 6: 1, 7: 1})

# we also can perform element function for showing all the repaeated element inline using counter.

print(list(count.elements()))

# Output:
#     [1, 1, 1, 1, 2, 2, 2, 2, 2, 3, 4, 5, 6, 7]


# most_common() fucntion will show the sorting value in a list with it's repeated times.

print(count.most_common())

# Output:
#     [(2, 5), (1, 4), (3, 1), (4, 1), (5, 1), (6, 1), (7, 1)]