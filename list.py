#list in python
# list is nothing but collection of elements which is enclosed by [] anad seperated by ' , '

roll_no=[1,2,3,4,5]
print(roll_no)
names=["sneha","vani","reshma"]
print(names)
mixed_list=[1,"sneha",False,10.10]#if you want find max and min ,it is not possible in mixed_list
print(mixed_list)


print(roll_no[3])#4
'''print(roll_no[10])'''#gives index error
print(len(roll_no))#5 return length of the string
'''negative index'''
print(roll_no[-2])#4

''' List slicing '''
print(roll_no[0:])#[1, 2, 3, 4, 5]
print(roll_no[0:5])#[1, 2, 3, 4, 5]
print(roll_no[1:3])#[2,3]
print(roll_no[1:4])#[2, 3, 4]
print(roll_no[::])#[1, 2, 3, 4, 5]
print(roll_no[:5])#[1, 2, 3, 4, 5]
print(roll_no[0:3:1])#[1, 2, 3]
print(roll_no[0:5:2])#[1,3,5]----extended slicing



numbers=[22,10,5,24,23]
print(numbers)#[22,10,5,24,23]
numbers.sort()
print(numbers)#[5, 10, 22, 23, 24]
numbers.reverse()#Which reverse the function
print(numbers)#[24, 23, 22, 10, 5]
print(max(numbers))#24
print(min(numbers))#5
numbers.append(54)#append which is used add element at end of the list
print(numbers)#[24, 23, 22, 10, 5, 54]
numbers.insert(2,55)#we can add element at index number using insert function--at atime only one item is aadded
print(numbers)#[24, 23, 55, 22, 10, 5, 54]
numbers.extend([45,25,60,77])
print(numbers)#[24, 23, 55, 22, 10, 5, 54, 45, 25, 60, 77]

numbers[1]=2210
print(numbers)#[24, 2210, 55, 22, 10, 5, 54, 45, 25, 60, 77]

numbers[1:4]=[23,24,25]
print(numbers)#[24, 23, 24, 25, 10, 5, 54, 45, 25, 60, 77]
numbers.remove(24)
print(numbers)#[ 23, 24, 10, 5, 54, 45, 25, 60, 77]
numbers.pop()
print(numbers)#[23, 24, 25, 10, 5, 54, 45, 25, 60]
print(numbers.pop())#return the popped element
numbers.pop(1)
print(numbers)#[23, 25, 10, 5, 54, 45, 25]
print(numbers.count(23))#1
print(numbers.copy())#[23, 25, 10, 5, 54, 45, 25]

print(numbers.clear())#None











