'''
           Lab Allocation

There are 3 labs in the CSE department (L1, L2 and L3) with a seating capacity of x, y and z. find the lab which has the minimal seating capacity. 

Input and Output Format:

Assume that x, y and z are always distinct.

Refer sample input and output. 

Note:

All text in bold corresponds to input and the rest corresponds to output.

Sample Input and Output 1:

Enter x

30

Enter y

40

Enter z

20

L3 has the minimal seating capacity

'''

print("Enter x")
x=int(input())
print("Enter y")
y=int(input())
print("Enter z")
z=int(input())
if x<y and x<z:
    print("L1 has the minimal seating capacity")
elif y<z:
    print("L2 has the minimal seating capacity")
else:
    print("L3 has the minimal seating capacity")
           
