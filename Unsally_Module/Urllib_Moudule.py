# urllib提供了一系列操作URL的功能
# Get
# urllib的request模块可以非常方便的抓取URL内容
# 也就是发送一个GET请求到指定的页面, 然后返回HTTP的响应;

# example
# 对豆瓣的一个URLhttps://api.douban.com/v2/book/2129650进行抓取, 并返回响应
from urllib import request

with request.urlopen('https://api.douban.com/v2/book/2129650') as f:
	data = f.read()
	print('Status:', f.status, f.reason)
	for k, v, in f.getheaders():
		print('%s: %s' % (k, v))
	print('Data:', data.decode('utf-8'))

# 模拟浏览器发送Get请求, 就需要使用Request对象, 通过
# 往Request对象添加HTTP头, 就可以把请求伪装成浏览器, 
# example iphone6
'''
from urllib import request

req = request.Request('http://www.douban.com/')
req.add_header('User-Agent', 'Mozilla/6.0(iPhone; CPU iPhone OS 8_0 \
	like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/8.0\
	Mobile/10A5376e Safari/8536.35')
with request.urlopen(req) as f:
	data = f.read()
	print('Status:', f.status, f.reason)
	# for k, v, in f.getheaders():
	# 	print('%s: %s' % (k, v))
	print('Data:', data.decode('utf-8')) # 返回了合适iPhone的移动版网页
'''

# Post
# 如果要以POST发送一个请求, 只需要把参数data以bytes形式传入,

# example
# 模拟一个微博登陆, 先读取登陆的邮箱和口令, 然后按照weibo.cn的登陆页
# 以username=xxx&password=xxx的编码传入
from urllib import request, parse
print('Login to weibo.cn...')
email = input('Email:')
passwd = input('Password:')
login_data = parse.urlencode([
	('username', email),
	('password', passwd),
	('entry', 'mweibo'),
	('client_id', ''),
	('savestate', '1'),
	('ec', ''),
	('pagereger', 'https://passport.weibo.cn/signin/welcom?entry=mweibo&r=http%3A%2F%2Fm.weibo.cn%2F')
	])

req = request.Request('https://passport.weibo.cn/sso/login')
req.add_header('Origin', 'https://passport.weibo.cn/sso/login')
req.add_header('User-Agent', 'Mozilla/6.0(iPhone; CPU iPhone OS 8_0 \
	like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/8.0\
	Mobile/10A5376e Safari/8536.35')
req.add_header('Referer', 'https://passport.weibo.cn/signin/login\
	?=entry=mweibo&res=wel&wm=3349&r=http%3A%2F%2Fm.weibo.con%2F')

with request.urlopen(req, data=login_data.encode('utf-8')) as f:
	print('Status:', f.status, f.reason)
	for k, v in f.getheaders():
		print('%s: %s' % (k, v))
	print('Data:', f.read().decode('utf-8'))

# urllib提供的功能就是利用程序去执行各种HTTP请求, 如果要模拟浏览器
# 完成特定的功能, 需要把请求伪装成浏览器, 伪装的方法就是先监控浏览器
# 发出的请求, 再根据浏览器的请求头来伪装, User-Agent头就是用来标识浏览器的
# 

