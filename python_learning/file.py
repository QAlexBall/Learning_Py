import os
filename = 'sketch.txt'
# with open(filename, 'w') as file_object:
	# file_object.write("this is a new functions")
	# pass
try:
	with open(filename) as file_object:
		file_object.write("this is addtional")
except FileNotFoundError:
	print("file not found!")

try:
	answer = (5/0)
except ZeroDivisionError:
	print("you can't divide by zero")
else:
	print(answer)