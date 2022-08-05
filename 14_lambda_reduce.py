#lambda that returns products of elements of a list
from functools import *
lst = [1, 2, 3, 4, 5,8,7]
# r = reduce(lambda x,y:x, lst)
# p = reduce(lambda x, y:y, lst)
w = reduce(lambda x, y:x+y, lst)
c = reduce(lambda x, y:x-y, lst)
# print(r)
# print(p)
print(w)
print(c)