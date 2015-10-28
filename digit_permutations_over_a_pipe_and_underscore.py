from digit import ambivances

tests = [
	"     |  |"
]
for item in tests:
	digit_in_a_line = item

	amb = ambivances(digit_in_a_line)

	for item in amb:
		print(item)
	print()