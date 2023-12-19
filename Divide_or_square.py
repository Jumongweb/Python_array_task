import math
def divide_or_square(number):
	#number = int(input("Enter a number: "))
	if number % 5 == 0:
		number = round(math.sqrt(number), 2)
	else:
		number = number % 5
	return number

print(divide_or_square(25))