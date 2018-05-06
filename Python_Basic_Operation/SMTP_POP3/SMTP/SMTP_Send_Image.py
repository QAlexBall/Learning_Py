# 大部分邮件服务上都会自动屏蔽带有外链的图片, 因为不知道这些连接是否指向恶意网站
# 要把图片嵌入到邮件正文中, 我们只需要按照发送附件的方式先把邮件作为
# 附件添加进去, 然后, 在HTML中通过引用src="cid:0"就可以把附件作为图片
# 嵌入了, 如果有多个图片, 给他们依次编号, 然后引用不同的cid:x
from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.utils import parseaddr, formataddr

import smtplib
from_addr = input('From: ') # 输入email地址
password = input('Password: ') # 输入email口令														
to_addr = input('To: ') # 输入收件人地址
smtp_server = input('SMTP server: ') # 输入SMTP服务器地址

def _format_addrs(s): # 格式化一个邮件地址
	name, addr = parseaddr(s)
	return formataddr((Header(name, 'utf-8').encode(), addr))
# 邮件对象
msg = MIMEMultipart()
msg['From'] = _format_addrs('Pythoner <%s>' % from_addr)
msg['To'] = _format_addrs('Manager<%s>' % to_addr)
msg['Subject'] = Header('From SMTP ...', 'utf-8').encode()

# 添加附件, 加上一个MIMEBase, 从本地读取一个图片:
with open('image.jpg', 'rb') as f:
	mime = MIMEBase('image', 'jpg', filename='image.jpg') # 设置附件的MIME和文件名
	mime.add_header('Content-Disposition', 'attachment', filename='image.jpg') # 加上必要的头信息
	mime.add_header('Content-ID', '<0>')
	mime.add_header('X-Attachment-ID', '0')
	mime.set_payload(f.read()) # 把附件内容读进来
	encoders.encode_base64(mime) # 使用Base64编码
	# msg.attach(mime) # 添加到MIMEMutiipart
msg.attach(MIMEText('<html><body><h1>Hello</h1>' \
	+ '<p><img src="cid:0"></p>' \
	+ '</body></html>', 'html', 'utf-8'))

server = smtplib.SMTP_SSL(smtp_server, 465)
server.set_debuglevel(1)
server.login(from_addr, password)
server.sendmail(from_addr, [to_addr], msg.as_string())
server.quit()