def add():

	user_input = input("Enter Numbers: ")
	addition = 0

	for i in user_input:
		if i.isnumeric():
			addition += int(i)

	print(addition)

add()