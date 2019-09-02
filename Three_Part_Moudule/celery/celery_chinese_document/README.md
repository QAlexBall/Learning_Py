# Celery 进阶

```shell
# Celery程序可以用于启动职称(Worker):
$ celery -A proj woker -l info

# stop woker
$ Control + c

# backend to run
$ celery multi start w1 -A proj -l info

# restart
$ celery multi restart w1 -A proj -l info

# stop backend
$ celery multi stop w1 -A proj -l info
$ celery multi stopwait w1 -A proj -l info # 可以保证在推出之前完成当前正在执行的任务
```

### 程序调用
可以用delay()方法进行调用。

```>>> add.delay(2, 2)```

delay()实际上为apply_async((2, 2))的快捷方式
apply_async()可以指定调用时执行的参数，例如运行的时间，使用的任务队列等。

```>>> add.apply_async((2, 2), queue='lopri', countdown=10)```

直接调用任务函数进行执行任务，不会发送任何任务消息。

```>>> add(2, 2) # output 4 ```

`delay()` `apply_async()` 以及 `apply(__call__)` 为Celery调用的API，也可以用于签名

如果配置了结果后端，可以获取任务的返回值

```shell
>>> res = add.delay(2, 2)
>>> res.get(timeout=1)
4
```

一个任务当前只能拥有一个状态，但他的执行过程可以分为多个状态，一个典型的阶段是：

```PENDING -> STARTED -> SUCCESS```

启动状态是一种比较特殊的状态，仅在task_track_started启动设置或`@task(track_started=True)` 的情况下才会进行记录，而是未知任务ID的默认状态。

```shell
>>> from proj.celery import app
>>> res = app.AsyncResult('this-id-does-not-exist')
>>> res.state
'PENDING'
```

重任务比较复杂，为了证明，一个任务会重试两次，任务的阶段为

`PENDING -> STARTED -> RETRY -> STARTED -> RETRY -> STARTED -> SUCCESS`

### Canvas: 设计工作流程

有时候可能希望将任务调用的签名传递给另一个进程或其他函数的参数，Celery提供了一共交签名的东西。

签名通过一种方式进行封装任务调用的参数以及执行选项，便于传递给他函数，或者通过序列化网络传送。

可以将add使用的参数作为任务创建的签名，倒计时为10s

```shell
>>> add.signture((2, 2), countdown=10)
task.add(2, 2)
```

也可以通过一个快捷方式进行操作

```shell
>>> add.s(2, 2)
tasks.add(2, 2)
```

##### 再次调用API

签名实例支持调用API：这就意味着可以使用delay和apply_async方法。但区别在于签名实例已经指定了签名参数，该add任务有两个参数，需要指定两个参数的钱ing才能够完成一个完整的签名实例。

```shell
>>> s1 = add.s(2, 2)
>>> res = s1.delay()
>>> res.get()
4
```

也可以创建不完整的签名来进行创建称之为`partials`的内容（有点像柯里化）

```shell
# incomplete the partial: add(?, 2)
>>> s2 = add.s(2)
```

s2为一个不完整的签名，需要另一个参数，可以通过调用签名解决：

```shell
# resolves the partial: add(8, 2)
>>> res = s2.delay(8)
>>> res.get()
10
```

如上所述，签名支持调用API：

* `sig.apply_async(args=(), kwargs={}, **options)`

  使用可选的部分参数和部分关键字调用参数签名以及支持部分执行选项

* sig.delay(args, *kwargs)

  快捷版本的apply_async,任何参数都将作为签名中的参数，关键字参数将与任何现有键合并。

##### 原语

这些原语本身就是签名对象，可以通过任何进行组合，形成复杂的工作流

###### 组： Groups

一个group并行调用任务队列，返回一个特殊的结果实例，可以将结果作为一个列表进行查看，并且通过索引进去获取返回值。

``` shell
>>> from celery import group
>>> from proj.tasks import add
>>> group(add.s(i, i) for i in xrange(10))().get()
[0, 2, 4, 6, 8, 10, 12, 14, 16, 18]
```

* Partial group

```sh j
>>> g = group(add.s(i) for i in xrange(10))
>>> g(10).get()
[10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
```

###### 链： Chains

可以将两个任务链接在一起，在一个返回后进行调用另外一个任务

```shell
>>> from celery import chain
>>> from proj.tasks import add, mul
# (4 + 4) * 8
>>> chain(add.s(4, 4) | mul.s(8))().get()
64
```

partial chain

```shell
>>> # (? + 4) * 8
>>> g = chain(add.s(4) | mul.s(8))
>>> g(4).get()
64
```

```shell
>>> (add.s(4, 4) | mul.s(8))().get()
64
```

###### 和弦： Chords

和弦是一个带有回调的组：

```shell
>>> from celery import chain
>>> from proj.tasks import add, mul

# (4 + 4) * 8
>>> chain(add.s(4, 4) | mul.s(8))().get()
64
```

链接到其他任务的组将自动转化成和弦

```shell
>>> (group(add.s(i, i) for i in xrange(10)) | xsum.s())().get()
90
```

这些原语都是签名类型的，可以根据需要进行组合

```shell
>>> upload_documnent.s(file) | group(apply_filter.s() for filter in filters)
```



### 路由

Celery支持AMQP中提供的所有路由，可以将消息发送到指定的任务队列路由。

通过`task_routes`可以设置一个按名称分配的路由任务队列，将所有的内容集中存放在一个位置：

```shell
app.conf.update(
		task_routes = {
				'proj.task.add': {'queue': 'hipri'},
		},
)
```

可以在程序使用queue参数进行指定队列

```shell
>>> from proj.tasks import add
>>> add.apply_async((2, 2), queue='hipri')
```

可以通过`,`作为分割符进行设置多个队列

```shell
$ celery -A proj worker -Q hipri,celery
```

队列名称的顺序不分前后，职程（Worker）给予队列分配的权重是相同的。

### 远程控制

使用RabbitMQ（AMQP），Redis或Qpid作为中间人（Broker），**可以在运行时控制和检查职程（Worker）。**

例如，当前职程（Worker）正在处理的任务。

`$ celery -A proj inspect active`

这是通过广播消息实现的，集群中所有职程（Worker）都会将收到远程控制发出的指令。也可以通过`—destination`选项

指定一个或多个职程（Worker）进行操作，使用`,`进分割职程（Worker）主机列表：

`$ celery -A proj inspect activae —destination=celery@example.com` 

如果没有提供目的地，那么每个工作人员都将采取行动并回复请求。

celery inspect命令不能修改程序，只能查看职程（worker）概况以统计信息，可以通过help查看

`$ celery -A proj inspect —help`

celery control 命令可以查看实际上改变了工作在运行时的状况。

`$ celery -A proj control —help`

例如，可以强制职程（Worker）启动事件消息（用于监控任务以及职程（Worker））：

`$ celery -A proj control enble_events`

启动事件后 ，可以启动事件转储程序，进行查看职程（Worker）目前执行的状况：

`$ celery -A proj events —dump`

或者可以启动`curses`接口

当监控完毕之后，可以禁用事件：

`$ celery -A proj control disable_events`

celery status命令可以远程控制并且显示集群中职程序（Worker）的列表：

`celery -A proj status`

### 时区

`app.conf.timezone = 'Europe/London'`

### 优化

`$ pip install librabbitmq`