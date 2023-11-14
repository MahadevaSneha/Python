def fact(num):
    fact=1
    for i in range(1,num+1):
        fact=fact*i
    return fact
res=fact(int(input("Enter a number to find factorial: ")))
print("The factorial of a given number is: ",res)


"""
Enter a number to find factorial: 5
The factorial of a given number is:  120

"""
