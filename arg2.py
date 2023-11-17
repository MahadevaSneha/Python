# we can mix both variable length and positional arguments

def f1(n1,*s):
    print(n1)
    for s1 in s:
        print(s1)
f1(10)
f1(10,20,30,40)
f1(10,"A",20,"B")


def f(*s,n1):
    for s1 in s:
        print(s1)
    print(n1)
f(10,20,n1="Sneha")



#keyword aqrguments

def fun(**k):
    for k,v in k.items():
        print(k,"=",v,end=" ")
fun(n1=10,n2=20)



"""
"C:\Users\Sneha M\PycharmProjects\pythonProject\ practice\venv\Scripts\python.exe" "C:\Users\Sneha M\python_class\main.py" 
10
10
20
30
40
10
A
20
B
10
20
Sneha
n1 = 10 n2 = 20 
Process finished with exit code 0


"""
