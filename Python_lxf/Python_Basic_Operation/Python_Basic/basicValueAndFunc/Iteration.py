d = {'a': 1, 'b': 2, 'c': 3}
for key in d:
	print(key)
for ch in 'ABC':
	print(ch)

"""
可直接作用于for循环的对象称为可迭代对象: Iteration
"""
from collections import Iterable
print(isinstance('abc', Iterable), '  ', isinstance([1, 2, 3], Iterable), '  ', isinstance(123, Iterable))
for i, value in enumerate(['A', 'B', 'C']):
	print(i, value)
for x, y in [(1, 1), (3, 4), (3, 9)]:
	print(x, y)
print(isinstance([], Iterable), isinstance({}, Iterable), isinstance((), Iterable))
print(isinstance(100, Iterable))
"""
可以被next()函数调用并不断返回下一个值的对象称为迭代器: Iterator
Iterator对象标识的是一个数据流, Iterator对象可以被next()函数调用并不断返回下一个数据,
知道没有数据时抛出StopIteration错误.
"""
from collections import Iterator
print(isinstance((x for x in range(10)), Iterator))
print(isinstance([], Iterator), isinstance({}, Iterator), isinstance((), Iterator))
it = iter([1, 2, 3, 4, 5])
while True:
	try:
		x = next(it)
		print(x)
	except StopIteration:
		break

""" 
列表生产式 List comprehensions, 是python内置的非常简单却强大的可以用来创建list的生成式
"""
"""
L = list(range(1, 11))
print(L)
L = []
for x in range(1, 11):
	L.append(x * x)
print(L)
L = [x * x for x in range(1, 11)]
print(L)
L = [m + n + w for m in 'ABC' for n in 'XYZ' for w in 'EDF']
print(L)
import os
L = [d for d in os.listdir('..')]
print(L)
d = {'x': 'A', 'y': 'B', 'z': 'C'}
for k, v in d.items():
	print(k, '=', v)
L = [k + '=' + v for k, v in d.items()]
print(L)
L = ['Hello', 'World', 'IBM', 'Apple']
L = [s.lower() for s in L]
print(L)

L = ['Hello', 'World', 18, 'Apple', None]
i = -1
for words in L:
	i = i + 1
	if(isinstance(words, str) == False):
		print(i)
		L.pop(i)
	#words.lower()
L = [s.lower() for s in L]
print(L)

print(isinstance(None, str))
"""