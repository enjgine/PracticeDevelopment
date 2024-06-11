# What is the largest prime factor of 600851475143
import math

n = 600851475143
i = 2
# Will reach 1 when last prime div by self
while n > 1:
	# Prime to div by will always grow in size, check if current composite is divisible
	if n % i == 0:
		# If divisible, divide by prime
		n /= i
	# If current prime is above squareroot of current composite, then current composite must be prime, as there cannot be 2 factors above sqrt
	elif i > math.sqrt(n):
		# Set current prime to current composite, so that we will divide n by itself and exit
		i = n
	# If current composite is not divisible, look for next prime to divide (all composites up to next prime cannot divide current composite)
	else:
		i += 1
print(i)