#Fee Collection
'''
Write a program to determine the fee amount to be collected from a student. The input to the program are the type of the student, tuition fee, bus fee, hostel fee.

Refer the table below for fee details.

Student Type

Student Type denoted as

Fee Details

Merit Seat Day Scholar

MSDS

Tuition fee + Bus fee

Merit Seat Hosteller

MSH

Tuition fee + Hostel fee

Management Seat Day Scholar

MGSDS

150% of Tuition fee + Bus fee

Management Seat Hosteller

MGSH

150% of Tuition fee + Hostel fee

 

Input and Output Format:

Input consists of a string (student type), tuition fee (float), bus fee (float) and hostel fee (float). All floating point numbers are displayed correct to 2 decimal places.

Refer sample input and output for formatting specifications.

All text in bold corresponds to input and the rest corresponds to output.

Sample Input and Output:

Enter the student type

MSH

Enter tuition fee

40000

Enter hostel fee

50000

The fees to be paid by the student is Rs.90000.00

'''
print("Enter the student type")
st=input()
if st=="MSH":
    print("Enter tuition fee")
    tf=int(input())
    print("Enter hostel fee")
    hf=int(input())
    print("the fees to be paid by the student is Rs.{:.2f}".format(tf+hf))
        
elif st=="MSDS":
    print("Enter tuition fee")
    tf1=int(input())
    print("Enter Bus fee")
    bf=int(input())
    print("the fee to be paid by the student is Rs.{:.2f}".format(tf1+bf))
elif st=="MGSDS":
    print("Enter tution fee")
    tf2=int(input())
    x=(150*tf2)/100
    print("enter bus fee")
    bf1=int(input())
    print("the fee to be paid by the student is Rs.{:.2f}".format(x+bf1))
elif st=="MGSH":
    print("Enter tution fee")
    tf3=int(input())
    x1=(150*tf3)/100
    print("enter hostel fee")
    hf1=int(input())
    print("the fee to be paid by the student is Rs.{:.2f}".format(x1+hf1))
else:
    print("Inavalid Student type")






