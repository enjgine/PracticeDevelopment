# Find the sum of the digits 100!

sum,revengeofthesum =1,0
for i in range(1,101):
	sum *= i
for i in str(sum):
	revengeofthesum += int(i)
print(revengeofthesum)