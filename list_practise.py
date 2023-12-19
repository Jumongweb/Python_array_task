my_list = [[1,3,6], "Neso", [7,4,9]]
my_list2 = ["George", "Jungle"]
my_list.append(5)
my_list.insert(0, -3)
print(my_list)

my_list.extend(my_list2)
print(my_list)
my_list3 = [[1,2,3],[['a','b','c'], 5,6]]
print(my_list3[1][0][1])
number = 1

print(type(number))