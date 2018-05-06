'''
如果要获得一个对象的所有属性和方法, 可以使用dir()函数, 
它返回一个包含字符串的list, 比如, 获得一个str对象的所有属性和方法

hasattr测试该对象的属性
setattr设置一个属性
getattr获取属性 getattr(obj, 'y')相当于obj.y
'''
a = 'ABC'
print(dir('ABC'), '\n',
 	len('ABC'), 'ABC'.__len__())
print('ABC'.__eq__(a), 'ABC'.__format__('123')) # output: True

class MyDog(object):
	def __init__(self, len=10, eat='meat'):
		self.__len = len
		self.__eat = eat
	def __len__(self):
		return self.__len
	def eat(self):
		return self.__eat

dog = MyDog(15)
dog1 = MyDog(10,'rice')
print(len(dog), len(dog1), '\n',
	dog.eat(), dog1.eat())





class Animal(object):
	def run(self):
		print('Animal is running...')
class Dog(Animal):
	def run(self):
		print('Dog is running...')
	def eat(self):
		print('Eating mear...')
class Cat(Animal):
	def run(selg):
		print('Cat is running...')
a = list()
b = Animal()
c = Dog()
print(type(123), type('str'))
print(type(abs))
print(type(b), type(a), type(c))
print(type(123) == int, 
	type('b') == type(c),
	type('abc') == type('123')) 

# 判断一个对象是否是函数
import types
def fn():
	pass
print(type(fn) == types.FunctionType, 
	type(lambda x: x) == types.LambdaType,
	type(abs) == types.BuiltinFunctionType, 
	type((x for x in range(10))) == types.GeneratorType)

class Husky(Dog):
	pass
a = Animal()
d = Dog()
h = Husky()
print('\n',
	isinstance(h, Husky),
	isinstance(h, Dog), isinstance(h, Animal), '\n', 
	isinstance(b'a', bytes), isinstance([1, 2, 3], (list, tuple)),
	isinstance((1, 2, 3), (list, tuple)))
print('\n', 
	'\n',
	'\n')



class MyObject(object):
	def __init__(self):
		self.x = 9
	def power(self):
		return self.x * self.x
obj = MyObject()
print(hasattr(obj, 'x'), hasattr(obj, 'y'), setattr(obj, 'y', 19), hasattr(obj, 'y'))
print(obj.y, getattr(obj, 'y'))
print(getattr(obj, 'z', 404))
print(hasattr(obj, 'power'),
	getattr(obj, 'power'))
fn = getattr(obj, 'power')
print(fn(), obj.power())
# 只有不知道对象信息的时候, 操去获取对象信息
# example
def readImage(fp):
	if(hasattr(fp, 'read')):
		return readData(fp)
	return None
print(readImage(obj))