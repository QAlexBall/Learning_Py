# 执行前修改db.txt中count数量
'''
使用join导致查票操作也变成单人了
'''
from multiprocessing import Process,Lock
import time,json

def search(name):
    dic = json.load(open('db.txt'))
    print('[%s 查到剩余票数%s' %(name, dic['count']))

def get(name):
    dic=json.load(open('db.txt'))
    time.sleep(1) #模拟读数据的网络延迟
    if dic['count'] > 0:
        dic['count'] -= 1
        time.sleep(1) #模拟写数据的网络延迟
        json.dump(dic, open('db.txt','w'))
        print('%s 购票成功' %name)

def task(name, ):
    search(name)
    get(name)

if __name__ == '__main__':
    for i in range(10):
        name='<路人%s>' %i
        p=Process(target=task,args=(name,))
        p.start()
        p.join()