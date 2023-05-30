#Love calculator
name1=input("Enter Your Name: ")
name2=input("Enter Your Crush Name: ")
combine_name=name1+name2
lower_case_name=combine_name.lower();

t=lower_case_name.count('t')
r=lower_case_name.count('v')
u=lower_case_name.count('u')
e=lower_case_name.count('e')
true=t+r+u+e
l=lower_case_name.count('l')
o=lower_case_name.count('o')
v=lower_case_name.count('v')
e=lower_case_name.count('e')
love=l+o+v+e
love_score=int(str(true)+str(love))

if love_score<10:
    print(f"Your Love Score is {love_score}")
elif love_score>=10 and love_score<=50:
    print(f"Your Love Score is {love_score}")
else:
    print(f"Your Love Score is {love_score}")
                  
                  

