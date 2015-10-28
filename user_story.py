input_file = open("input01.txt","r")

entries = []

for line in input_file:
	entries.append(line.rstrip())

count = (len(entries)+1)/4
for z in range(count):
	i = 0
	digits = []
	for j in range(9):
		digit = []
		digit.append(entries[z*4][i:i+3])
		digit.append(entries[z*4+1][i:i+3])
		digit.append(entries[z*4+2][i:i+3])
		i+=3
		digits.append(digit)
for digit in digits:
	for line in digit:
		print line
