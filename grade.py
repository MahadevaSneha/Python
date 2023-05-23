#Grading System
'''
The newly appointed Vice Chancellor of Anna University wanted to create a automated grading system for the students to check their grade. When a student enter a mark, the grading system displays the corresponding grade.

Write a program to solve the given problem.

 

Marks scored

Grade

100

S

(90,100)

A

(80,90)

B

(70,80)

C

(60,70)

D

(50,60)

E

<50

F
 
The interval [a,b) includes all numbers greater than or equal to a and less than b.

 Input and Output Format:

Input consists of a single integer which corresponds to the marks scored by the student. Print Invalid Input if it is not in the range 0 to 100.

Refer sample input and output for formatting specifications.

Sample Input 1:

85

Sample Output 1:

B

Sample Input 2:

850

Sample Output 2

Invalid Input
'''
a=int(input())
if a==100:
    print("S")
elif a>=90 and a<100:
    print("A")
elif a>=80 and a<90:
    print("B")
elif a>=70 and a<80:
    print("C")
elif a>=60 and a<70:
    print("D")
elif a>=50 and a<60:
    print("E")
elif a<50:
    print("F")
else:
    print("Invalid Input")
    
