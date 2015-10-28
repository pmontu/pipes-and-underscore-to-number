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

def valid(new_digit_in_a_line):
	isValid = False
	for item in master:
		if item["string"] == new_digit_in_a_line:
			isValid = True
			break
	return isValid

def ambivances(digit_in_a_line):
	amb = []
	add_pipe_positions = [3,5,6,8]
	add_underscore_positions = [1,4,7]

	def permute(pos, char):
		if digit_in_a_line[pos] != char:
			new_digit_in_a_line = digit_in_a_line[:pos]+char+digit_in_a_line[pos+1:]
			if valid(new_digit_in_a_line):
				amb.append(new_digit_in_a_line)
				return new_digit_in_a_line

	for pos in add_pipe_positions:
		permute(pos,"|")

	for pos in add_pipe_positions:
		permute(pos," ")

	for pos in add_underscore_positions:
		permute(pos,"_")

	for pos in add_underscore_positions:
		permute(pos," ")

	return amb