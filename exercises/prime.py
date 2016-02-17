from math import sqrt
def is_prime(num):
    if num<2:
        return True;
    my_num = int(sqrt(num))
    for i in range(2, my_num+1):
        if num%i==0:
            return False;
    return True;

def get_largest_prime(num):
	for i in range(2, int(sqrt(num))+1):
		while num%i==0:
			if is_prime(num):
				break;
			num = num/i
	return num