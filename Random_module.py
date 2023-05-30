#Random module in python
import random
a=random.randint(1,4)#returns int from 1 to 4
print(a)


b=random.randrange(2,10)#return int 10 is not included
print(b)

#floating point number

c=random.random()#return a floating point number from 0.0 to 1.0 
print(c)


d=random.uniform(1,3)#return floating point number between the range
print(d)

l1=[2,5,90,-5,20,32,56]
s=random.choice(l1)#print the random number from the list
print(s)

list=[2,3,4,5,6,7]
random.shuffle(list)#shuffle the list
#if you store the shuffle function in a variable then print it .it willreturn none so no neeed to store it directly shuffle it by using shuffle function
print(list)#[7, 6, 5, 2, 3, 4]
