# What is the largest prime factor of 600851475143
import math

n = 600851475143
i = 2
while n > 1:
    if n % i == 0:
        n /= i
    elif i > math.sqrt(n):
        i = n
    else:
        i += 1
print(i)