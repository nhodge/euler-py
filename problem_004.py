# A palindromic number reads the same both ways. The largest palindrome made
# from the product of two 2-digit numbers is 9009 = 91 x 99.
# Find the largest palindrome made from the product of two 3-digit numbers.

max_pal = 0

def palindrome(n):
    return n == int(str(n)[::-1])

for x in range(999, 99, -1):
    for y in range(999, 99, -1):
        n = x * y
        if n > max_pal and palindrome(n):
            max_pal = n

print max_pal
