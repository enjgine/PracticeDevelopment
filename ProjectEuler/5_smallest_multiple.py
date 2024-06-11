# Find the smallest number evenly divisible by all numbers 1-20

testnum = 20
while True:
    correct = 0
    for i in range(1,21):
        if testnum % i != 0:
            break
        else:
            correct += 1
    if correct == 20:
        break
    testnum += 20
print(testnum)