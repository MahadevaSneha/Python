#WAP  which will select a random name from the list of names and the person selected
#person have to pay for everybody's bill
#using choice method
import random
names=(input("Enter everybody's name seperated by comma: "))
spt=names.split(",")
print(spt)
m=random.choice(spt)
print(f"{m} paying the bill.")



