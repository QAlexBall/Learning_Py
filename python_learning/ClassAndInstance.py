class Student(object):
	pass
bart = Student()
print('\n', bart, '\n', Student)

bart.name = 'Bart Simpson'
print(bart.name)


class Student(object):

	def __init__(self, name, score):
		self.name = name
		self.score = score

	def print_socre(self):
		print('%s: %s' % (self.name, self.score))

	def get_grade(self):
		if self.score >= 90:
			return 'A'
		elif self.score >= 60:
			return 'B'
		else:
			return 'C'
bart = Student('Bart Simpson', 59)
print(bart.name, ': ', bart.score)
bart.print_socre()
print(bart.get_grade())

'''
访问限制
在class内部, 可以有属性和方法, 而外部代码可以通过直接调用实例变量的方法
来操作数据, 便有了隐藏内部的复杂逻辑
'''
bart = Student('Bart Simpson', 58)
print(bart.score)

class Student(object):

	def __init__(self, name, score):
		self.__name = name
		self.__score = score

	def set_name(self, name):
		self.__name = name
	def get_name(self):
		return self.__name
	def set_score(self, score):
		if 0 <= score <= 100:
			self.__score = score
		else:
			raise ValueError('bad score')
	def get_score(self):
		return self.__score

	def print_score(self):
		print('%s: %s' % (self.__name, self.__score))

bart = Student('Bart Simpson', 58)
bart.print_score()
bart.set_score(60)
# bart.set_score(-60) output: ValueError: bad socre
bart.print_score()
