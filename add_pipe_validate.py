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
for i in range(1,2):
	digit_in_a_line = master[i]["string"]
	print(digit_in_a_line)

	def logic(pos, char):
		if digit_in_a_line[pos] != char:
			new_digit_in_a_line = digit_in_a_line[:pos]+char+digit_in_a_line[pos+1:]
			amb.append(new_digit_in_a_line)
			isPipeChanged = True
			return new_digit_in_a_line

	amb = []
	add_pipe_positions = [3,5,6,8]
	add_underscore_positions = [1,4,7]

	print("\nPipes")
	for pos in add_pipe_positions:
		#print(logic(pos,"|"))
		if digit_in_a_line[pos] != "|":
			new_digit_in_a_line = digit_in_a_line[:pos]+"|"+digit_in_a_line[pos+1:]
			amb.append(new_digit_in_a_line)
			print (new_digit_in_a_line)

	print("\nPipes Not")
	for pos in add_pipe_positions:
		#print(logic(pos," "))
		if digit_in_a_line[pos] != " ":
			new_digit_in_a_line = digit_in_a_line[:pos]+" "+digit_in_a_line[pos+1:]
			amb.append(new_digit_in_a_line)
			print (new_digit_in_a_line)

	print("\nUnderscore")
	for pos in add_underscore_positions:
		#print(logic(pos,"_"))
		if digit_in_a_line[pos] != "_":
			new_digit_in_a_line = digit_in_a_line[:pos]+"_"+digit_in_a_line[pos+1:]
			amb.append(new_digit_in_a_line)
			print (new_digit_in_a_line)

	print("\nUnderscore Not")
	for pos in add_underscore_positions:
		#print(logic(pos," "))
		if digit_in_a_line[pos] != " ":
			new_digit_in_a_line = digit_in_a_line[:pos]+" "+digit_in_a_line[pos+1:]
			amb.append(new_digit_in_a_line)
			print (new_digit_in_a_line)

