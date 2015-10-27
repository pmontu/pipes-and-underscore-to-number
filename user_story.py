input_file = open("input01.txt","r")

entries = []

for line in input_file:
	entries.append(line.rstrip())

count = (len(entries)+1)/4

i = 1
for j in range(9):
	print i, i+1, i+2
	i+=3
