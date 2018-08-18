# Lock
# 锁能确保某段关键代码只能由一个线程从头到尾执行
# 但是阻止了多线程并发执行, 包含锁的某段代码实际上只能以单线程模式执行
# 由于可以存在多个锁, 不同的线程持有不同的锁, 并试图获取对方持有的锁时, 会导致死锁 

# Python的线程虽然是真正的线程, 但是解释代码执行时,有一个GIL锁: Global Interpreter Lock
# 任何Python线程执行前, 必须获得GIL锁, 然后每执行100条字节码, 解释器就自动释放GIL锁
# 然别的线程有机会执行.这个GIL全局锁实际上把所有线程的执行代码都上了锁, 所以多线程在Python中智能交替执行


# 多线程和多进程最大的不同在于, 多进程中, 同一个变量, 各自有一份拷贝再每个进程中互不影响
# 多线程中, 所有变量都由所有线程共享, 所以, 任何一个变量都可以被任何一个线程修改.
# example

import time, threading
# 假定为个人银行存款:
balance = 0
lock = threading.Lock()

def change_it(n):
	# 先存后取, 结果应该为0
	global balance
	balance = balance + n
	balance = balance - n
def run_thread(n):
	for i in range(1000000):
		# 先获取锁:
		lock.acquire() # 当多个线程同时执行lock.acquire时只有一个线程能成功获取锁.
		try:
			change_it(n)
		finally:
			# 释放锁
			lock.release() # 用完后释放锁, 否则会造成死锁
		# print(threading.current_thread().name)
	# print(threading.current_thread().name)

t1 = threading.Thread(target=run_thread, args=(5,))
t2 = threading.Thread(target=run_thread, args=(8,))
t1.start()
t2.start()
t1.join()
t2.join()
print(balance) # output: 9


# 要使balance计算正确就要确保线程在修改balance是别的线程不能修改
# 给change_it()加锁, 通过创建threading.Lock实现


# 死循环
'''
import threading, multiprocessing

def loop():
	x = 0
	while True:
		x = x ^ 1
for i in range(multiprocessing.cpu_count()):
	t = threading.Thread(target=loop)
	t.start()
'''