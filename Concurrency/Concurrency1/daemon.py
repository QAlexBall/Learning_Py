'''
如果我们有两个任务需要并发执行,那么开一个主进程和一个子进程分别去执行就可以了
如果子进程的任务在主进程任务结束后就没有存在的必要了,那么该子进程应该在开启前
就被设置程守护进程.主进程代码运行结束, 守护进程随即终止

* 守护进程会在主进程代码执行结束后就终止
* 守护进程内无法再开启子进程,否则抛出异常:
AssertionError: daemonic processes are not allowed to have children
'''
from multiprocessing import Process
import time
import random

def task(name):
    print('%s is piaoing' % name)
    time.sleep(random.randrange(1, 3))
    print('%s is piao end' % name)

if __name__ == '__main__':
    p = Process(target=task, args=('egon', ))
    p.daemon = True # 一定要在p.start()前设置,设置p为守护进程,禁止p创建子进程,并且让父进程代码执行结束,p即终止运行
    p.start()
    time.sleep(1)
    print('main') #　只要终端打印出这一行内容，守护进程ｐ也就梗着结束了
    
'''
➜  Concurrency1 git:(master) ✗ python daemon.py 
main
➜  Concurrency1 git:(master) ✗ python daemon.py
egon is piaoing
main
'''