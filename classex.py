#write a program to create a student class and create an object to it .call the method talk() to display student details

class Student:
    """Student details"""
    def __init__(self,name,age,marks):
        self.name=name
        self.age=age
        self.marks=marks
    def talk(self):
        print("Hello I'm ",self.name)
        print("My age is ",self.age)
        print("My marks are ",self.marks)
s=Student("Sneha",20,60)
print(Student.__doc__)
s.talk()


"""

Student details
Hello I'm  Sneha
My age is  20
My marks are  60
"""
