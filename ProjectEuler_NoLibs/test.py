pathlist = [[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]
for y in range(5):
    for x in range(5):
        if x == 0 or y == 0:
            pathlist[y][x] = 1
print(pathlist)