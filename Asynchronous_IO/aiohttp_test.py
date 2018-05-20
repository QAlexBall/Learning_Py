"""
[description]
asycio可以实现单线程并发IO操作.如果仅用在客户端,发挥的威力不大.
如果把asyncio用在服务器端,例如Web服务器,由于HTTP连接就是IO操作
因此可以用单线程+coroutine实现多用户的高并发支持.
"""

# asyncio实现了TCP,UDP,SSL等协议,aiohttp则是基于asyncio实现的HTTP框架
