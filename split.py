'''
Input consists of 2 integers. 

The first integer corresponds to the number of students in the class 

The second integer corresponds to the number of teams.
'''
stu=int(input())#60
teams=int(input())#8
pt=int(stu/teams)#7
lf=int(stu%teams)#4
print("The number of students in each team is {} and left out is {}".format(pt,lf))
