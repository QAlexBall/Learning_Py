print(abs(-10))
print(abs)
f = abs
print(f(-10))

def add(x, y, f):
	return f(x) + f(y)
print(add(-5, 6, abs))
"""
python内建了map()和reduce()函数
map()函数接收两个参数, 一个是函数, 一个是Iterable,
map将传入的函数依次作用到序列的每个元素, 并把结果作为新的Iterator返回.
"""
def f(x):
	return x * x
r = map(f, [1, 2, 3, 4, 5, 6, 7, 8, 9])
print(list(r))
x = [1, 2, 3]
y = iter(x)
print(next(y), next(y))
while True:
	try:
		print(next(y))
	except StopIteration as e:
		print('Generator return value: ', e.value)
		break

f = list(map(str, [1, 2, 3]))
print(f)
"""
a = [1, 2, 3]
b = type(a)
print(b)
# print(next(b)) TypeError: 'type' object is not an iterator
# c = iter(b) TypeError: 'type' object is not iterable
from itertools import islice
class Fib:
    def __init__(self):
        self.prev = 0
        self.curr = 1

    def __iter__(self):
        return self

    def __next__(self):
        value = self.curr
        self.curr += self.prev
        self.prev = value
        return value
f = Fib()
print(next(f), f.__next__(), f.__iter__(), f.__next__(), f.__next__(), f.__next__(), next(f))
f = type(f)
"""