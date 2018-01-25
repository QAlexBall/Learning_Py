__author__ = 'QAlexBall'
import sys

def test():
	args = sys.argv
	if len(args)==1:
		print('Hello world!')
	elif len(args)==2:
		print('Hello, %s!' % args[1])
	else:
		print('Too many arguments!')
if __name__ == '__main__':
	test()
#正常函数和变量名是公开的(public),
#可以直接被引用,
#类似于__xxx__这样的变量是特殊变量, 可以被直接引用,但是有特殊用途,
#比如__author__, __name__就是特殊变量, 
#类似__xxx__和__xxx遮掩的函数或变量就是非公开的(private), 不应该被直接引用
def _private_1(name):
	return 'Hello, %s' % name
def _private_2(name):
	return 'Hi, %s' % name
# 在模块里公开greeting函数, 而把内部逻辑private函数隐藏起来
def greeting(name):
	if len(name) > 3:
		return _private_1(name)
	else:
		return _private_2(name)
