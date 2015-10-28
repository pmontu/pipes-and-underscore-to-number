config = [
	{"input":"input01.txt", "output":"output01.txt", "level":1},
	{"input":"input02.txt", "output":"output02.txt", "level":3},
	{"input":"input03.txt", "output":"output03.txt", "level":4},
]
CONFIG_NUM = 1
input_file = open(config[CONFIG_NUM]["input"],"r")

entries = []

for line in input_file:
	entries.append(line.rstrip("\n"))

#number of entries in input file
count = int((len(entries)+1)/4)
acc_nums = []
#vertical traversal
for z in range(count):
	#column start of every digit
	i = 0
	digits = []
	#horizontal traversal
	for j in range(9):
		#3 lines height, 9 digits each 3 columns width
		digit = []
		digit.append(entries[z*4][i:i+3].ljust(3," "))
		digit.append(entries[z*4+1][i:i+3])
		digit.append(entries[z*4+2][i:i+3])
		#ignore 4th line
		i+=3
		digits.append(digit)
	acc_nums.append(digits)

#all digits respective pipe and underscore value. 3 rows and 3 columns expressed in 1 row and 9 columns.
master = [
	{"string":" _ | ||_|","number":0},
	{"string":"     |  |","number":1},
	{"string":" _  _||_ ","number":2},
	{"string":" _  _| _|","number":3},
	{"string":"   |_|  |","number":4},
	{"string":" _ |_  _|","number":5},
	{"string":" _ |_ |_|","number":6},
	{"string":" _   |  |","number":7},
	{"string":" _ |_||_|","number":8},
	{"string":" _ |_| _|","number":9},
]

def search(master, s):
	d = "?"
	for item in master:
		if s == item["string"]:
			return item["number"]
	return d

def check(account_num):
	if account_num.find("?") == -1:
		check_sum = 0
		for index, digit in enumerate(account_num):
			check_sum += (9-index) * int(digit)
		if check_sum % 11 == 0 : return ""
		else: return "ERR"
	else: return "ILL"

output_file = open(config[CONFIG_NUM]["output"],"r")
for num in acc_nums:
	account_num = ""
	for digit in num:
		s = ""
		for line in digit:
			s += line
		account_num += str(search(master, s))

#check ambivalence
for num in acc_nums:
	account_num = ""
	
	for digit in num:
		s = ""
		for line in digit:
			s += line
		account_num += str(search(master, s))
	expected = output_file.readline().rstrip("\n")
	if config[CONFIG_NUM]["level"]==1:
		output = account_num
		assert output == expected
		print (output)
	if config[CONFIG_NUM]["level"]==3:
		output = account_num
		#analysis of check sum and illegible digits
		check_val = check(account_num)
		if check_val:
			output += check_val.rjust(4, " ")
		assert output == expected
		print (output)
	if config[CONFIG_NUM]["level"]==4: