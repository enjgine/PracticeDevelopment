# Find the sum of all primes below two million

from my_library import findifprime

# Floating point issues with limiting prime search to x**0.5 as some are product of prime**2, so findifprime uses x**0.6 as limit (Arbitrary)
primes = int(0)
# Test all 2,000,000 numbers
for i in range(2,2000000):
	# Test if prime
	if findifprime(i) == True:
		# Increment prime sum
		primes += int(i)

print(primes)