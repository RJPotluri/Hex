import math
import time

number = int(input('Number: '))
start = time.time()

if number > 0:
	list1 = []
	value = math.log(number,16)
# take the log value of the number

	"""print (value)"""
	
	n = math.floor(value)+1
# find the length of the hex number

	while len(list1)<n:
		list1.append(0)	
# create a list of blank placeholders for number length

	"""print (list1)"""
	x = 0
	
	while x < n:
		value = math.floor(number/(16**((n-x)-1)))
		list1[x] = value
		x += 1
		number = number - (value * 16**(n-x))
		"""print (number)"""
		
# set the leftmost digit as the number of times the highest possible
# exponent number (ex. 16^2) fits into the orignal number 
# 16**(n-1) = 16**(n-x-1)

	"""print (list1)"""

	for item in list1:
		if item == 10:
			list1[list1.index(10)] = 'A'
		if item == 11:
			list1[list1.index(11)] = 'B'
		if item == 12:
			list1[list1.index(12)] = 'C'
		if item == 13:
			list1[list1.index(13)] = 'D'
		if item == 14:
			list1[list1.index(14)] = 'E'
		if item == 15:
			list1[list1.index(15)] = 'F'
# Check the list and replace values > 9 with corresponding letters
			
	"""print (list1)"""
	string1 = ''.join(str(e) for e in list1)
# convert list into a single string

	print ("Hexadecimal: %s" % (string1))
	print ("Converted in %s seconds" % ((time.time() - start)))
elif number == 0:
	print (0)
	print ("Converted in %s seconds" % ((time.time() - start)))
else:
	print ("Entered value was not a positive integer.")