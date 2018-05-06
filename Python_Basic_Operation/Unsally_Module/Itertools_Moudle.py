 # python的内建模块itertools提供了非常有用的用于操作迭代对象的函数
 # itertools"无限"迭代器
import itertools
natuals = itertools.count(5) # count()会创建一个无限迭代器
for n in natuals:
	print(n)
	if n == 10:
		break

n = 0
cs = itertools.cycle('ABC') # cycle()会把传入的要给序列无限重复下去
num = itertools.count(1)
for c in cs:
	if c == 'C':
		n = n + 1
		if n == 2:
			break
	print(c)

ns = itertools.repeat('A', 3) # repeat()负责把一个元素无限重复下去, 第二个参数限定重复次数
for n in ns:
	print(n)
	
# takewhile()等函数根据条件判断来截取出一个有限的序列
natuals = itertools.count(1)
ns = itertools.takewhile(lambda x: x <= 8, natuals)
print(list(ns))
print(ns)
print(dir(ns))

# itertools提供几个迭代器操作函数
# chain()可以把得带对象串联起来, 形成一个更大的迭代器
for c in itertools.chain('ABC', 'XYZ'):
	print(c)
# groupby()把迭代器中相邻的重复元素挑出来放在一起
for key, group in itertools.groupby('AAABBBCCAAA'):
	print(key, list(group))
# 忽略大小写分组
for key, group in itertools.groupby('AaaBBbcCAAa', lambda c: c.upper()):
	print(key, list(group))

# itertools模块提供的全部是处理迭代功能的函数, 它们的返回值不是list
# 而是Iterator, 只有用for循环得带的时候才真正计算