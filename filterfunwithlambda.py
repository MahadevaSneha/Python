#Program to filter even numbers and odd numbers from the list by using filter() function

#with using lambda function
m=[0,2,6,5,9,1,11,19,20,34]
l1=list(filter(lambda x:x%2==0,m))
l2=list(filter(lambda x:x%2!=0,m))

print(l1)
print(l2)


"""
"C:\Users\Sneha M\PycharmProjects\pythonProject\ practice\venv\Scripts\python.exe" "C:\Users\Sneha M\python_class\main.py" 
[0, 2, 6, 20, 34]
[5, 9, 1, 11, 19]

Process finished with exit code 0

"""
