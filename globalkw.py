#global Keyword


#Without global variable
a=10
def f1():
    a=7
    print(a)
def f2():
    print(a)
f1()
f2()



#With global Variable

a=7
def f1():
    global a
    a=10
    print(a)
def f2():
    print(a)
f1()
f2()




#Without initial a value
def f1():
    global a
    a=10
    print(a)
def f2():
    print(a)
f1()
f2()


#We can access the global variable inside another function through global() function

b=100
def f1():
    a=777
    print(a)
    print(globals()['b'])
f1()



"""
"C:\Users\Sneha M\PycharmProjects\pythonProject\ practice\venv\Scripts\python.exe" "C:\Users\Sneha M\python_class\main.py" 
7
10
10
10
10
10
777
100

Process finished with exit code 0



"""
