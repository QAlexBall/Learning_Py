import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('119.23.33.220', 8081))
print("success!")
# 接受消息
print(s.recv(1024).decode('utf-8'))
for data in [b'Alex\n', b'Tracy\n', b'Sarah\n']:
	# 发送数据
	s.send(data)
	print(s.recv(1024).decode('utf-8'))

pic = open('2.jpg', 'w')
print(pic)
pic.close()
# s.send(pic)
s.send(b'exit')
s.close()
