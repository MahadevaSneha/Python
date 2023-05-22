'''
INPUT FORMAT:
Input consists of 2 integers.
The first integer corresponds to the number of students in the class
The second integer corresponds to the number of teams.

OUTPUT FORMAT:
The output consists of two integers.
The first integer corresponds to the number of students in each team
The second integer corresponds to the students who are left out.
'''
stu=int(input())#60
teams=int(input())#8
pt=int(stu/teams)#7
lf=int(stu%teams)#4
print(pt)
print(lf)

