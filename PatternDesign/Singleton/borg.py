class Borg:
    __shared_state = {"1":"2"}
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
'''
output:
Borg Object 'b':  <__main__.Borg object at 0x7f05ec933a90>
Borg Object 'b1':  <__main__.Borg object at 0x7f05ec933b38>
Object State 'b': {'1': '2', 'x': 4}
Object State 'b1': {'1': '2', 'x': 4}
'''

class Borg1(object):
    _shared_state = {}
    def __new__(cls, *args, **kwargs):
        obj = super(Borg1, cls).__new__(cls, *args, **kwargs)
        obj.__dict__ = cls._shared_state
        return obj
    
    def test(self):
        print("test")

b2 = Borg1()
b2.test()
b3 = Borg1()
b2.x = 4
b3.a = 3


print("Borg2 Object 'b2': ", b2)
print("Borg3 Object 'b3': ", b3)
print("Object State 'b2':", b2.__dict__)
print("Object State 'b3':", b3.__dict__)
'''
output:
Borg1 Object 'b':  <__main__.Borg1 object at 0x7f05ec933ba8>
Borg1 Object 'b1':  <__main__.Borg1 object at 0x7f05ec933a90>
Object State 'b': {'x': 4}
Object State 'b1': {'x': 4}
'''