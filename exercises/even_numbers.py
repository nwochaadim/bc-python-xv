def even_numbers(low, high):
	if low<high:
		if type(low) != int and type(high) != int:
			return "Arguments are not strings"
			
		num = range(low, high)
		mylist = []
		for i in num:
			if i%2==0:
				mylist.append(i)
		return mylist
	else:
		return "Error, Arguments are incorrect"

