# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and 
n=int(input())
for i in range(1,n+1):
    for j in range(1,n+1):
        if(i==1 or i==n or j==1 or j==n or  n+1-i==j):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
