def count():
    fs = []
    for i in range(1, 4):
        def f():
             print(i)
             return i * i
        fs.append(f)
    return fs 		# fs = [function f1, function f2, function f3]

f = count()
print(f)

f1, f2, f3 = count()	# 返回的函数引用了变量i,等到3个函数都返回时,i变成了3,再调用f函数结果为9
						# 执行f(): i = 3
print(f1, f1()) # <function count.<locals>.f at 0x7f8e29b71950> 9


def count1():
	def f(j):
		def g():
			return j * j;
		return g
	fs = []
	for i in range(1, 4):
		fs.append(f(i))	# f(i)立即被执行,因此i的当前值被传入f()	
	return fs

f1, f2, f3 = count1() # 执行f(j): f(1), f(2), f(3)
print(f1, f1()) # <function count1.<locals>.f.<locals>.g at 0x7f8e29b71bf8> 1


# 利用闭包返回一个计数器函数,每次调用它返回递增整数
def createCounter():
	n = 0
	def counter():
		nonlocal n
		n += 1
		return n
	return counter
counterA = createCounter()
print(counterA(), counterA())

def createCounter():
	def _next():
		i = 1
		while True:
			yield i
			i += 1
	g = _next()
	def counter():
		return next(g)
	return counter
counterA = createCounter()
print(counterA(), counterA())

	
