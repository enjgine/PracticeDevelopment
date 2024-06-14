 # If all numbers 1 - 1000 were written as words, how many letters would be used?

ones = {
	0:'',1:'one',2:'two',3:'three',4:'four',5:'five',6:'six',
	7:'seven',8:'eight',9:'nine',10:'ten',11:'eleven',12:'twelve',
	13:'thirteen',14:'fourteen',15:'fifteen',16:'sixteen',
	17:'seventeen',18:'eighteen',19:'nineteen'}
tens = {
	0:'',2:'twenty',3:'thirty',4:'forty',5:'fifty',
	6:'sixty',	7:'seventy',8:'eighty',9:'ninety'}

all_words = ['one','thousand']
# Iterate across all numbers
for i in range(1,1001):
# First 20 special rules
	if i < 20:
		all_words.append(ones[i])
# Iterate two digit nums
	if 19 < i < 100:
		for y,z in str(i).split():
			all_words.append(tens[int(y)])
			all_words.append(ones[int(z)])
# Iterate three digit nums
	if 99 < i < 1000:
# x00
		if 0 == int(str(i)[1]+str(i)[2]):
			all_words.append(ones[int(str(i)[0])])
			all_words.append('hundred')
# x01 - x19
		if 1 <= int(str(i)[1]+str(i)[2]) < 20:
			all_words.append(ones[int(str(i)[0])])
			all_words.append('hundred')
			all_words.append('and')
			all_words.append(ones[int(str(i)[1]+str(i)[2])])
# x20 - x99
		elif 19 < int(str(i)[1]+str(i)[2]):
			all_words.append(ones[int(str(i)[0])])
			all_words.append('hundred')
			all_words.append('and')
			all_words.append(tens[int(str(i)[1])])
			all_words.append(ones[int(str(i)[2])])

print(all_words)
length = 0
for i in all_words:
	length += len(i)
print(length)