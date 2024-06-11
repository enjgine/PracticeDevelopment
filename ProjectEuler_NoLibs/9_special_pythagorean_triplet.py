# Find a pythagorean triplet for whom the product of abc = 1000

triplets = []
# Test all numbers to 1000
for c in range(1,1000):
    # Test all numbers excluding where sum is greater than 1000
    for b in range(1,min(c,1000-c)):
        # Test all numbers excluding where sum is greater than 1000
        for a in range(1,min(b,1000-b)):
            # Check if sum is 1000 and if pythagorean triplet
            if a+b+c == 1000 and a**2 + b**2 == c**2:
                print(a,b,c)