# 分布式进程
# 在Thread和Process中, 应当优选Process, 因为Process更加稳定, 
# 而且Process可以分布到多台机器上, 而Thread只能分布到同一台机器的多个CPU上
# 
# Python的multiprocessing模块中的managers子模块, 支持把多进程分不到多台机器上.
# 一个服务进程作为调度者, 将任务分布到其他多个进程中, 以来网络通信.
# 由于managers模块封装很好, 不必了解网络通信细节.
# 
# Example
# 有一个通过Queue通信的多进程程序在同一台机器上运行, 
# 希望把任务的进程和处理任务的分布到两台机器上
# 实现: 
# 原有Queue继续使用, 通过managers模块把Queue通过网络暴露出去, 其他机器即可访问.

# 服务进程负责启动Queue,把Queue注册到网络上, 然后往Queue里面写任务
import random, time, queue
from multiprocessing.managers import BaseManager

# 发送任务的队列
task_queue = queue.Queue()
# 接受任务的队列
result_queue = queue.Queue()

# 从BaseManager继承QueueManager
class QueueManager(BaseManager):
	pass

# 把两个Queue都注册到网络上, callable参数关联了Queue对象
QueueManager.register('get_task_queue', callable=lambda: task_queue)
QueueManager.register('get_result_queue', callable=lambda: result_queue)
# 绑定端口5000, 设置验证码'abc':
manager = QueueManager(address=('', 5000), authkey=b'abc')
# 启动Queue:
manager.start()
# 获得通过网络访问的Queue对象
task = manager.get_task_queue()
result = manager.get_result_queue()
# 放几个任务进去:
for i in range(10):
	n = random.randint(0, 10000)
	print('Put task %d...' % n)
	task.put(n)
# 从result队列读取结果:
print('Try get reuslt...')
for i in range(10):
	r = result.get(timeout=10)
	print('Result: %s' % r)
# 关闭:
manager.shutdown()
print('master exit')




import time, sys, queue
from multiprocessing.managers import BaseManager

# 创建类似的QueueManager:
class QueueManager(BaseManager):
    pass

# 由于这个QueueManager只从网络上获取Queue，所以注册时只提供名字:
QueueManager.register('get_task_queue')
QueueManager.register('get_result_queue')

# 连接到服务器，也就是运行task_master.py的机器:
server_addr = '127.0.0.1'
print('Connect to server %s...' % server_addr)
# 端口和验证码注意保持与task_master.py设置的完全一致:
m = QueueManager(address=(server_addr, 5000), authkey=b'abc')
# 从网络连接:
m.connect()
# 获取Queue的对象:
task = m.get_task_queue()
result = m.get_result_queue()
# 从task队列取任务,并把结果写入result队列:
for i in range(10):
    try:
        n = task.get(timeout=1)
        print('run task %d * %d...' % (n, n))
        r = '%d * %d = %d' % (n, n, n*n)
        time.sleep(1)
        result.put(r)
    except queue.Queue.Empty:
        print('task queue is empty.')
# 处理结束:
print('worker exit.')

# 计算密集型任务同时进行的数量应当等于CPU核心数, 最好用C编写
# 对于IO密集型的任务, 任务越多, CPU效率越高(有限度)
# 异步IO
# Python语言, 单进程的异步编程模型称为协程, 
# 有了协程的支持, 就可以基于事件驱动编写高效的多任务程序