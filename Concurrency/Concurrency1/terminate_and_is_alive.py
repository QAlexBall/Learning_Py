from multiprocessing import Process
import time
import random


def task(name):
    print('% is piaoing' % name)
    time.sleep(random.randrange(2, 5))
    print('%s is piao end' % name)


if __name__ == '__main__':
    p1 = Process(target=task, args=('egon',))
    p1.start()

    p1.terminate()  # 关闭进程,不会立即关闭,所以is_alive查看结果可能还是存活
    print(p1.is_alive())  # True
    print('main')
    time.sleep(1)
    print(p1.is_alive())  # False

'''
➜  Concurrency1 git:(master) ✗ python terminate_and_is_alive.py 
True
main
True
➜  Concurrency1 git:(master) ✗ python terminate_and_is_alive.py
True
main
False
'''
