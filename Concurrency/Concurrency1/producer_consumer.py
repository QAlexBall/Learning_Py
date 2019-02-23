from multiprocessing import Process, Queue
import time

def producer(q):
    for i in range(10):
        res = 'baozi%s' % i
        time.sleep(1)
        q.put(res)
        print('producer producing %s' % res)

def consumer(q):
    while True:
        time.sleep(2)
        res = q.get()
        if res == None:
            break
        print('consumer eat %s' % res)

if __name__ == "__main__":
    # container
    q = Queue()

    # producers
    p1 = Process(target=producer, args=(q, ))
    # consumers
    c1 = Process(target=consumer, args=(q, ))

    p1.start()
    c1.start()

    p1.join()
    q.put(None)

