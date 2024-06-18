# Evaluate the sum of all amicable numbers under 10000

divisors,totalsum = [0,],0

# Create list of divisors from 1
for x in range(1,10000):
	sublist = []
	for y in range(1,int(x/2 + 1)):
		if x % y == 0:
			sublist.append(y)
	divisors.append(sum(sublist))

# For each index, find divisors that point to the index
for index,sums in enumerate(divisors):
	try:
		if index == divisors[sums] and index != sums:
			print(index,sums,divisors[sums])
			totalsum += divisors[index]
	except IndexError:
		pass
print(totalsum)