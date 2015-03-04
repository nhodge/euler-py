# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?

from math import sqrt

n = int(sqrt(600851475143))

def prime(x):
    y = int(sqrt(x))
    for x in range(y, 1, -1):
        if x % y == 0:
            print x, "is not prime."
        else:
            print x, "is prime."

for x in range(n, 1, -1):
    if 600851475143 % x == 0:
        prime(x)

