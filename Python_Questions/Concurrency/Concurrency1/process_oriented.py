import time
import random
from threading import Thread

def eat(name):
    print('%s eating' % name)
    time.sleep(random.randrange(1, 5))
    print('%s eat end' % name)

if __name__ == '__main__':
    t1 = Thread(target=eat, args=('jack', ))
    t1.start()
    print('main')