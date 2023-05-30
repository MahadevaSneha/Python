#WAP  which will select a random name from the list of names and the person selected
#person have to pay for everybody's bill
#using choice method
import random
names=(input("Enter everybody's name seperated by comma: "))
spt=names.split(",")
print(spt)
length=len(spt)
m=random.randint(0,length-1)#we have calucate the length of the list
print(f"{spt[m]} will pay the bill.")



