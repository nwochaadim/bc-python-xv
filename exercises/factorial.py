def get_factorial(num):
	""" Gets Facusing lamba functions """
	if num>0:
		factorial = reduce(lambda x,y: x*y, range(1, num+1));
		return factorial;
	else:
		return "Number not valid"