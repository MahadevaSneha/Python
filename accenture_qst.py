def amount_of_food(r,unit,n,arr):
    if arr is None or n==0:
        return -1
    food=r*unit
    new,c=0,0
    for i in range(n):
        if new<food:
            new+=arr[i]
            c+=1
        else:
            break
    if new>=food:
        return c
    else:
        return 0
r=int(input())
unit=int(input())
n=int(input())
arr=list(map(int,input().split()))
print(amount_of_food(r,unit,n,arr))

"""
7
2
0
0
-1


7 
2 
8
2 8 3 5 7 4 1 2
4

"""
