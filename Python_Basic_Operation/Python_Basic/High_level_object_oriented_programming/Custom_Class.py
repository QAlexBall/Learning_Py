# 利用特殊用途的函数, 制作定制类
class Student(object):
	def __init__(self, name):
		self.name = name
print(Student('Alex'))

class Student(object):
	def __init__(self, name):
		self.name = name

	def __str__(self):
		return 'Student object (name: %s)' % self.name
s = Student('Alex')
print(s)
print(Student('Alex'))

class Student(object):
	def __init__(self, name):
		self.name = name

	def __str__(self):
		return 'Student object (name: %s)' % self.name

	__repr__ = __str__

s1 = Student('Adam')
print(Student('Alex'))
print(s1)

class Fib(object):
	def __init__(self):
		self.a, self.b = 0, 1

	def __iter__(self):
		return self # 实例本身即是迭代对象, 返回自己

	def __next__(self):
		self.a, self.b = self.b, self.a + self.b
		if self.a > 100:
			raise StopIteration()
		return self.a

for n in Fib():
	print(n)
s = Fib()
print(s.__next__)

#__getitem__()
class Fib(object):
	def __getitem__(self, n):
		a, b = 1, 1
		for x in range(n):
			a,b = b, a + b
		return a
f = Fib()
print(f[0])
print(f[10])

print(list(range(100)[5:10]))
# print(f(range(100)[5:10])) 
# output : TypeError: 'Fib' object is not callable

class Fib(object):
	def __getitem__(self, n):
		if isinstance(n, int):
			a, b = 1, 1
			for x in range(n):
				a, b = b, a + b
			return a
		if isinstance(n, slice):
			start = n.start
			stop = n.stop
			if start is None:
				start = 0
			a, b = 1, 1
			L = []
			for x in range(stop):
				if x >= start:
					L.append(a)
				a,b = b, a + b
			return L
f = Fib()
print(f[0:5])

# 与getitem对应的有__setitem__()方法, 把对象视作list或dict来对集合赋值
# __delitem__(), 用于删除某个元素


# __getattr__(), 为了避免找不到attribute, 
# 可以写一个__getattr__()函数, 动态返回一个属性
class Student(object):

	def __init__(self):
		self.name = 'Alex'

	def __getattr__(self, attr):
		if attr == 'score':
			return 99
		if attr == 'age':
			return lambda: 25

s = Student()
print(s.name, s.score) # before use __gettattr__() output: 
					   # AttributeError: 'Student' object has no attribute 'score'
print(s.age, s.age())

class Student(object):

	def __getattr__(self, attr):
		if attr == 'age':
			return lambda: 25
		raise AttributeError('\'Studnent\' object has no attribute \'%s\' nonono' %attr)

s = Student()
print(s.age)

# 利用完全动态__getattr__, 写一个链式调用
class Chain(object):

	def __init__(self, path=''):
		self._path = path

	def __getattr__(self, path):
		return Chain('%s%s' % (self.path, path))

	def __str__(self):
		return self._path

	__repr__ = str

print(Chain())

# 任何一个类, 只需要定义一个__call__()方法, 就可以直接对实例进行调用
class Student(object):
	def __init__(self, name):
		self.name = name
	def __call__(self):
		print('My name is %s' % self.name)
s = Student('Alex')
s()

# 判断一个对象是否能被调用
# 能被调用的对象就是一个callable的类实例
print(callable(Student('Alex')), callable(max), callable(s), callable(Chain()))
