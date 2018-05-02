 ### 异步IO
**当代码需要执行一个耗时的IO操作时,**
**它只发出IO指令,并不等待IO结果,然后就去执行其他代码,**
**一段时间后,当IO返回结果时,再通知CPU进行处理**

如果按普通顺序写出的代码实际上是没法完成异步IO的:
```python
def_some_code()
f = open('/path/to/file', 'r')
r = f.read() # <== 线程停在此处等待IO操作结果
# IO操作完成后线程才能继续执行
def_some_code(r)
```
所以同步IO模型的代码是无法实现异步IO模型的
**异步IO模型需要一个消息循环,在消息循环中,**
**主线程不断重复"读取消息-处理消息"这一过程**
```python
loop = get_event_loop()
while True:
	event = loop.get_evnet()
	process_event(event)
```
消息模型早在桌面应用程序中使用,一个GUI的主线程就负责不停地读取消息并处理消息.所有的键盘鼠标等消息都被发送到GUI程序的消息队列中,然后由GUI程序的主线程处理.
