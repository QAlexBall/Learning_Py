def foo():
	r = some_function()
	if r == (-1):
		return (-1)
	# do something
	return r
def bar():
	r = foo()
	if r == (-1):
		print('Error')
	else:
		pass

try:
	print('try...')
	r = 10 / 0
	print('result:', r)
except ZeroDivisionError as e:
	print('except:', e)
finally:
	print('finally...')
print('END')

try:
	print('try...')
	r = 10 / int('a')
	print('result:', r)
except ValueError as e:
	print('ValueError:', e)
except ZeroDivisionError as e:
	print('ZeroDivisionError:', e)
finally:
	print('finally...')
print('END')

try:
	print('try...')
	r = 10 / int('2')
	print('result:', r)
except ValueError as e:
	print('ValueError:', e)
except ZeroDivisionError as e:
	print('ZeroDivisionError:', e)
else:
	print('no error!')
finally:
	print('finally...')
print('END')

# python中的错误也是class, 所有的错误类型都继承自BaseException
 
# except不会捕捉到UnicodeError, UnicodeError是ValueError的子类.
# try:
# 	foo()
# except ValueError as e:
# 	print('ValueError')
# except UnicodeError as e:
# 	print('UnicodeError')

# def foo(s):
# 	return 10 / int(s)
# def bar(s):
# 	return foo(s) * 2
# def main():
# 	try:
# 		bar('0')
# 	except Exception as e:
# 		print('Error:', e)
# 	finally:
# 		print('finally...')
# main()

# 如果错误没有被捕获, 它就会一直往上抛, 最后被python解释器捕获
# 打印一个错误信息, 然后推出程序
# python内置的logging模块可以非常容易的记录错误信息;
# 同样是出错, 程序答应玩错误信息后会据悉执行, 并正常退出
# logging还可以把错误记录到日志文件
# def main():
# 	bar('0')
# main()
# output:
# main()
# bar('0')
# return foo(s) * 2
# return 10 / int(s)
# ZeroDivisionError: division by zero
import logging
print('\n')
print('Using logging')
def main():
	try:
		bar('0')
	except Exception as e:
		logging.exception(e)
main()
print('END')

class FooError(ValueError):
	pass

def foo(s):
	n = int(s)
	if n == 0:
		raise FooError('invalid value: %s' % s)
	return 10 / n

foo('0')