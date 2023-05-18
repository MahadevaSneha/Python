#AVERAGE OF GIVEN STUDENTS
total=int(input())
n=0
for i in range(total):
    #m = float(input(f"Enter the score for student {i+1}: "))
    m=float(input())
    n=n+m
avg=n/total
print("{:.2f}".format(avg))#30.00


    
