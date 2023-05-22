'''
INPUT FORMAT: 

Input consists of 6 integers. 

The first integer corresponds to x1. 

The second integer corresponds to y1. 

The third and fourth integers correspond to x2 and y2 respectively. 

The fifth and sixth integers correspond to x3 and y3 respectively. 

OUTPUT FORMAT: 

The output consists of two floating point numbers (with one decimal place) which correspond to the location of the house.
'''
x1=int(input())#2
y1=int(input())#4
x2=int(input())#10
y2=int(input())#15
x3=int(input())#5
y3=int(input())#8
md1=((x1+x2+x3)/3)#5.7
md2=((y1+y2+y3)/3)#9.0
print('{:.1f}'.format(md1))
print('{:.1f}'.format(md2))
