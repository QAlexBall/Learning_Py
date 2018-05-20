# asyncio是Python3.4版本引入的标准库,直接内置了对异步IO的支持
#　asyncio的编程模型就是一个消息循环.从asyncio模块中直接获取一个EventLoop的引用
#　然后把需要执行的协程扔到ＥventLoop中执行,就实现了异步IO.

import asyncio

@asyncio.coroutine
def hello():
	print('Hello World!')
	# 异步调用asyncio.sleep(1)
	r = yield from asyncio.sleep(1)
	print('Hello again!')

# 获取EventLoop
loop = asyncio.get_event_loop()
# 执行coroutine
loop.run_until_complete(hello())
loop.close()