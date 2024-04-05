def anagram(s,t):
    return int(sorted(s)==sorted(t))
s,t=input().split()
print(anagram(s,t))
