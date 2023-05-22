#Sheela has three things in her bag. She wants to compute the area of 3 things but 3 things are in different shapes. The three things are in square shape, rectangular shape, and circular shape respectively.
#Write a program to help Sheela to calculate the area of different shapes.
side=int(input())#5
length=int(input())#5
breadth=int(input())#4
radius=float(input())#2.0
area_of_square=side*side
area_of_rectangle=length*breadth
area_of_circle=3.14*(radius**2)
print(area_of_square)#25
print(area_of_rectangle)#2.0
print('{:.2f}'.format(area_of_circle))#12.56
