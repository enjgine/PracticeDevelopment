# Find the largest palindrome made from the product of two 3 digit numbers

maxval = 0

# Search through all 3 digit numbers starting from max
for n in range(999,100,-1):
    # Search through all 3 digit numbers except those already tested
    for x in range(999-(999-n),100,-1):
        # Test these two numbers for palindromey (0,1,2,-3,-2,-1)
        i = n*x
        if str(i)[0] == str(i)[-1] and str(i)[1] == str(i)[-2] and str(i)[2] == str(i)[-3]:
            # Test if maxval has changed
            maxval = max(i, maxval)
print(maxval)