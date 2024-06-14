# How many sundays fell on the first day of the month between 6 jan 1901 and 31 dec 2000

# List of first days and all base values
firstday = []
year = 1901
days = 0

months = [31,28,31,30,31,30,31,31,30,31,30,31]

while True:
# Adjust for feb weirdness 
	for i in months:
		if i == 28 and year % 4 == 0:
			days += 29
# Increment days
		else:
			days += i
# Set first day of month
		firstday.append(days)
# Increment year
	year += 1
# Once we have finished counting 2000, break
	if year > 1999:
		break

# Newday 6 is adjustment to sunday
newday = 6
sundays = 0

# When multiple of 7 aligns with first of month, increment
while True:
	newday += 7
	if newday in firstday:
		sundays += 1
	if newday > max(firstday):
		break
print(sundays)