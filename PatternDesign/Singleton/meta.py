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