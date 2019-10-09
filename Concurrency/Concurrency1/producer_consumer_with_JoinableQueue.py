'''
JoinableQueue([maxsize]),这就像一个Queue对象,但队列允许项目的使用者通知生成者
项目已经被成功处理.通知进程是使用共享信号和条件变量来实现的.
'''

from multiprocessing import Process, JoinableQueue
import time


def producer(q, name):
    for i in range(3):
        res = 'baozi %s' % i
        time.sleep(1)
        print('%s producer %s' % (name, res))
        q.put(res)
    q.join()  # 接收到task_done的信号后,等待消费者把自己放入队列中的所有数据都取走,生产者才结束


def consumer(q, name):
    while True:
        time.sleep(2)
        res = q.get()
        print('%s consumer %s' % (name, res))
        q.task_done()  # 发送信号给q.join(),说明已经从队列中取走一个数据并处理了


if __name__ == "__main__":
    q = JoinableQueue()

    p1 = Process(target=producer, args=(q, 'p1'))
    p2 = Process(target=producer, args=(q, 'p2'))

    c1 = Process(target=consumer, args=(q, 'c1'))
    c2 = Process(target=consumer, args=(q, 'c2'))
    c1.daemon = True
    c2.daemon = True

    p1.start()
    p2.start()
    c1.start()
    c2.start()

    p1.join()
    p2.join()
    print('main')
