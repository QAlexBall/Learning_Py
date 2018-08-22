def is_odd(n):
	return n % 2 == 1

def not_empty(s):
	return s and s.strip()

a = list(filter(is_odd, [1, 2, 4, 5, 6, 7, 8]))
b = list(filter(not_empty, ['A', '' , 'B', None, 'C', ' ']))
# filter 函数返回的是一个Iterator, 也就是一个惰性序列

print(a, b)

def _odd_iter():
	n = 1
	while True:
		n = n + 2
		yield n
def _not_divisible(n):
	return lambda x: x % n > 0

def primes():
	yield 2
	it = _odd_iter()
	while True:
		n = next(it)
		yield n
		it = filter(_not_divisible(n), it)
		# 先过滤掉能整除3的数,从这个基础上过滤掉能整除5的数......    
		# 这里it = filter((...)(_not_disivible(n-2), fileter(_notdivisble(n-1), filter(_not_divisible(n), it))))
		# 也就是说过滤了能整除除以[3, 5, 7, 11...](当前要求的质数之前的质数)的数

for n in primes():
	if n < 30:
		print(n)
	else:
		break

func = _not_divisible(9)	# _not_divisible(9) 返回一个函数(x % 9 > 0)
print(func(18))				# 18 % 9 == 0, return false

f = lambda x: x * x
print(f(19))
