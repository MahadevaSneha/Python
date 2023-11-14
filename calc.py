#returning multiple values from a function
def sum_sub(x,y):
    sum=x+y
    sub=x-y
    mul=x*y
    div=x/y
    return sum,sub,mul,div
res=sum_sub(int(input("Enter fst num: ")),int(input("Enter scn number: ")))
for x in res:
    print(x)





"""
"C:\Users\Sneha M\PycharmProjects\pythonProject\ practice\venv\Scripts\python.exe" "C:\Users\Sneha M\python_class\main.py" 
Enter fst num: 10
Enter scn number: 5
15
5
50
2.0

Process finished with exit code 0
"""
