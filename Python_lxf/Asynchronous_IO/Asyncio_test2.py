import threading
import asyncio


@asyncio.coroutine
def hello():
    print('hello world! (%s)' % threading.current_thread())
    yield from asyncio.sleep(1)
    print('Hello again! (%s)' % threading.current_thread())


loop = asyncio.get_event_loop()
tasks = [hello(), hello()]
loop.run_until_complete(asyncio.wait(tasks))    # 两个coroutine是由同一个线程并发执行的
loop.close()
