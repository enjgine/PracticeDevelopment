# Find the sum of even fibonacci sequence numbers below four million

# Memreg [sum,currentnum,lastnum]
calcunit = [0,1,1]
while True:

    # Break at currentnum 4,000,000
    if calcunit[1] >= 4000000:
        break
    else:

        # Add sum if currentnum even
        if calcunit[1] % 2 == 0:
            calcunit[0] += calcunit[1]

        # Set current num to current + last
        calcunit[1] += calcunit[2]
        
        # Set last num to current - last
        calcunit[2] = calcunit[1] - calcunit[2]

print(calcunit[0])