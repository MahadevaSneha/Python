#working with class and its description

class Student:
    """This is student class with required data"""
print(Student.__doc__)
help(Student)


"""
This is student class with required data
Help on class Student in module __main__:

class Student(builtins.object)
 |  This is student class with required data
 |  
 |  Data descriptors defined here:
 |  
 |  __dict__
 |      dictionary for instance variables (if defined)
 |  
 |  __weakref__
 |      list of weak references to the object (if defined)


"""
