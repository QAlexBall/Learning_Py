print(int('12345'))
print(int('12345', base=8))
print(int('12345', base=16))
def int2(x, base=2):
	return int(x, base)
print(int2('11001'), '\n')


# functools.partial是帮助创建偏函数的
import functools
int2 = functools.partial(int, base=2)
print(int2('1001'))
kw = { 'base' : 2 } 
print(int('1010', **kw), '\n')

max2 = functools.partial(max, 10)
print(max2(5, 6, 29))
args = (29, 5, 6, 7, 10)
print(max(*args))

