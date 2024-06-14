# What is the sum of the digits of 2**1000

testnum = 2**1000
testnum = str(testnum)
testlist = []
for i in testnum:
	testlist.append(int(i))
print(sum(testlist))