# Snippets for my testing

def findifprime(num: int):
# This is most efficient up to 17 digits

	if num == 2 or num == 3:
		return True
	# Test for divison
	if num % 2 == 0 or num % 3 == 0:
		return False

	# Test for division up to square root by numbers of form 6n(-/+)1. Limit is **0.6 as floating point is not accurate enough for **0.5
	for x in range(6,int(num**0.6),6):
		if num % (x-1) == 0 or num % (x+1) == 0:
			return False

	# No division found return True
	return True
