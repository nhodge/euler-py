# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?

from math import sqrt

n = int(sqrt(600851475143))

def prime(x):
    y = int(sqrt(x))
    for i in range(y, 1, -1):
        if x % i == 0:
            return False
    return True

for x in range(n, 1, -1):
    if 600851475143 % x == 0:
        if prime(x):
            print x
            break

