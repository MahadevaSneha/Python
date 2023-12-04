#function aliasing in python

def wish(name):
    print("Hello",name,"Good morning")
greeting=wish#function aliasing
print(id(wish))
print(id(greeting))

wish("sneha")
greeting("surya")


"""
2676055228080
2676055228080
Hello sneha Good morning
Hello surya Good morning

Process finished with exit code 0

"""
