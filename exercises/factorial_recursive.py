def factorial(num):
	while num>0:
		return num * factorial(num-1)
	else:
		return 1
print factorial(4)