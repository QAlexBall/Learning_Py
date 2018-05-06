'''
以__开头的,变为一个私有变量(private)
类似__xxx__, 是特殊变量, 不是private变量
_一个下划线开头的变量名, 这样的实例变量外部是可以访问的
但是, 按照约定俗成的规定, 虽然可以被访问,
 但是一般视为私有的, 不能随意访问
'''
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

# 双下划线开头例如__name, python解释器对外把__name变量变成了
# _Student__name, 所以任然可以使用_Student__name进行访问__name变量
# !!! 不同版本的python解释器可能会把__name改成不同的变量名

print(bart._Student__name)
bart._Student__score = 59
print(bart.get_score())