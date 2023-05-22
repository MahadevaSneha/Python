'''
Input format:
Input consists of 2 integers.
The first integer corresponds to the length of the ground
The second integer corresponds to the breadth of the ground.
Output Format:
Output Consists of two integers.
The first integer corresponds to the length.
The second integer corresponds to the quantity of carpet required.
'''
leng=int(input())#20
brd=int(input())#90
l=2*(leng+brd)#220
q=leng*brd#1800
print(l)
print(q)
