# Find the sum of even fibonacci sequence numbers below four million

calcunit = [0,1,1]
while True:
    if calcunit[1] >= 4000000:
        break
    else:
        if calcunit[1] % 2 == 0:
            calcunit[0] += calcunit[1]
        calcunit[1] += calcunit[2]
        calcunit[2] = calcunit[1] - calcunit[2]

print(calcunit[0])