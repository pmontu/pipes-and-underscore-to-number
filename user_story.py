input_file = open("input01.txt","r")

account_number_pipes_underscores = []
account_number_pipes_underscores.append(input_file.readline().rstrip())
account_number_pipes_underscores.append(input_file.readline().rstrip())
account_number_pipes_underscores.append(input_file.readline().rstrip())
for line in account_number_pipes_underscores: print line

s = ""
for i in range(1,10):
	 s += str(i)
s += s + s
print s

i = 1
for j in range(9):
	print i, i+1, i+2
	i+=3
	