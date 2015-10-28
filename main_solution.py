from digit import ambivances, valid

config = [
	{"input":"input01.txt", "output":"output01.txt", "level":1},
	{"input":"input02.txt", "output":"output02.txt", "level":3},
	#{"input":"input03.txt", "output":"output03.txt", "level":4},
]

for setting in config:
	print(setting)
	input_file = open(setting["input"],"r")

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

	def pipes_underscores_to_a_string_digit(s):
		d = "?"
		for item in master:
			if s == item["string"]:
				return str(item["number"])
		return d

	def check(account_num_converted):
		if account_num_converted.find("?") == -1:
			check_sum = 0
			for index, digit in enumerate(account_num_converted):
				check_sum += (9-index) * int(digit)
			if check_sum % 11 == 0 : return ""
			else: return "ERR"
		else: return "ILL"

	output_file = open(setting["output"],"r")
	#for each entry. conversion to digits then account number then validation.
	#output ie account number and status if needed are printed.
	for num in acc_nums:

		account_num_converted = ""
		for digit in num:
			pipes_and_underscores_of_a_digit = ""
			for line in digit:
				pipes_and_underscores_of_a_digit += line
			account_num_converted += pipes_underscores_to_a_string_digit(pipes_and_underscores_of_a_digit)

		expected = output_file.readline().rstrip("\n")
		if setting["level"]==1:
			output = account_num_converted
			assert output == expected
			print (output)
		if setting["level"]==3:
			output = account_num_converted
			#analysis of check sum and illegible digits
			check_val = check(account_num_converted)
			if check_val:
				output += check_val.rjust(4, " ")
			assert output == expected
			print (output)
		#if setting["level"]==4: