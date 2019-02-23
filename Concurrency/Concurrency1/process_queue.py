'''
进程间批次之间互相隔离,要实现进程间通信(IPC),multiprocessing模块
支持两种形式: 队列和管道,这两种方式都是使用消息传递的.
创建队列的类(底层就是以管道和锁定的方式实现的):
Queue([maxsize]): 创建共享的进程队列,Queue是对进程安全的队列,可以使用Queue
实现多进程之间的数据传递.
'''

from multiprocessing import Process, Queue 
import time

q = Queue(3)

q.put(3)
q.put(3)
q.put(3)
print(q.full())

print(q.get()) # FIFO
print(q.get())
print(q.get())
print(q.empty())

'''
➜  Concurrency1 git:(master) ✗ python process_queue.py 
True
3
3
3
True
'''