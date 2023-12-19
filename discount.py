def my_discount(price, discount):
	discount = (discount / 100) * price

	return price - discount

print(my_discount(150, 15))