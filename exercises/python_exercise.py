from functools import reduce
def get_largest(my_dict):
	highest = {}
	highest['count'] = 0;
	for item in my_dict:
		if highest['count']<len(my_dict[item]):
			highest['count'] = len(my_dict[item])
			highest['key'] = item
	return highest['key'];


my_dict = {};
my_dict['a']= ['Helen', 'Paul']
my_dict['b']=['Helen', 'Paul', 'Sandra', 'Ruth', 'Aisha']
my_dict['c']=['Helen', 'Paul', 'Sandra']

def get_factorial(num):
	if num>0:
		factorial = reduce(lambda x,y: x*y, range(1, num+1));
		return factorial;
	else:
		return "Number not valid"

def get_factorial1(num):
	if num>0:
		result = 1;
		for i in range(1, num+1):
			result*=i
		return result
	else:
		return "Number not valid"


print(get_factorial1(0));

print(get_largest(my_dict));
