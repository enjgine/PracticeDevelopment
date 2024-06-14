# Which starting number under one million produces the longest collatz chain

testednums = {}
limit = 1000000

# Test all nums up to limit
for i in range(1,limit):

	# Reset counters
	testnum = i
	counter = 0
	while True:
		counter += 1

		# Break once root reached
		if testnum == 1:
			testednums[i] = counter
			break

		# Test and modify by collatz rules
		if testnum % 2 == 0:
			testnum /= 2
		else:
			testnum = testnum * 3 + 1
		
		# Cut early if found previously
		if testnum in testednums:
			counter += testednums[testnum]
			testednums[i] = counter
			break

print(max(testednums, key=testednums.get))