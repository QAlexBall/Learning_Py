# TCP编程
# Socket是网络编程的一个抽象概念,通常用Socket表示"打开了一个网络链接"
# 而打开一个Socket需要知道目标计算机的IP地址和端口号,再指定协议类型即可

# 大多数来凝结都是可靠的TCP连接, 创建TCP连接时, 
# 主动发起连接的叫客户端, 被动响应连接的叫服务器
# 导入socket库
import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)   # AF_INET指定使用IPv4, SOCK_STREAM指定使用面向流的TCP协议
s.connect(('www.sina.com.cn', 80))      # 建立连
s.send(b'GET / HTTP/1.1\r\nHost: www.sina.com.cn\r\nConnection:close\r\n\r\n')      # 发送数据

# 接收数据
buffer = []
while True:
	d = s.recv(1024) # 每次最多接收一个字节
	if d:
		buffer.append(d)
	else:
		break
data = b''.join(buffer)
s.close()

# 接收到的数据包括HTTP头和网页本身, 
# 把HTTP头和网页分离一下, 把HTTP头打印出来, 网页内容保存到文件
header, html = data.split(b'\r\n\r\n', 1)
print(header.decode('utf-8'))
with open('sina.html', 'wb') as f:		# 把接收的数据写入文件
	f.write(html)
