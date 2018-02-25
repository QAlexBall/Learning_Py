# 服务器进程首先要绑定一个端口并监听来自其他客户端的连接, 如
# 果其他客户端来连接过来了, 服务器就与客户端建立Socket连接
# , 随后的通信就依靠这个Socket连接
#  
# 服务器会打开固定端口监听, 每来一个客户端来凝结, 就应该创建
# 该Socket连接, 一个Socket依赖4项来唯一确定一个Socket
# 服务器地址, 服务器端口
# 客户端地址, 客户端端口 	
# 服务器需要同时响应多个客户端的请求, 所以, 每个来连接都需要
# 一个新的进程或者新的线程来处理


# 创建一个基于IPv4和TCP协议的Socket
import socket, threading, time
def tcplink(sock, addr):
	print('Accept new connection from %s:%s...' % addr)
	sock.send(b'Welcome!')
	while True:
		data = sock.recv(1024)
		time.sleep(1)
		if not data or data.decode('utf-8') == 'exit':
			break
		sock.send(('Hello, %s!' % data).encode('utf-8'))
	sock.close()
	print('Connection from %s:%s closed.' % addr)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 监听端口
s.bind(('127.0.0.1', 9999))
# 调用listen()方法开始监听端口, 
# 传入的参数指定等待连接的最大数量
s.listen(5)
print('Waiting for connection...')
# accept()等待并返回一个客户端的连接:
while True:
	sock, addr = s.accept()
	# 创建新线程来处理TCP连接
	t = threading.Thread(target=tcplink, args=(sock, addr))
	t.start()