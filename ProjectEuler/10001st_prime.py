# Find the 10 001st Prime Number

primelist = [2]
number = 2
while len(primelist) < 10001:
    number += 1
    check = 0
    for i in primelist:
        if number % i == 0:
            break
        else:
            check += 1
    if check == len(primelist):
        primelist.append(number)
print(primelist[-1])