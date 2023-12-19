import zeroed_code

def test_zeroed_code():
	actual = zeroed_code.zeroed([1,2,3,4,5,6])
	expected = [0,2,3,4,5,0]
	assert actual == expected