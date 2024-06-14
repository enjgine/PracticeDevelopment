# How many right/down paths exist for a 20x20 lattice [thanks @Asznard for refactoring the pathlist code]

# Ceate 20x20 matrix
pathlist = []
for y in range(21):
	path = []
	for x in range(21):
		if x == 0 or y == 0:
			path.append(1)
		else:
			path.append(0)
	pathlist.append(path)

# For each row and column, add the left and above value
for y in range(1,21):
	for x in range(1,21):
		pathlist[y][x] = pathlist[y-1][x] + pathlist[y][x-1]


print(pathlist[-1][-1])