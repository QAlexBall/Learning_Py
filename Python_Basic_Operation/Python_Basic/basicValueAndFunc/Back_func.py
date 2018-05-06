def calc_sum(*args):
	ax = 0
	for n in args:
		ax = ax + n
	return ax

def lazy_sum(*args):
	def sum():
		ax = 0
		for n in args:
			ax = ax + n
		return ax
	return sum # 返回的不是求和结果而是求和函数
f = lazy_sum(1, 3, 5, 7, 9)
g = calc_sum(1,3, 5, 7, 9)
print('\n', f, '\n', f(), '\n', g)
f1 = lazy_sum(1, 3, 5, 7, 9)
f2 = lazy_sum(1, 3, 5, 7, 9)
print('\n', f1 == f2)

def count():
	fs = []
	for i in range(1, 4):
		def f():
			return i*i
		fs.append(f)
	return fs
f1, f2, f3 = count()
print('\n', f1(), f2(), f3())

def count():
	def f(j):
		def g():
			return j*j
		return g
	fs = []
	for i in range(1, 4):
		fs.append(f(i))
	return fs
f1, f2, f3 = count()
print('\n', f1(), f2(), f3())
