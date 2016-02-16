def even_numbers(low, high):
	
	if type(low) == int and type(high) == int and low<high:
		num = range(low, high)
		mylist = []
		for i in num:
			if i%2==0:
				mylist.append(i)
		return mylist
	else:
		return "Error, Arguments are incorrect"
