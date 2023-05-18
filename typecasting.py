#type casting,type conversion,type checking,type error
print(len("sneha manahadeva"))#16-->return length of the string
#print(len(12345))  --> TypeError: object of type 'int' has no len()
print(len("12345"))#5
length=len("snehasurya")
#print("your name has "+length+" characters")
#TypeError: can only concatenate str (not "int") to str
print("your name has "+str(length)+" characters")#your name has 10 characters
print(type(length))#int
new_length=str(length)#converted int into string
print(type(new_length))#int

print(10+10)#20
print("10"+"10")#1010
print(int("10")+int("10"))#20
print(float(20))#20.0
#print(10+int("name"))--->ValueError: invalid literal for int() with base 10: 'name'

name="123"
print(10+int(name))#133
