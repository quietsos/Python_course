# deque pronounced as deck is an optimised list to perform insertion and deletion easily.
from collections import deque

a =['s','h','o','h','a','n']
b = deque(a)
b.append('uzzaman') #append function is used for adding element in any collection
b.appendleft('md')
print(b)
b.popleft() #pop() function is used for deleting element from collection and it also donot allow any argument inside it.
b.pop()
print(b)