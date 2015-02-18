import random, math

def column(matrix, i):
	"""
	Returns the ith column of the matrix.
	"""
	return [row[i] for row in matrix]

def row(matrix, i):
	"""
	Returns the ith row of the matrix.
	"""
	return matrix[i]

def swap(a1, a2):
	"""
	Swaps two elements.
	"""
	return a2, a1

def dirtyRow(arr):
	"""
	Returns 1 if a row is dirty and 0 if not.
	"""
	symbol = arr[0]			# hold the first symbol of the row
	counter = 0 		  
	for s in arr:			# for every symbol of the row
		if (s == symbol):	# if the first symbol is used more than once
			counter = counter + 1

	if counter == len(arr): # clean row
		return 0 
	else: 					# dirty row
		return 1

def printMatrix(matrix):
	"""
	Prints the matrix in a user friendly format.
	"""
	length = len(matrix)
	row = " "
	separator = length* "---|"
	
	for i in range (0, length):
		for j in range (0, length):
			row = row + str(matrix[i][j]) +  " | "
		print row[0:-3]
		row = " "
		if (i != (length-1)): print separator[0:-1]

def OddEvenSort(arr, flag):
	"""
	Returns a sorted array using the Odd-Even transposition algorithm
	and the number of steps needed.
	"""
	sorted1, sorted2 = False, False			# flags for the two different types of compare
	steps = 0								# initialize steps variable

	while ((not sorted1) or (not sorted2)): # while array is not sorted
		sorted1, sorted2 = True, True		# reset flags
		for i in range(0, len(arr) - 1, 2): # for pairs 0-1, 2-3, 4-5, ..
			if (flag == 'R'):				# ascending order
				if(arr[i] > arr[i+1]):
					arr[i], arr[i+1] = swap(arr[i], arr[i+1])
					sorted1 = False
			elif (flag == 'L'): 			# descending order
				if(arr[i] < arr[i+1]):
					arr[i], arr[i+1] = swap(arr[i], arr[i+1])
					sorted1 = False

		# if a swap was made to the array, add one step 
		if (sorted1 == False): steps = steps+1

		for i in range(1, len(arr) - 1, 2): # for pairs 1-2, 3-4, 5-6, ..
			if (flag == 'R'): 				# ascending order
				if(arr[i] > arr[i+1]):
					arr[i], arr[i+1] = swap(arr[i], arr[i+1])
					sorted2 = False

			elif (flag == 'L') : 			# descending order
				if(arr[i] < arr[i+1]):
					arr[i], arr[i+1] = swap(arr[i], arr[i+1])
					sorted2 = False

		# if a swap was made to the array, add one step 
		if (sorted2 == False): steps = steps+1

	return (arr, steps)

def ShearSort(N):
	"""
	Returns a random NxN matrix sorted using the Shearsort algorithm.
	"""
	# define matrix
	myMatrix = [[0 for i in xrange(N)] for i in xrange(N)] 

	tmp_steps, steps = 0, 0 				# temp variables holding steps
	sum_steps = 0 							# sum of steps 

	# randomize matrix
	for i in range(0, N):
		for j in range(0, N):
			myMatrix[i][j] = random.randint(0, 1)
	
	print "Initial Phase:"
	printMatrix(myMatrix)					# print initial matrix

	for phase in range(1, N+2):				# for every phase (1, .., N+1)
		steps = 0 							# reset counter in every phase
		if (phase%2 == 1):					# phase 1, 3, 5..
			for r in range(0, N):			# for every row
				if (r%2 == 0):				# even rows are sorted in ascending order
					arr, tmp_steps = OddEvenSort(row(myMatrix, r), 'R')
				elif (r%2 == 1):			# odd rows are sorted in descending order
					arr, tmp_steps = OddEvenSort(row(myMatrix, r), 'L')
				
				# hold the max steps needed for the Odd-Even sort for the row
				if steps < tmp_steps: steps = tmp_steps 

		elif (phase%2 == 0):				# phase 2, 4, 6..
			for c in range(0, N):			# for every column
				# columns are sorted in ascending order
				tmp_col, tmp_steps = OddEvenSort(column(myMatrix, c), 'R')
				for r1 in range(0, N): 		# update matrix
					myMatrix[r1][c] = tmp_col[r1]
				
				# hold the max steps needed for the Odd-Even sort for the row
				if steps < tmp_steps: steps = tmp_steps
		
		# sum the steps needed for the current phase
		sum_steps = sum_steps + steps

		# print matrix
		print "\nPhase " + str(phase) + ":"
		printMatrix(myMatrix)

		# calculate dirty rows
		dirty_rows = 0 						# reset dirty rows counter in every phase
		for r in range(0, N):				# for every row
			dirty_rows = dirty_rows + dirtyRow(row(myMatrix, r))	
		print "Dirty rows: " + str(dirty_rows)

	print "\nSteps needed: " + str(sum_steps)

	return myMatrix

if __name__ == "__main__":
	dim = input("Please enter dimension: ")
	ShearSort(dim) 							# Run the ShearSort function
	raw_input("Press any key to continue...")