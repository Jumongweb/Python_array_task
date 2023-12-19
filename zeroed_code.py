def zeroed(my_list):
	my_list[0] = 0
	my_list[len(my_list) - 1] = 0
	return my_list

array = [2,5,1,6,9,43]

print(zeroed(array))
print(len(array))