# -*- coding: utf-8 -*-
# 一个完整的decorator例子
'''
返回的那个wrapper()函数名字就是'wrapper'，
所以，需要把原始函数的__name__等属性复制到wrapper()函数中，
否则，有些依赖函数签名的代码执行就会出错。
不需要编写wrapper.__name__ = func.__name__这样的代码，
Python内置的functools.wraps就是干这个事的
'''

import functools

class Foo(object):
	def __init__(self, func):
		self._func = func

	def __call__(self):
		print ('class decorator runing')
		self._func()
		print ('class decorator ending')

@Foo
def bar():
	print('bar')
bar()


def foo(name, age=None, height=None):
    print("I am %s, age %s, height %s" % (name, age, height))

def log(func):
	@functools.wraps(func)
	def wrapper(*args, **kw):	
		#print('call %s():' % func.__name__)
		print('in log', args[0], args[1], args[2])
		print(**kw)
		#print(func(*args, **kw))
		return func(*args, **kw)
	# wrapper()
	return wrapper

@log
def now(n=0, c=2, func_name='now', func_tools='log', d={'a':1}):
	print(n, c, func_name, func_tools, d)
	print('2018-05-19')
now(3, 0, 'now', 'hello', {'a':1, 'b':2, 'c':3})


def time_this(original_function): 
    def new_function(*args, **kwargs):
        import datetime 
        before = datetime.datetime.now() 
        x = original_function(*args, **kwargs) 
        after = datetime.datetime.now() 
        print("Elapsed Time = {}".format(after-before)) 
        return x 
    return new_function
@time_this
def func_a(stuff): 
    import time 
    time.sleep(stuff) 
func_a(0)


import functools
def log(func):
	@functools.wraps(func) # 如果没有这一行, 则print(now.__name__输出为wrapper)
	def wrapper(*args, **kw):
		print('call %s():' % func.__name__)
		return func(*args, **kw)
	return wrapper
@log
def now():
	print('2015-3-25')	
now()
print(now.__name__)

def log(text):
	def decorator(func):
		#@functools.wraps(func)
		def wrapper(*args, **kw):
			print('%s, %s():' % (text, func.__name__))
			return func(*args, **kw)
		return wrapper
	return decorator
@log('DEBUG')
def now():
	print('2015-3-25')
now()
print(now.__name__)

'''
input:
	call now():
	2015-3-25
	wrapper 
	[Finished in 0.1s]
'''



def now():
	print('2015-3-25')
f = now
print(f(), now.__name__, f.__name__)

def log(func):
	# wrapper的参数定义是(*args, **kw), 因此, wrapper()函数可以接受任意参数的调用
	def wrapper(*args, **kw):
		print('call %s():' %func.__name__)
		return func(*args, **kw)
	return wrapper

@log 
def now():
	print('2015-3-25')
now()
print()

def log(text):
	def decorator(func):
		def wrapper(*args, **kw):
			print('%s, %s():' % (text, func.__name__))
			return func(*args, **kw)
		return wrapper
	return decorator
@log('execute') # 返回decorator
def now():
	print('2015-3-26')
now() # now 作为返回的wrapper函数
print(now.__name__)
print(log('execute')(now)())

print()
now = log('execute')(now)
print(now(), now.__name__)

print()
now = log('execute')
print(now)


print()
def now1():
    print('hello, world!')
print(now)          # <function log.<locals>.decorator at 0x7efd2c9a3510>
print(now(now1))    # <function log.<locals>.decorator.<locals>.wrapper at 0x7f52684af950>
print(now(now1)())
print(log('execute')(now1)())

