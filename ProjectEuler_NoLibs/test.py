listy = ['AA','BB','CC','AA','BB','CC']

listy.sort()

print(listy)

listz = [0,'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
listx = []

for i in range(0,len(listy)):
	listx.append(0)
	for x in range(0,len(listy[i])):
		for index,key in enumerate(listz):
			if key == listy[i][x].lower():
				listx[i] += index

print(listx)

for index,value in enumerate(listx):
	listx[index] *= (index+1)   
print(listx)

print(sum(listx))