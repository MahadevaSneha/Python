#calculating body mass index BMI
#formula for calculating BMI is
#weight/(height*height)
weight=int(input("Enter your weight in kgs: "))
height=float(input("Enter your height in inches: "))
BMI=weight/(height**2)
print(BMI)
