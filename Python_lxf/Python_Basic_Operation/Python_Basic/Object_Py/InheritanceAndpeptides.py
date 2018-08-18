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
dog = Dog()
dog.run()
cat = Cat()
cat.run()

a = list()
b = Animal()
c = Dog()
print(isinstance(a, list), isinstance(b, Animal), isinstance(c, Dog))
print(isinstance(c, Animal), isinstance(c, list))

def run_twice(animal):
	animal.run()
	animal.run()
run_twice(Animal())
run_twice(Dog())
# Peptides
# 任何依赖Animal作为参数的函数或者方法都可以不加修改的正常运行
class Tortoise(Animal):
	def run(self):
		print('Tortoise is running slowly...')
run_twice(Tortoise())
'''
对于java,如果需要传入Animal类型, 则传入的对象必须是
Animal类型或者其子类, 否则无法调用run()方法
python动态语言, 不一定需要传入Animal类型, 只保证传入对象有run()方法
'''
class Timer(object):
	def run(self):
		print("Start...")
run_twice(Timer())
