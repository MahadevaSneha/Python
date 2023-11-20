"""
Sample Input

9
1 2 3 4 5 6 7 8 9
9
10 1 2 3 11 21 55 6 8
Sample Output

13
Explanation

Roll numbers of students who have at least one subscription:
 and . Roll numbers:  and  are in both sets so they are only counted once.
Hence, the total is  students.
"""
n=int(input())
s=set(input().split())
m=int(input())
s1=set(input().split())
s2=set()
count=0
s3=s.union(s1)
for x in s3:
    count=count+1
print(count)
