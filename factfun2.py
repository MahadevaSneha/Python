def fact(num):
    fact=1
    for i in range(1,num+1):
        fact=fact*i
        print("factorial of ",i,"is: ",fact)
fact(int(input("Enter a number to find a factorial value:")))



"""
"C:\Users\Sneha M\PycharmProjects\pythonProject\ practice\venv\Scripts\python.exe" "C:\Users\Sneha M\python_class\main.py" 
Enter a number to find a factorial value:10
factorial of  1 is:  1
factorial of  2 is:  2
factorial of  3 is:  6
factorial of  4 is:  24
factorial of  5 is:  120
factorial of  6 is:  720
factorial of  7 is:  5040
factorial of  8 is:  40320
factorial of  9 is:  362880
factorial of  10 is:  3628800

Process finished with exit code 0



"""
