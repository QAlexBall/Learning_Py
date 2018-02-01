# 利用print()把可能有问题的变量打印出来
import logging
# logging允许制定记录信息的级别, 有debug, info, warning, error等几个级别
logging.basicConfig(level=logging.INFO)
print('\n')
print('using logging')
def foo(s):
	n = int(s)
	print('>>> n = %d' % n) # 打印可能有问题的变量
	return 10 / n

def main():
	try:
		foo('1')
	except Exception as e:
		logging.exception(e)
		# raise ZeroDivisionError('ZeroDivisionError error!')
main()

# 断言
# 凡是用print()来辅助查看的地方, 都可以用assert断言来代替
# 启动python解释器时可以用-O参数关闭assert.
print('\n')
def foo(s):
	n = int(s)
	assert n != 0, 'n is zero!' # assert
	# assert的意思是, 表达式n != 0应该是True, 否则, 根据程序运行的逻辑
	# 后面的代码会出错, 如果断言失败, assert语句本身就会抛出AssertionError
	return 10 / n

def main():
	try:
		foo('1')
	except Exception as e:
		logging.exception(e)
		# raise ZeroDivisionError('ZeroDivisionError error!')
main()

# logging
# 把print()替换成logging, logging不会抛出错误, 而且可以输出到文件
s = '1'
n = int(s)
logging.info('n = %d' % n)
print(10 / n)
