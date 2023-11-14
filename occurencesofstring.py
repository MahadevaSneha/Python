w=input("Enter a string:")
d={}
for x in w:
    d[x]=d.get(x,0)+1
for k,v in d.items():
    print(k,"occured in",v,"times")

"""
Enter a string:snehasurya
s occured in 2 times
n occured in 1 times
e occured in 1 times
h occured in 1 times
a occured in 2 times
u occured in 1 times
r occured in 1 times
y occured in 1 times
"""
