#nested functions in python

def outer():
    print("Hello ,How are you???")
    def inner():
        print("I'm fine,what about you???")
    inner()
outer()


"""
Hello ,How are you???
I'm fine,what about you???

Process finished with exit code 0

"""
