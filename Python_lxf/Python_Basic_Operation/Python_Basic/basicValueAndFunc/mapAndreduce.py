a = list(map(str, [1, 2, 3, 4, 5]))
print(a)
def f(x):
	return 2 * x;
b = list(map(f, [1, 2, 4]))
print(b)

'''
reduce把一个函数作用在一个序列[x1, x2, x3, ...]上,
这个函数必须接收两个参数, reduce把结果继续和序列的下一个元素做累计算
reduce(f, [x1, x2, x3, x4]) = f(f(f(x1, x2), x3), x4)
'''
from functools import reduce
def add(x, y):
	return x + y
c = reduce(add, [1, 3, 5, 7, 9])
print(c)

def fn(x, y):
	return x * 10 +y
d = reduce(fn, [1, 3, 5, 7, 9])
print(d)
# input: 13579

