"""
Input Format

The first line contains an integer , the total number of country stamps.
The next  lines contains the name of the country where the stamp is from.
Constraints


Output Format

Output the total number of distinct country stamps on a single line.

Sample Input

7
UK
China
USA
France
New Zealand
UK
France 
Sample Output

5
Explanation

UK and France repeat twice. Hence, the total number of distinct country stamps is  (five).

"""

# Enter your code here. Read input from STDIN. Print output to STDOUT
s=set()
n=int(input())
count=0
for i in range(n):
    s1=input()
    if s1 not in s:
        s.add(s1)
        count=count+1
print(count)
