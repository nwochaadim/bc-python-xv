from math import sqrt
def is_prime(num):
    if num<2:
        return True;
    my_num = int(sqrt(num))
    for i in range(2, my_num+1):
        if num%i==0:
            return False;
    return True;

def get_largest_prime_factor(num):
    if num <= 0:
        return "Invalid Number"
    else:
    	for i in range(2, int(sqrt(num))+1):
    		while num%i==0:
    			if is_prime(num):
    				break;
    			num = num/i
    	return num

def censor(text, word):
    string = ''
    arrays = text.split()
    for array in arrays:
        if array==word:
            string+='*'*len(array)+" "
        else:
            string+=array+" "
    return string.rstrip()

def reverse_string(string):
  if string=='':
    return None
  my_string = ''
  for i in range(len(string)):
    my_string+=string[len(string)-i-1]
  if string==my_string:
    return True
  else:
    return my_string

def words(string):
  words = string.split()
  count = {}
  for word in words:
    if word.isdigit():
        word = int(word)
    if word in count:
      count[word]+=1
    else:
      count[word]=1
  return count

def data_type(arg):
  if type(arg) == str:
    return len(arg)
  elif type(arg) == None:
    return 'no value'
  elif type(arg) == bool:
    return arg
  elif type(arg) == int:
    if arg<100:
      return 'less than 100'
    else:
      return 'more than 100'
  elif type(arg) == list:
    if len(arg)>=3:
      return arg[2]
    else:
      return None

def add_two(x):
    return x+2

def do_arith(lst):
    my_lst = map(add_two, lst)
    return my_lst;

print(do_arith([1,2,3]))

print(data_type(None))

print(words("testing 1 2 testing"))


