class RunnableMaxIn(object):
	def run(self):
		print(self.name, 'is', end='')
		print('Running...')
class FlyableMaxIn(object):
	def fly(self):
		print(self.name, 'is', end='')
		print('flying....')

class Animal(object):
	def __init__(self, name):
		self.name = name



class Mammal(Animal):
	pass
class Bird(Animal):
	pass


# 对于需要Runnable功能的类, 多继承一个Runnable
# '混入'额外的功能, 例如runnable, 通过多重继承就可以实现
# 这种设计通常被称为MixIN
# 为了更好的看出继承关系, 可以用RunnableMaxIn代替Runnable, 
# 可以让一个类拥有多种MaxIn
class Dog(Mammal, RunnableMaxIn):
	pass
class Bat(Mammal, FlyableMaxIn, RunnableMaxIn):
	pass

class Parrot(Bird, FlyableMaxIn):
	pass
class Ostrich(Bird, RunnableMaxIn):
	pass

d = Dog(name='dog')
d.run()
o = Ostrich(name='ostrich')
o.run()
b = Bat('bat')
b.fly()
b.run()
