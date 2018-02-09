# Unix/Linux 提供一个fork()函数调用, 普通函数调用调用一次返回依次
# fork()调用一次返回两次, 因为操作系统把当前进程(父进程)复制一份(子进程)
# 然后分别在父进程和子进程内返回, 子进程永远返回0, 父进程返回子进程的ID
# Python的os模块里封装了常见的系统调用, 其中就包括fork

'''
import os
print('Process (%s) start...' % os.getpid())
# Only works on Unix/Mac:
# pid = os.fork()
# if pid == 0:
# 	print('I am child Process (%s) and my parents is %s.'
# 	 % (os.gepid(), os.getppid))
# else:
# 	print('I (%s) just create a child process (%s).' 
# 		% (os.getpid(), pid))

# multiprocessing 模块是跨平台版本的多进程模块
# multiprocessing模块提供了一个Process类来代表一个进程对象


from multiprocessing import Process
import os
# child process
def run_proc(name):
	print('Run child process %s (%s)...' % (name, os.getpid()))

if __name__	== "__main__":
	print('Parents process %s.' % os.getpid())
	p = Process(target=run_proc, args=('run_proc',)) # 传入执行函数和函数的参数(args)
	print('Child process will start.')
	# 创建一个Process实例, 用start()启动, 
	p.start()
	p.join() # join()可以等待子进程及术后继续往下运行, 通常用于进程间的同步
	print('Child process end.')
'''

# 如果要起启动大量的子进程, 可以用进程池的方式批量创建子进程
'''
from multiprocessing import Pool
import os, time, random

def long_time_task(name):
	print('Run task %s (%s)...' % (name, os.getpid()))
	start = time.time()
	time.sleep(random.random() * 3)
	end = time.time()
	print('Task %s runs %0.2f seconds.' % (name, (end - start)))

if __name__ == '__main__':
	print('Parent Process %s.' % os.getpid())
	p = Pool(4)
	for i in range(5):
		p.apply_async(long_time_task, args=(i,))
	print('Waiting for all subprocesses done...')
	p.close()
	time.sleep(5)
	# p.join() 	# 对Pool对象调用join()方法会等待所有子进程执行完毕,
				# 调用join()之前必须先调用close(), 调用close()之后不能继续添加新的Process
	print('All subprocesses done.')

'''
# subprocess模块启动一个子进程, 并控制其输入输出
'''
import subprocess
print('$ nslookup www.python.org')
r = subprocess.call(['nslookup', 'www.python.org'])
print('exit code:', r)

# 如果需要子进程输入, 可以用communicate()方法
import subprocess
print('$ nslookup')
p = subprocess.Popen(['nslookup'], stdin=subprocess.PIPE,
	stdout=subprocess.PIPE, stderr=subprocess.PIPE)
output, err = p.communicate(b'set q=mx\npython.org\nexit\n')
print(output.decode('GBK')) # utf-8 err
print('Exit code:', p.returncode)

'''
# Process之间需要通信, 操作系统提供了很多机制来实现进程间的通信
# Python的mutiprocessing模块包装了底层的机制, 提供了, Queue, pipes等多种方式来交换数据

# 在父进程中创建两个子进程, 一个往Queue里写数据, 一个从Queue里读数据
from multiprocessing import Process, Queue
import os, time, random

# write
def write(q):
	print('Process to write: %s' % os.getpid())
	for value in ['A', 'B', 'C']:
		print('Put %s to queue...' % value)
		q.put(value)
		time.sleep(random.random())
# read
def read(q):
	print('Process to read: %s' % os.getpid())
	while True:
		value = q.get(True)
		print('Get %s from queue.' % value)
if __name__ == "__main__":
	# 父进程创建Queue, 并传给各个子进程
	q = Queue()
	pw = Process(target=write, args=(q, ))
	pr = Process(target=read, args=(q, ))
	pw.start()
	pr.start()
	pw.join()
	pr.terminate()