#map() function
#without lambda function

l=[1,2,3,4,5]
def func(x):
    return 2*x
l1=list(map(func,l))
print(l1)


#with lamda fun

l=[10,20,30,40,50]
l1=list(map(lambda x:2*x,l))
print(l1)
