#Write a program to find factorial of given number with recursion

def fact(num):
    if num==0:
        return 1
    return num*fact(num-1)
res=fact(int(input("Enter a number: ")))
print("The Factorial of a given number is:",res)


"""
"C:\Users\Sneha M\PycharmProjects\pythonProject\ practice\venv\Scripts\python.exe" "C:\Users\Sneha M\python_class\main.py" 
Enter a number: 2
The Factorial of a given number is: 2

Process finished with exit code 0

"""
