def float_check(num1, num2):
	count = 0
	if isinstance(num1, float):
		count += 1
	if isinstance(num2, float):
		count += 1
	return count

	"""
	count = 0
	if type(num1) == type(1.0) and type(num2) == type(1.0):
		count += 2
	elif type(num1) == type(1.0):
		count += 1

	return count
	"""

print(float_check(21.4, 1.3))