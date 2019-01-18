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
    
s = Singleton() # class initialized, but object not created
print("Object created", Singleton.get_instance())
s1 = Singleton()
'''
output:
__init__method called..
__init__method called..
Object created <__main__.Singleton object at 0x7fc6b7718550>
Instance already created: <__main__.Singleton object at 0x7fc6b7718550>
'''