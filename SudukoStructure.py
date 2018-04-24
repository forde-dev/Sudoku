# this reads the file and sortes it into lists within a list
def readBoard(file):
	infile = open(file, "r")
	b = []
	for line in infile:
		newline = line.strip("\n")
		row = newline.split(" ")

		# convert the list row to a list of numbers, not characters
		intRow = []
		for sNum in row:
			intRow.append(int(sNum))
		b.append(intRow)
	# print (b)

	infile.close()
	return b

# this prints the board when executed
def printBoard (SBoard):
	for rowNo in range (9):
		if rowNo % 3 == 0:
			print ("+---------+---------+---------+")
		for colNo in range (9):
			if colNo % 3 == 0:
				print ("|", end="")
			if SBoard[rowNo][colNo] == 0:
				print ("   ", end="")
			else:
				print (" %i " % (SBoard[rowNo][colNo]), end="")
		print ("|")
	print ("+---------+---------+---------+")
	
# this uses recursion to solve the sudoko
def solveBoard (b, row, col):
	# Find next empty cell
	result = False
	for i in range(0, 81):
		row = i // 9
		col = i % 9
		if b[row][col] == 0:
			for number in range(1, 10):
				# Check that this value has not already be used on this row
				if isValidMove(b, row, col, number):
					b[row][col] = number

					# A function to check if the grid is full

					def checkBoard(b):                   # this checks if the grid is complete, ie no 0 left in it
						for rowC in range(0, 9):
							for colC in range(0, 9):
								if b[rowC][colC] == 0:
									return False

						# We have a complete grid!
						return True

					if checkBoard(b):                # this checks if the grid is complete and returns the board to get printed
						print("\nSOLUTION :")
						result = True
						return b
					else:
						if solveBoard(b, row, col):
							result = True
							return b
			break

        # this is the backtrack
	print("Backtrack")
	b[row][col] = 0
	
# this verifies weather a number can be used in a certain cell
def isValidMove (b, row, col, number):

	valid = False
	if not (number in b[row]):
		# Check that this number has not already be used on this column
		if not number in (
				b[0][col], b[1][col], b[2][col], b[3][col], b[4][col], b[5][col], b[6][col],
				b[7][col], b[8][col]):
			square = []
			if row < 3:
				if col < 3:
					square = [b[i][0:3] for i in range(0, 3)]
				elif col < 6:
					square = [b[i][3:6] for i in range(0, 3)]
				else:
					square = [b[i][6:9] for i in range(0, 3)]
			elif row < 6:
				if col < 3:
					square = [b[i][0:3] for i in range(3, 6)]
				elif col < 6:
					square = [b[i][3:6] for i in range(3, 6)]
				else:
					square = [b[i][6:9] for i in range(3, 6)]
			else:
				if col < 3:
					square = [b[i][0:3] for i in range(6, 9)]
				elif col < 6:
					square = [b[i][3:6] for i in range(6, 9)]
				else:
					square = [b[i][6:9] for i in range(6, 9)]
			# Check that this number has not already be used on this 3x3 square
			if not number in (square[0] + square[1] + square[2]):
				valid = True

	return valid 	# this returns wether its valid or not



# Main Program
filename = "easyPuzzle.txt"
board = readBoard(filename)

print ("\nPROBLEM:")
printBoard(board)

printBoard(solveBoard(board, 0, 0))
