#write a program to accept student name and marks from the keyboard and creates a dict .also display student marks by taking student name as input
n=int(input("Enter how many students: "))
d={}
for x in range(n):
    name=input("Enter student name: ")
    marks=input("Enter student marks: ")
    d[name]=marks
while True:
    name=input("Enter Student name to get marks:")
    marks=d.get(name,-1)
    if marks==-1:
        print("student is not found")
    else:
        print("The marks of",name,"is",marks)
    option=input("Do you want to know more student details(Yes/No): ")
    if option=="No":
        break
print("Thanks for using this application")



"""


Enter how many students: 3
Enter student name: sneha
Enter student marks: 89
Enter student name: surya
Enter student marks: 90
Enter student name: chok
Enter student marks: 78
Enter Student name to get marks:sneha
The marks of sneha is 89
Do you want to know more student details(Yes/No): Yes
Enter Student name to get marks:surya
The marks of surya is 90
Do you want to know more student details(Yes/No): No
Thanks for using this application


"""
