from multiprocessing import Process
import time

class MyProcess(Process):

    def __init__(self, name):
        super().__init__()
        self.name = name

    def run(self): # 进程函数使用run表示
        print('%s is running' % self.name)
        time.sleep(3)
        print('%s is done' % self.name)

if __name__ == '__main__':
    p = MyProcess('subprocess1')
    p.start()

    print('main')