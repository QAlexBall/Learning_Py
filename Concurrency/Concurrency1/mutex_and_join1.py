# 执行前修改db.txt中count数量
from multiprocessing import Process, Lock
import json
import time

def search(name):
    time.sleep(1)
    with open('db.txt', 'r', encoding='utf-8') as f:
        dic = json.load(f)
        print('<%s> find tickets [%s]' % (name, dic['count']))

def get(name):
    time.sleep(1)
    dic = json.load(open('db.txt', 'r', encoding='utf-8'))
    if dic['count'] > 0:
        dic['count'] -= 1
        time.sleep(3)
        json.dump(dic, open('db.txt', 'w', encoding='utf-8'))
        print('<%s> success!' % name)
    else:
        print('fail')

def task(name, mutex):
    search(name)
    mutex.acquire()
    get(name)
    mutex.release()

if __name__ == "__main__":
    mutex = Lock()
    for i in range(5):
        p = Process(target=task, args=('user%s' % i, mutex))
        p.start()
