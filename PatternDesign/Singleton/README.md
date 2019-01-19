# 单例设计模式

### 理解单例设计模式
单例模式提供了这样一个机制,确保类有且只有一个特定类型的对象,并**提供全局访问点**.
* 确保类有且仅有一个对象被创建
* 为队形提供一个访问点,以使程序可以全局访问该对象
* 控制共享资源的并行访问
单例模式UML图

![single.png](single.png)

实现单例模式的一个简单方法是,是构造函数私有化,并创建一个静态方法来完成对象的初始化.这样,对象在第一次调用时创建,此后,这个类返回同一个对象.

利用Python实现经典的单例模式
1. 只允许Singleton类生成一个实例
2. 如果已经有一个实例了,我们会重复提供同一个对象
```python
# singleton1.py
class Singleton(object):
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Singleton, cls).__new__(cls)
        return cls.instance
s = Singleton()
print("Object created", s)
s1 = Singleton()
print("Object created1", s1)
```
在上面代码中,我们通过覆盖__new__方法(Python用于实例化对象的特殊方法)来控制对象的创建.对象s就是由__new__方法但在创建之前,该方法会检查对象是否已存在.
方法hasattr(Python特殊方法,用来了解对象是否具有某个属性)用于查看对象cls是否具有属性instance,该属性的作用是检查cls是否具有属性instance,该属性的作用是检查gailei是否已经生成了一个对象.当对象是
被请求的时候,hasattr()发现对象已经存在,所以,对象是被分配已有的对象实例.

### 单例设计模式中的懒汉式实例化
单例模式的用例之一就是懒汉式实例化.例如,在导入模块的时候,我们可能会无意中创建一个对象,但当时根本用不到它.懒汉模式实例化能够确保在实际需要时才创建对象.所以,懒汉式实例化是一种节约资源并仅在需要时才创建它们的方式.
```python
class Singleton:
    __instance = None
    def __init__(self):
        if not Singleton.__instance:
            print("__init__method called..")
        else:
            print("Instance already created:", self.get_instance())
    
    @classmethod
    def get_instance(cls):
        if not cls.__instance:
            cls.__instance = Singleton()
        return cls.__instance

s = Singleton()
print("Object created", Singleton.get_instance())
s1 = Singleton()
'''
output:
__init__method called..
__init__method called..
Object created <__main__.Singleton object at 0x7fc6b7718550>
Instance already created: <__main__.Singleton object at 0x7fc6b7718550>
'''
```
执行s = Singleton()时,它会调用__init__方法,但是没有新的对象被创建.然而,实际的对象创建发生在调用Singleton.get_instance()的时候,我们正式通过这种方式来实现懒汉式实例化的.

### Monostate单例模式
```python
class Borg:
    __shared_state = {"1":"2"}  # 双下划线表示类中私有变量
    def __init__(self):
        self.x = 1
        self.__dict__ = self.__shared_state
        pass
    
b = Borg()
b1 = Borg()
b.x = 4

print("Borg Object 'b': ", b)
print("Borg Object 'b1': ", b1)
print("Object State 'b':", b.__dict__)
print("Object State 'b1':", b1.__dict__)
'''output
➜  Singleton git:(master) ✗ python borg.py
Borg Object 'b':  <__main__.Borg object at 0x7fb8b8642b00>
Borg Object 'b1':  <__main__.Borg object at 0x7fb8b8642b38>
Object State 'b': {'1': '2', 'x': 4}
Object State 'b1': {'1': '2', 'x': 4}
'''
```
我们将类变量 __shared_state赋给了变量__dict__(它是Python的一个特殊变量).Python使用__dict__存储一个类所有对象的状态.在这段代码中,我们故意把__shared_state赋给所有已经创建的实例.随意,如果创建了两个实例"b"和"b1",我们将得到两个不同的对像,这一点和单例模式大为不同,后者只能生成一个对象.然而,对象的状态,即b.__dict__和b1.__dict__却是相同的.现在就算对象b的对象变量x发生了变化,这个变化也会被复制到所有对象共享的__dict__变量.

除此之外，我们还可以通过修改__new__方法本身来实现Borg模式.我们知道__new__方法是用来创建对象实例的.具体如下所示:
```python
class Borg1(object):
    _shared_state = {}
    def __new__(cls, *args, **kwargs):
        obj = super(Borg1, cls).__new__(cls, *args, **kwargs)
        obj.__dict__ = cls._shared_state
        return obj
```

### 单例和元类
元类是一个类的类,这意味着该类是它的元类的实例.使用元类,程序员有机会从预定义的Python类创建自己类型的类.在Python中一切皆对象.类的定义由它的元类决定.
当我们用类A创建一个类时,Python通过A=type(name, bases, dict)创建它们,让我们看一下Python中的一个实例元类的实现
```python
class MyInt(type):
    def __call__(cls, *args, **kwargs):
        print("******** Here's My int ********", args)
        print("Now do whatever you want with these objects...")
        return type.__call__(cls, *args, **kwargs)

class int(metaclass=MyInt):
    def __init__(self, x, y):
        self.x = x
        self.y = y

i = int(3, 5)
print(i)
'''
output:
******** Here's My int ******** (3, 5)
Now do whatever you want with these objects...
<__main__.int object at 0x7f366e347b38>
'''
```
对于已经存在的类来说,当需要创建对象时,将调用Python的特殊方法__call__.这段代码中,当我们使用int(3, 5)实例化int类时,
MyInt元类的__call__方法将被调用,这意味着现在元类控制着对象的实例化.

前面的思路同样适用于单例设计模式.由于元类对类创建和对象实例化有更多的控制权,所以它可以用于创建单例.(注意:为了控制类的创建和初始化,元类将覆盖__new__和__init__方法.)
```python
class MetaSingleton(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(MetaSingleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]

class Logger(metaclass=MetaSingleton):
    pass

logger1 = Logger()
logger2 = Logger()
print(logger1, logger2)
'''
output:
<__main__.Logger object at 0x7fd9c7668e80> <__main__.Logger object at 0x7fd9c7668e80>
'''
```

单例模式用于多个服务间实现一致的数据库操作
```python
class HealthCheck:
    _instance = None
    def __new__(cls, *args, **kwargs):
        if not HealthCheck._instance:
            HealthCheck._instance = super(HealthCheck, cls).__new__(cls, *args, **kwargs)
        return HealthCheck._instance

    def __init__(self):
        self._servers = []
    
    def add_server(self):
        self._servers.append("Server 1")
        self._servers.append("Server 2")
        self._servers.append("Server 3")
        self._servers.append("Server 4")
    
    def change_server(self):
        self._servers.pop()
        self._servers.append("Server 5")

hc1 = HealthCheck()
hc2 = HealthCheck()
print(hc1, hc2)

hc1.add_server()
print("Schedule heath check for servers (1)..")

for i in range(4):
    print("Checking ", hc1._servers[i])

hc2.change_server()
print("Schedule health check for servers (2)..")
for i in range(4):
    print("Checking ", hc2._servers[i])
```

### 单例模式的缺点
* 全局变量可能在某处已经被误改,但是开发人员仍然认为它们没有发生变化,而该变量还在应用程序的其他位置被使用.
* 可能会对同一对象创建多个引用.由于单例只创建一个对象,因此这种情况下会对同一个对象创建多个引用.
* 所有依赖于全局变量的类都会由于一个类的改变而紧密耦合为全局数据,从而可能在无意中影响另一个类.

