#Identity operator----- is and is not
a=5
b=5
print(id(a))
print(id(b))
print(a is b)#true
print(a is not b)#false
c=5
d='5'
print(id(c))
print(id(d))
print(a is b)#false
print(a is not b)#true
a=6
print(id(a))
print(a is a)#true
