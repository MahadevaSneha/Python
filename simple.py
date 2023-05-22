#simple interest problem in python
'''
The first line containing integer value denoting the borrowed amount(principal amount) 

The second line containing integer value denoting the period in years 

The third line containing float value denoting the rate of interest
'''
principal_amount=int(input())#15000
period=int(input())#2
rate_of_interest=float(input())#2.8
simple_interest=float((principal_amount*period*rate_of_interest)/100)
print('{:.2f}'.format(simple_interest))#840.00
