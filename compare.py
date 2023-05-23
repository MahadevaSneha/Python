#Greatest of two numbers
'''
Input format: 

Input consist of 2 integers 

The first input corresponds to the first number(a) 

The second input corresponds to the second number(b) 

Output format: 

If the first number is equal to the second number, print "a is equal to b". 

Otherwise, print "a greater than b" or "a less than b"
Sample Input: 

17

12

Sample Output: 

17 greater than 12
'''
a=int(input())
b=int(input())
if a>b:
    print("{} greater than {}".format(a,b))
else:
    print("{} greater than {}".format(b,a))
