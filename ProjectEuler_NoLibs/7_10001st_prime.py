# Find the 10 001st Prime Number

primelist = [2]
number = 2

# Break when 10,001 found
while len(primelist) < 10001:
    # Increment number
    number += 1
    # Reset test checker
    check = 0
    # Test for division among all current primes
    for i in primelist:
        if number % i == 0:
            break
        else:
            check += 1
    # Check if test checker passed all primes
    if check == len(primelist):
        primelist.append(number)
# Print last items
print(primelist[-1])