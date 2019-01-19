# 工厂模式

### 了解工厂模式
在面向对象编程中,术语"工厂"表示一个负责创建其他类型对象的类.通常情况下,作为一个工厂的类有一个对象以及与它关联的多个方法.客户端使用某些参数调用此方法,之后工厂会根据创建所需类型的对象,然后将它们返回给客户端.
工厂具有一下优点:
* 松耦合,即对象的创建可以独立于类的实现
* 客户端无需了解创建对象的类,但是照样可以使用它来创建对象.它只需要知道需要传递的接口,方法和参数,就能够创建所需类型的对象了.这简化了客户端的实现.
* 工厂还可以重用现有对象.但是,如果客户端直接创建对象的话,总是创建一个新的对象.

Factory模式有三种变体,如下所示.
* 简单工厂模式: 允许接口创建对象,但不会暴露对象的创建逻辑.
* 工厂方法模式: 允许接口创建对象,但使用哪个类来创建对象,则是交由子类决定的.
* 抽象工厂模式: 抽象工厂是一个能够创建一系列相关的对象而无需指定/公开其具体类的接口.该模式能够提供其他工厂的对象,在其内部创建其他对象.

###简单工厂模式
```python
# ForestFactory.py
from abc import ABCMeta, abstractmethod

class Animal(metaclass=ABCMeta):
    @abstractmethod
    def do_say(self):
        pass

class Dog(Animal):
    def do_say(self):
        print("Bhow Bhow!")

class Cat(Animal):
    def do_say(self):
        print("Meow Meow!")

## forest factory defined
class ForestFactory(object):
    def make_sound(self, object_type):
        return eval(object_type)().do_say()

## client code
if __name__ == '__main__':
    ff = ForestFactory()
    try:
        animal = input("Which animal should make_sound Dog or Cat?\n")
    
    ff.make_sound(animal)
```