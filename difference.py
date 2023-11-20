"""
Input Format

The first line contains the number of students who have subscribed to the English newspaper.
The second line contains the space separated list of student roll numbers who have subscribed to the English newspaper.
The third line contains the number of students who have subscribed to the French newspaper.
The fourth line contains the space separated list of student roll numbers who have subscribed to the French newspaper.

Constraints


Output Format

Output the total number of students who are subscribed to the English newspaper only.

Sample Input

9
1 2 3 4 5 6 7 8 9
9
10 1 2 3 11 21 55 6 8
Sample Output

4
Explanation

The roll numbers of students who only have English newspaper subscriptions are:
 and .
Hence, the total is  students.
"""

# Enter your code here. Read input from STDIN. Print output to STDOUT

n=int(input())
s1=set(input().split())
m=int(input())
s2=set(input().split())
count=0
s=s1.difference(s2)
for x in s:
    count=count+1
print(count)
