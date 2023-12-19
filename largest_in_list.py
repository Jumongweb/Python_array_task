def largest_number(numbers):
	if not numbers:
		return None

	largest = numbers[0]
	for number in numbers:
		if largest < number:
			largest = number

	return largest

print(largest_number([3,111,5,32,329]))

