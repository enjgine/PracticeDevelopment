# Find the smallest number evenly divisible by all numbers 1-20

testnum = 20
# Loop breaks when all 20 divisions work
while True:
    correct = 0
    # Run over 1-20
    for i in range(1,21):
        # Break if not divisible
        if testnum % i != 0:
            break
        # Increment if divisible
        else:
            correct += 1
    # Check if division by all 20
    if correct == 20:
        break
    # Only iterate by multiples of 20
    testnum += 20
print(testnum)