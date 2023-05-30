#Multiple if statements in python
height=int(input("What is your height in feet? "))
if height>=3:
    print("You can ride")
    age=int(input("What is your age? "))
    if age<12:
        bill=150
        print("Ticket Price is Rs.150")
    elif age>=12 and age<=18:
        bill=250
        print("Ticket Price is Rs.250")
    else:
        bill=500
        print("Ticket Price is Rs.500")
    want_photo=input("Do you want to take photo(Y/N)?")
    if want_photo == 'y' or want_photo=='Y':
        bill=bill+50
    print(f"Your total bill is Rs.{bill}")
else:
    print("You cannot ride")
print("Bye")
