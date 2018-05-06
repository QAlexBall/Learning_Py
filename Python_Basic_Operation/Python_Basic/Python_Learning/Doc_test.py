# 自动执行卸载注释中的这些代码
#
#
import re
m = re.search('(?<=abc)def', 'abcdef')
print(m.group(0))

def abs(n):
	'''
	Function to get absolute value of number.
	Example:
	>>> abs(1)
	1
	>>> abs(-1)
	1
	>>> abs(0)
	0
	'''
	return n if n >= 0 else (-n)
# python内置的'文档测试'(doctest)模块可以直接提取注释中的代码并执行测试
# doctest严格按照python交互式命令行的输入和输出来判断测试结果是否正确
# 只有测试异常的时候, 可以用...表示中间一大段输出

class Dict(dict):
	'''
	Simple dict but alse support access as x.y style.y		
	>>> d1 = Dict(x=100, y=100)
	>>> d1['x']
	100
	>>> d1.y = 200
	>>> d1['y']
	200
	>>> d2 = Dict(a=1, b=2, c='3')
	>>> d2['c']
	'3'
	>>> d2['empty']
	Traceback (most recent call last):
		...
	KeyError: 'empty'
	>>> d2.empty
	Traceback (most recent call last):
		...
	AttributeError: 'Dict' object has no attribute 'empty'
	'''
	def __init__(self, **kw):
		super(Dict, self).__init__(**kw)

	def __getattr__(self, key):
		try:
			return self[key]
		except KeyError:
			raise AttributeError(r"'Dict' object has no attribute '%s'" % key)

	def __setattr__(self, key, value):
		self[key] = value
d = Dict(a=1, b=2)
d['a'] = 100
d.a = 12
print(d, d['a'])
if __name__ == '__main__':
	import doctest
	doctest.testmod()

# test
def fact(n):
	'''
	>>> fact(-1)
	Traceback (most recent call last):
		...
	ValueError
	>>> fact(2 + 3)
	120
	>>> fact(1)
	1
	>>> fact(1, 2)
	Traceback (most recent call last):
  		File "<stdin>", line 1, in <module>
	TypeError: fact() takes 1 positional argument but 2 were given
	'''
	if n < 1:
		raise ValueError()
	if n == 1:	
		return 1
	return n * fact(n - 1)

if __name__ == '__main__':
	import doctest
	doctest.testmod()
# python -m pydoc <modulename>