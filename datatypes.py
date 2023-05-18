#datatypes in python
#integer
var_1=2210
print(var_1)#2210
print(var_1+20)#2230
print(type(var_1))#int
#binary
n=0b10
print(n)#2
m=0B10
print(m)#2
#octal
a=0o123
print(a)#83
b=0O123
print(a)#83
#hexa
c=0x123
print(c)#291
d=0X123
print(d)#291


#float
var2=22.10
var3=123
print(var2+var3)#145.1
print(type(var2))#float


#string
name="sneha"
print(name)#sneha
print(type(name))#str
print(name[0])#print s means first index value
print(name[2])#prints second index value
name1="sneha"
name2="mahadeva"
print(name1+name2)#snehamahadeva
x="123"#consider as string not an int
y="1"
print(x+y)#1231
print("sneha's notebook")#sneha's notebook
print("sneha\'s \"notebook\"")#sneha's "notebook"
print("sneha\'s\n\"notebook\"")#sneha's "notebook"(in next line)
print("sneha\'s\\n\"notebook\"")#sneha's\n"notebook"
print(5*"cute")#cutecutecutecutecute

#boolean
var=True
print(var)#True
print(type(var))#bool
#var=true --->name error:true is not defined
i=1
j=2
varr=i>j
print(var)#True
print(type(var))#bool
