# The important modules for the algorithm; mainly to 
from random import randint
import random
# 1). Create a program; that lists the sub-sets that adds up to a certain number, 16. 
array =  [2,4,6,10]

# First Attempt
def counts_set():
	countArray = len(array)
	# The total of the array
	#total = 26
	# The validating statement for the array/algorithm
	if array > 4:
		return False # Application with boolean
	elif array < 4:
		return False # Boolean function makes the program more robust
	elif array == 4:
		pass

def rec():
	countArray = len(array)
	array =  [2,4,6,10]
	# Counting the numbers with variables
	a = array[0]
	b = array[1]
	c = array[2]
	d = array[3]

	# Considering this an attempt, it will be not be very sophisticated
	# Hopefuly, the code will run just fine :-)
	print("Our task is find the sub-sets of 16 in array [2,4,6,10]. ")
	addingArrays = print(random.randint(a+b+c+d))
	# The main program of the whole task
	for i in array:
		if addingArrays == 16:
			result1 = (a+b+d)
			result2 = (c+d)
			# Calling the results
			return result1, result2

#while True:
	# The array
	#array =  [2,4,6,10]
	# The basic validation statement
	#if 16%2==0:
		#pass
	#else:
		#break

	# 					*** Construction Site***
	# There syntax errors currently, but fixing would not be a challenge

	#print(counts_set())
	#print(rec())


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