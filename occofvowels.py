#write a program to find no.of occurencees of each vowel present in the given string
w=input("Enter a string:")
a={"a","e","i","o","u"}
d={}
for x in w:
    if x in a:
        d[x]=d.get(x,0)+1
for k,v in sorted(d.items()):
    print(k,"occured in",v,"times")

"""
Enter a string:sneha
a occured in 1 times
e occured in 1 times

"""
