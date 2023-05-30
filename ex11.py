#pizza order program
size=input("What size pizza you want(S/M/L) ? ")
bill=0
if size =='S' or size=='s':
    bill=bill+100
    print("Small pizza price is Rs.100")
elif size =='M' or size=='m':
    bill=bill+200
    print("Medium pizza price is Rs.200")
else:
    bill=bill3+00
    print("Medium pizza price is Rs.300")
add_pepperoni=input("Do you want pepperoni(Y/N)? ")
if add_pepperoni=='Y' or add_pepperoni=='y':
    if size=='S' or size=='s':
        bill=bill+30
    else:
        bill=bill+50
extra_cheese=input("Do you want extra cheese(Y/N)? ")
if extra_cheese=='Y' or extra_cheese=='y':
    bill=bill+20
print(f"The total bill is Rs.{bill}")
