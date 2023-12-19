import check_duplicate

def test_check_duplicate():
	expected = check_duplicate.check_duplicate_value("Toheeb", ["Jumong", "Toheeb", "Lawal", "Toheeb", "Prince"])
	actual = "Toheeb"
	assert actual == expected

def test_check_No_duplicate():
	actual = check_duplicate.check_duplicate_value("cashew", ["apple", "banana", "cashew", "date"]) 
	expected = "No duplicate"
	assert actual == expected