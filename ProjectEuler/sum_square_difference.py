# Find the difference between the sum of squares and square of sums of 1-100

sumsquare = 0
squaresum = 0
for i in range(1,101):
    sumsquare += i**2
    squaresum += i
squaresum **= 2
print(squaresum-sumsquare)