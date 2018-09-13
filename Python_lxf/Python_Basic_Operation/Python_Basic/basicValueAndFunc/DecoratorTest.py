# coding=utf-8
def log(text):
    def decorator(func):
        def wrapper(*args, **kw):
            print('%s, %s():' % (text, func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator

def now(a=0):
    print('2018, 8, 18', a)

a = log('execute')(now)(2)   # 先编译log('execute')(now)返回wrapper函数, 再执行wrapper
@log('execute') # 返回decorator
def now(a=0):
    print('2015-3-26', a)

a = log('execute')(now(1))   # 这里引用的now都已经加了修饰器
a = now() # now 作为返回的wrapper函数
print(log('execute')) # <function log.<locals>.decorator at 0x7f8e19412840>
print()

print(a)    # <function log.<locals>.decorator.<locals>.wrapper at 0x7f19a8c38488>


print()

print(log('execute')(now))  # <function log.<locals>.decorator.<locals>.wrapper at 0x7fd604ac4510>
a = log('execute')(now)(2)   # 先编译log('execute')(now)返回wrapper函数, 再执行wrapper, 也就是now,是加了修饰器的now
print(a)    # None

def hello():
    def decorator(func):
        def wrapper(*args, **kwargs):
            print('in, wrapper')
            func()
        return wrapper
    return decorator
@hello()
def hello1():
    print('hello1')

hello1()
hello()(hello1)()