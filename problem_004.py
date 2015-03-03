# A palindromic number reads the same both ways. The largest palindrome made
# from the product of two 2-digit numbers is 9009 = 91 x 99.
# Find the largest palindrome made from the product of two 3-digit numbers.

max_pal = []

def palindrome(n):
    return n == int(str(n)[::-1])

for x in range(100, 1000):
    for y in range(100, 1000):
        n = x * y
        if palindrome(n):
            max_pal.append(n)

print max(max_pal)
