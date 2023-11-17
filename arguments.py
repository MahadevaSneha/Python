
"""Arguments in python"""
#Positional arguments

def sub(a,b):
    print(a-b)
sub(100,200)
sub(200,100)

#Keyword Arguments

def wish(name,msg):
    print("Hello",name,msg)
wish(name="sneha",msg="Gud Mrng")
wish(msg="gud Mrng",name="surya")

#Default Arguments

def wish(name="Guest"):
    print("Hello",name)
wish("Sneha")
wish()

#Variable Length Argument

def sum(*n):
    total=0
    for n1 in n:
        total=total+n1
    print("The sum is: ",total)
sum(0)
sum(10)
sum(10,20)
sum(10,100,1000,199999,309899)



"""
"C:\Users\Sneha M\PycharmProjects\pythonProject\ practice\venv\Scripts\python.exe" "C:\Users\Sneha M\python_class\main.py" 
-100
100
Hello sneha Gud Mrng
Hello surya gud Mrng
Hello Sneha
Hello Guest
The sum is:  0
The sum is:  10
The sum is:  30
The sum is:  511008

Process finished with exit code 0


"""
