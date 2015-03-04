# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?

from math import sqrt

n = int(sqrt(600851475143))

def factor(x, y):
    return n ** 2 == x * y

for x in range(n, 1, -1):
    for y in range(n, 1, -1):
        if n ** 2 == x * y:
            print x, 'times', y, 'equals', n ** 2

