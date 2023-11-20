#Program to filter only even numbers from the llist by using filter() function

#without using lambda function

def isEven(l):
    if l%2==0:
        return True
    else:
        return False
m=[0,2,6,5,9,1,11,19,20,34]
l1=list(filter(isEven,m))
print(l1)


"""
"C:\Users\Sneha M\PycharmProjects\pythonProject\ practice\venv\Scripts\python.exe" "C:\Users\Sneha M\python_class\main.py" 
[0, 2, 6, 20, 34]

Process finished with exit code 0

"""
