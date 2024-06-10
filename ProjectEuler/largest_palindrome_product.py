# Find the largest palindrome made from the product of two 3 digit numbers

maxval = 0
for n in range(999,100,-1):
    for x in range(999-(999-n),100,-1):
        i = n*x
        if str(i)[0] == str(i)[-1] and str(i)[1] == str(i)[-2] and str(i)[2] == str(i)[-3]:
            maxval = max(i, maxval)
print(maxval)