"""
Input Format

The first line contains the number of students who have subscribed to the English newspaper.
The second line contains the space separated list of student roll numbers who have subscribed to the English newspaper.
The third line contains the number of students who have subscribed to the French newspaper.
The fourth line contains the space separated list of student roll numbers who have subscribed to the French newspaper.

Constraints


Output Format

Output total number of students who have subscriptions to the English or the French newspaper but not both.

Sample Input

9
1 2 3 4 5 6 7 8 9
9
10 1 2 3 11 21 55 6 8
Sample Output

8
Explanation

The roll numbers of students who have subscriptions to English or French newspapers but not both are:
 and .
Hence, the total is  students.
"""

# Enter your code here. Read input from STDIN. Print output to STDOUT

n=int(input())
s1=set(input().split())
m=int(input())
s2=set(input().split())
s3=s1 ^ s2
count=0
for x in s3:
    count=count+1
print(count)

