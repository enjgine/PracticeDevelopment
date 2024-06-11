# Find a pythagorean triplet for whom the product of abc = 1000

triplets = []
for c in range(1,1000):
    for b in range(1,min(c,1000-c)):
        for a in range(1,min(b,1000-b)):
            if a+b+c == 1000 and a**2 + b**2 == c**2:
                print(a,b,c)