'''
如果主进程的任务在执行到某一阶段时,需要等待子进程执行完毕后才能继续执行,
就需要一种机制能够让主进程检测子进程是否运行完毕,在子进程运行完毕后才继续
执行,否则一致在原地阻塞,这就是jion的用法.
'''
from multiprocessing import Process
import time
import random
import os

def task():
    print('% is piaoing' % os.getpid())
    time.sleep(random.randrange(1, 3))
    print('%s is piao end' % os.getpid())

if __name__ == '__main__':
    p = Process(target=task)
    p.start()
    p.join() # 等待p停止,才执行下一行代码
    print('main')