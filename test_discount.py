import discount

def test_discount():
	actual = discount.my_discount(150, 15)
	expected = 127.5
	assert actual == expected

def test_discount2():
	actual = discount.my_discount(3000, 10)
	expected = 2700
	assert actual == expected