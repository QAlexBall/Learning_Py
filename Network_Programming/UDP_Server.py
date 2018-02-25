# UDP编程(面向无连接的协议)
# 使用UDP协议, 不需要建立连接, 只需要知道对方IP地址和端口号
# 就可以直接发送数据包, 不确定能否到达, 不可靠但比TCP快

import socket
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# SOCK_DGRAM指定这个socket类型是UDP
# 绑定端口
s.bind(('127.0.0.1', 9999))
# 不需要listen()方法, 而是直接接收来自任何客户端的数据
print('Bind UDP on 9999...')
while True:
	# 接收数据
	data, addr = s.recvfrom(1024) # 返回数据和客户端的地址和端口
	print('Received from %s:%s.' % addr)
	s.sendto(b'Hello, %s!' % data, addr) # 把数据用UDP发给客户端
# 省掉了多线程

