# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?

from math import sqrt
from math import ceil

n = int(ceil(sqrt(600851475143)))

def factor(x, y):
    return x * y == 600851475143

for x in range(n, 1, -1):
    for y in range(n, 1, -1):
        if factor(x, y):
            print x, 'times', y, 'equals', 600851475143

