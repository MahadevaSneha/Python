#returning multiple values from a function
def sum_sub(x,y):
    sum=x+y
    sub=x-y
    return sum,sub
res1,res2=sum_sub(int(input("Enter fst num: ")),int(input("Enter scn number: ")))
print("The Sum is: ",res1)
print("The Sub is: ",res2)

"""
Enter fst num: 100
Enter scn number: 50
The Sum is:  150
The Sub is:  50

"""
