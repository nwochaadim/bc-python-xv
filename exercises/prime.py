from math import sqrt
def is_prime(num):
    if num<2:
        return True;
    my_num = int(sqrt(num))
    for i in range(2, my_num+1):
        if num%i==0:
            return False;
    return True;

def find(n):
	i = 2;
	while i*i < n:
		while n%i==0:
			n = n/i
		i = i+1
	print(n);

def find2(num):
	result = 0
	for i in range(2, 999999):
		if is_prime(i) and num%i==0 and result<i:
			result = i
	return result

print(find(120))
