class Student(object):
	name = 'Student'
s = Student()
print(s.name)
print(Student.name)
print('\n')

'''
在编写程序的时候, 不要把实例属性和类属性使用相同的名字,
相同的名字和实例属性将屏蔽掉类属性, 删除实例属性后,
在使用相同名称将会访问到类属性
'''
s.name = 'Alex'
print(s.name)
print(Student.name)
del s.name
print(s.name)
print('\n')

Student.name = 'Alex'
print(s.name)
print(Student.name)
