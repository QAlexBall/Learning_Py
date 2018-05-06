# 线程是操作系统直接支持的执行单元
# Python的线程是真正的Posix Thread, 不是虚拟出来的线程
# Python的标准库提供了两个模块: _thread和threading, 
# _thread是低级模块, threading是高级模块, 对_thread进行了封装
# 启动一个线程就是把一个函数传入并创建Thread实例, 然后调用start()开始执行
import time, threading

# 新线程执行的代码
def loop():
	print('thread %s is running...' % threading.current_thread().name)
	n = 0
	while n < 5:
		n = n + 1
		print('thread %s >>> %s' % (threading.current_thread().name, n))
		time.sleep(1)
	print('thread %s ended.' % threading.current_thread().name)
print('thread %s is running...' % threading.current_thread().name)
t = threading.Thread(target=loop, name='LoopThread')
t.start()
t.join()
print('thread %s ended.' % threading.current_thread().name)

