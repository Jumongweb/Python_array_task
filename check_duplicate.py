def check_duplicate_value(item, my_list):
#	if item in my_list:
#		return


	count = 0
	checker = False
	for check in my_list:
		if item == check:
			item = check
			count += 1
		if count > 1:
			checker = True

	if checker == True:
		item = item
	elif count == 0:
		item = "No item on the list"
	else: 
		item = "No duplicate" 
	return item


my_list = [2, "apple", "banana", "banana", "apple", "Date"]
my_list2= ["Jumong", "Toheeb", "Lawal", "Prince"]

print(check_duplicate_value("apple", my_list))
print(check_duplicate_value("Lawal", my_list2))