"""
Input Format

The first line contains , the number of students who have subscribed to the English newspaper.
The second line contains  space separated roll numbers of those students.
The third line contains , the number of students who have subscribed to the French newspaper.
The fourth line contains  space separated roll numbers of those students.

Constraints


Output Format

Output the total number of students who have subscriptions to both English and French newspapers.

Sample Input

9
1 2 3 4 5 6 7 8 9
9
10 1 2 3 11 21 55 6 8
Sample Output

5
Explanation

The roll numbers of students who have both subscriptions:
 and .
Hence, the total is  students.
"""




# Enter your code here. Read input from STDIN. Print output to STDOUT
n=int(input())
s1=set(input().split())
m=int(input())
s2=set(input().split())
s=s1.intersection(s2)
count=0
for x in s:
    count=count+1
print(count)
