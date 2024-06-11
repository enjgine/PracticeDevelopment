# What is the value of the first tirangle number with over five hundred divisors

naturalnumber = 0
trianglenumber = 0

# Loop till found
while True:
	# Increment number and triangle, reset counter
	naturalnumber += 1
	divisorcount = 0
	trianglenumber += naturalnumber
	# Limit search to sqrt as no factors above sqrt are new
	limit = (trianglenumber**0.5)+1
	# Search all factors from 1 to sqrt and double increment (factor pairs)
	for i in range(1,int(limit)):
		if trianglenumber % i == 0:
			divisorcount += 2

	# Break once divisors high enough
	if divisorcount > 500:
		break
print(trianglenumber)
