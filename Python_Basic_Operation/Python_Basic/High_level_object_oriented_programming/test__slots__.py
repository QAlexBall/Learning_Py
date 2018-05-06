from types import MethodType
class Student(object):
	pass

def set_age(self, age):
	self.age = age

from types import MethodType
s = Student()
s.name = 'Alex'
print(s.name)
# 将set_age绑定给s, 其他对象无法使用
s.set_age = MethodType(set_age, s)
s.set_age(25)
print(s.age)

# 给class绑定方法后所有实例均可访问
def set_score(self, score):
	self.score = score
Student.set_score = MethodType(set_score, Student)

# 获取到的score是类的属性而不是实例的属性?
s.set_score(98)
print(s.score)
s1 = Student()
s1.set_score(99)
print(s.score, s.name, s.age)
print('>>>>>>>>>>', '\n')


# 限制实例的属性
# 例如只允许Student实例添加name和age属性
# 利用__slot__, 限制该class实例能添加的属性
class Student(object):
	__slots__ = ('name', 'age') # 用tuple定义允许绑定的属性名称

s = Student()
s.name = "Alex"
s.age =25
# s.score = 99
# print(s.score)
# output: AttributeError: 'Student' object has no attribute 'score'
print(s.name, s.age)

# 使用slots仅对当前类的实例起作用, 对其继承的子类不起作用
class GraduateStudent(Student):
	pass 
g = GraduateStudent()
g.score = 88
print(g.score)





