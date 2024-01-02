import Divide_or_square

def test_divide_or_square():
	actual_result = Divide_or_square.divide_or_square(10)
	expected_result = round(3.16, 2)
	assert actual_result == expected_result