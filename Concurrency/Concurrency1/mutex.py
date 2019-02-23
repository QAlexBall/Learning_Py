'''
互斥锁:把并发改成串行,降低了效率,但是保证了数据安全不乱
'''
from multiprocessing import Process, Lock
import time

def task(name, mutex):
    mutex.acquire()
    print('%s 1' % name)
    time.sleep(1)
    print('%s 1' % name)
    time.sleep(1)
    print('%s 1' % name)
    time.sleep(1)
    mutex.release()

if __name__ == "__main__":
    mutex = Lock() # 实例化得到互斥锁
    for i in range(3):
        p = Process(target=task, args=('process%s' % i, mutex)) # 传入子进程
        p.start()
