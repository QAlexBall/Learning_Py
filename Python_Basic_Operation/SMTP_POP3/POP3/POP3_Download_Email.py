# 收取邮件常用的协议是POP3, Python内置poplib模块, 实现了POP3模块
# 可以用来接收邮件 POP3收取的不是一个已经可以阅读的邮件本身, 而是
# 邮件的原始文本, 这和SMTP协议很像, SMTP发送的也是经过编码后的一大段文本
# 
# 
# 要把POP3收取的文本变成可以阅读的邮件, 还需要用email模块提供的各类来
# 解析原始文件, 变成可阅读的邮件对象, 所以收取文件分两步:
										# 1, 用poplib把邮件的原始文本下载到本地
										# 2, 用email解析原始文本, 还原为邮件对象
import poplib

from email.parser import Parser
from email.header import decode_header
from email.utils import parseaddr
email = input('Email:')
password = input('Password:')
pop3_server = input('POP3 Server:')

server = poplib.POP3_SSL(pop3_server) # 连接到POP3服务器
server.set_debuglevel(1) # 可以代开或关闭调试信息
print(server.getwelcome().decode('utf-8')) # 打印POP3服务器的欢迎文字

server.user(email)
server.pass_(password)
print('Messsage: %s. Size: %s' % server.stat()) # 返回邮件的数量和占用空间
resp, mails, octets = server.list() # list()返回所有邮件的编号
print(mails) # 可以查看发返回的列表类似[b'1 8948', b'2 79574'...]

index = len(mails)
resp, lines, octets = server.retr(index) # 获取最新的以封邮件, 索引由1开始

# lines存储了邮件的原始文本的每一行
msg_content = b'\r\n'.join(lines).decode('utf-8') # 可以获得整个邮件的原始文本
msg = Parser().parsestr(msg_content)
# sever.dele(index) 可以根据索引号直接从服务器删除邮件
server.quit()

# indent用于缩进显示
def print_info(msg, indent=0):
	if indent == 0:
		for header in ['From', 'To', 'Subject']:
			value = msg.get(header, '')
			if value:
				if header == 'Subject':
					value = decode_str(value)
				else:
					hdr, addr = parseaddr(value)
					name = decode_str(hdr)
					value = u'%s <%s>' % (name, addr)
			print('%s%s: %s' % (' ' * indent, header, value))
	if (msg.is_multipart()):
		parts = msg.get_payload()
		for n, part in enumerate(parts):
			print('%spart %s' % (' ' * indent, n))
			print('%s-------------------' % (' ' * indent))
			print_info(part, indent + 1)

	else:
		content_type = msg.get_content_type()
		if content_type=='text/plain' or content_type=='text/html':
			content = msg.get_payload(decode=True)
			charset = guess_charset(msg)
			if charset:
				content = content.decode(charset)
				print('%sText: %s' % ('  ' * indent, content + '...'))
			else:
				print('%sAttachment: %s' % ('  ' * indent, content_type))
def decode_str(s):
	value, charset = decode_header(s)[0]
	if charset:
		value = value.decode(charset)
		return value
def guess_charset(msg):
	charset = msg.get_charset()
	if charset is None:
		content_type = msg.get('Content-Type', '').lower()
		pos = content_type.find('charset=')
		if pos >= 0:
			charset = content_type[pos + 8:].strip()
		return charset
print_info(msg, 0)