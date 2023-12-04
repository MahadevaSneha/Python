#a function can return another function

def outer():
    print("outer function started")
    def inner():
        print("inner function execution")
    print("outer function returning inner function")
    return inner
f1=outer()
f1()


"""
outer function started
outer function returning inner function
inner function execution

"""
