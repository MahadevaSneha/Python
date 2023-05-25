#f_strings in python
name="sneha"
age=30
height=1.6
#normal concatenation and type casting
print("My name is:"+name,"I am " +str(age),"years old","My height is ",height,"meters")
print("My name is:",name,"I am " ,+age,"years old")
print(f"My name is {name},I am {age} ,My height is {height} metres")#f_strings
print(f"sneha's father is {age*2} year old.")
print("My name is {} ,My age is {},My height is {}".format(name,age,height))
