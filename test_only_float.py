import only_float

def test_for_two_float():
	actual = only_float.float_check(2.4, 1.0)
	expected = 2
	assert actual == expected

def test_for_one_float():
	actual = only_float.float_check(2, 2.3);
	expected = 1
	assert actual == expected

def test_for_no_float():
	actual = only_float.float_check(5, 6)
	expected = 0
	assert actual == expected