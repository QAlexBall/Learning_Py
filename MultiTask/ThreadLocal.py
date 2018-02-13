# ThreadLocal最常用于每个线程绑定一个数据库连接, HTTP请求, 用户身份信息等.HTTP请求
# ThreadLocal解决了参数在一个线程中各个函数之间互相传递的问题

# 在多线程环境下, 每个线程都有自己的数据. 
# 一个线程使用自己局部变量比使用全局变量要好, 
# 不会影响其他线程, 而且全局变量的修改需要加锁, 
# 但是局部变量在参数调用时, 传递麻烦
# example
def process_student(name):
	std = Student(name)
	# std是全局变量, 但是每个函数都要用它, 因此必须传入;
	do_task_1(std)
	do_task_2(std)
def do_task_1(std):
	do_subtask_1(std)
	do_subtask_2(std)
def do_task_2(std):
	do_subtask_1(std)
	do_subtask_2(std)

# example use dict
# 利用一个全局dict存放所有的Student对象, 
# 然后以thread自身作为key获得线程对应的Student对象
# 消除了std对象在每层函数中的转递问题
global_dict = {}

def std_thread(name):
	std = Student(name)
	# 把std放到全局变量global_dict中;
	global_dict[threading.current_thread()] = std
	do_task_1()
	do_task_2()
def do_task_1():
	# 不传入std, 而是根据当前线程查找
	std = global_dict[threading.current_thread()]
def do_task_2():
	# 任何函数都可以查找出当前进程的std变量
	std = global_dict[threading.current_thread()]

# ***** ThreadLocal *****
import threading

# 创建全局ThreadLocal对象
local_school = threading.local()

def process_student():
	# 获取当前线程关联的student;
	std = local_school.student
	print('Hello, %s (in %s)' % (std, threading.current_thread().name))
def process_thread(name):
	# 绑定ThreadLocal的student:
	local_school.student = name
	process_student()
t1 = threading.Thread(target=process_thread, args=('Alice',), name='Thread-A')
t2 = threading.Thread(target=process_thread, args=('Bob',), name='Thread-B')
t1.start()
t2.start()
t1.join()
t2.join()
# 全局变量local_school就是一个ThreadLocal对象, 每个Thread对它都可以读写student属性
# 但互不影响. 可以把local_school看成全局变量, 但每个属性如local_school.student
# 都是线程的局部变量, 可以任意读写互补干扰, 也不用管理锁问题, Thread内部处理
