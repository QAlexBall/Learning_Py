from hello import Hello
h = Hello()
h.hello()
print(type(Hello))

# type函数既能返回一个对象的类型, 又可以创建出新的类型
# 可以通过type()函数创建出Hello类, 无需通过class
def fn(self, name='world'):
	print('Hello, %s.' % name)
Hello1 = type('Hello', (object,), dict(hello=fn))
h1 = Hello1()
h1.hello()
print(type(h1))
# 要创建一个class对象, type()函数要依次传入三个参数:
# 1. class的名称
# 2. 继承的父类集合, 如果只有一个父类, tuple的单元素写法
# class的名称与函数绑定
# 通过type()函数创建的类和直接写class是完全一样的, 因为python解释器
# 遇到class定义时, 仅仅是扫描一下class定义的语法, 然后调用type()函数创建出class
# type函数允许动态创建类, 动态语言本身支持运行期间创建类

# 除了使用type()动态创建类以外, 还可以使用metaclass, 直译为元类
# 就是当我们定义了类以后, 就可以根据这个类创建出实例.先定义metaclass就可以创建出类,
# 最后创建实例,可以把类看成metaclass创建出来的实例
# 
# 
# metaclass是类的模板, 所以必须从'type'类型派生
class ListMetaClass(type):
	def __new__(cls, name, bases, attrs):
		attrs['add'] = lambda self, value: self.append(value)
		return type.__new__(cls, name, bases, attrs)
class MyList(list, metaclass=ListMetaClass):
	pass
# __new__()方法接收到的参数依次是
# 1. 当前准备创建的类的对象
# 2.类的名字
# 3.类继承的父类集合
# 4.类的方法集合
class Dog(list, metaclass=ListMetaClass):
	def eat(self):
		print('dog is eating...')
dog = Dog()
print(dog)
dog.add(1)
dog.add(2)
print(dog)
L= MyList()
L.add(1)
L.add(2)
print(L)
# 函数type实际上是一个元类


