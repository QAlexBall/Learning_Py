当代码需要执行一个耗时的IO操作时,它只发处IO指令(就去执行其他代码),并不等待IO结果,当IO返回结果时,再通知CPU进行处理

异步IO需要一个消息循环,在消息循环中,主线程不断地"读取消息-处理消息"这一过程

```python
loop = get_event_loop()
while True:
    event = loop.get_event()
    process_event(event)
```



##### 协程(Coroutine)

协程在执行过程中,在子程序内部可中断,然后转而执行别的子程序,在适当的时候再返回来接着执行

**在子程序中中断,再取执行其他子程序,不是函数调用,有点类似于CPU的中断**

```python
def A():
    print("1")
    print("2")
    print("3")
def B():
    print("x")
    print("y")
    print("z")
```

假设由协程去执行,在执行A的过程中,可以随时中断,去执行B,B也可能在执行过程中中断再去执行A,结果可能是

```shell
1
2
x
y
3
z
```

协程的特点在于是一个线程执行

##### 协程优势

* 极高的执行效率,没有线程切换开销
* 不需要多线程锁机制,因为只有一个线程,也不存在同时写变量冲突,在协程中控制共享资源不加锁,只需要判断条件

##### 协程Python

python对协程的支持是通过generator实现的

在generator中,我们不但可以通过for循环来迭代,还可以不断调用next()函数获取由yield语句返回的下一个值

python的yield不但可以返回一个值,它还可以接受调用者发出的参数



##### 例子

传统的生产者消费者模型是一个线程写消息,通过锁机制控制队列等待,可能会死锁

如果改用协程,生产者生产消息后,直接通过yield跳转到消费者开始执行,待消费者执行完毕后,切换回到生产者继续生产

```python
def consumer():
    r = ''
    while True:
        n = yield r	# 拿到n,		yield返回r
        if not n:
            return
        print('[CONSUMER] Consuming %s...' % n)
        r = '200 OK'
        
def produce(c):
    c.send(None)	# 启动生成器
    n = 0
    while n < 5:
        n = n + 1
        print('[PRODUCER] Producing %s...' % n)
        r = c.send(n)　# 切换consumer执行
        print('[PRODUCER] Consumer return: %s' % r)	# 拿到consumer处理结果,继续生产下一条消息
        c.close()
c = consumer()
produce(c)
```

