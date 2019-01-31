class Actor(object):

    def __init__(self):
        self.is_busy = False

    def occupied(self):
        self.is_busy = True
        print(type(self).__name__, "is occupied with current movie")
    
    def available(self):
        self.is_busy = False
        print(type(self).__name__, "is free for the movie")
    
    def get_status(self):
        return self.is_busy

'''
代理设计模式主要完成了一下工作
* 它为其他对象提供了一个代理,从而实现了对原始对象的访问控制.
* 它可以作为一个层或接口,以支持分布式访问.
* 它通过增加代理,保护真正的组件不受意外的影响.
'''

class Agent(object):

    def __init__(self):
        self.principal = None
    
    def work(self):
        self.actor = Actor()
        if self.actor.get_status():
            self.actor.occupied()
        else:
            self.actor.available()

if __name__ == '__main__':
    r = Agent()
    r.work()