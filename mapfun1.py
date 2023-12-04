#using map() for multiple lists

l1=[1,2,3,4,5]
l2=[6,7,8,9,10]
l=list(map(lambda x,y:x*y,l1,l2))
print(l)



"""
[6, 14, 24, 36, 50]
"""
