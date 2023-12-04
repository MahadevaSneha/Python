#reduce() function in python

from functools import *
l=[10,20,30,40,50]
l1=reduce(lambda x,y:x+y,l)
print(l1)



"""
150

"""
