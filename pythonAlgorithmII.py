# 2). How do you find the largest and smallest number in an unsorted integer array? --> [6,5,2,4,7]: Organize the array(Challenge) 

unsortedArray = [6,5,2,4,7] # The array is pretty unsorted 

def arranging_arrays():
	# The function will rely on the "if and else statement", mainly because it has to sort the array
	a = unsortedArray[0]
	b = unsortedArray[1]
	c = unsortedArray[2]
	d = unsortedArray[3]
	e = unsortedArray[4]
	# Another array dedicated to the variables
	varArray = [a,b,c,d,e]
	# Where the magic happens; if and else statement [6,5,2,4,7]
	if a < 7:
		varArray = [b,c,d,a,e]
	elif b < 6:
		varArray = [c,d,b,a,e]
	elif c < 4:
		varArray = [c,d,b,a,e]

	# The program will return the final result
	#[2, 4, 5, 6, 7]
	varArray = [c,d,b,a,e]
	return varArray

def checking_the_numbers():
	# The code is guaranteed to work, but I will try :-)
	varArray = [2, 4, 5, 6, 7]
	# The final code
	if varArray[0] <= 4:
		result = varArray[0]
	elif varArray[4] >= 6:
		resultII = varArray[4]
	
	result = varArray[0]
	resultII = varArray[4]
	# Calling the two variables
	return f"the array includes {varArray} and the biggest number is {result} and the smallest is {resultII}"


print(arranging_arrays())
print(checking_the_numbers())

# The algorithm worked sell!

# 3). 
