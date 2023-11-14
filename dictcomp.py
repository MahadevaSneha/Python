#Dictionary comprehensions
squares={x:x*x for x in range(1,10)}
print(squares)
doubles={x:2**x for x in range(1,10)}
print(doubles)



"""
{1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81}
{1: 2, 2: 4, 3: 8, 4: 16, 5: 32, 6: 64, 7: 128, 8: 256, 9: 512}
"""
