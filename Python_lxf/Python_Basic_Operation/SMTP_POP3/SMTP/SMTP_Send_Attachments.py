# 带附件的邮件可以看作包含若干部分的邮件: 文本和各个附件本身
# 可以构建一个MIMEMultipart对象代表邮件本身, 加上一个MIMEText
# 作文邮件正文, 再继续添加MIMEBase对象

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

# 邮件正文时MIMEText
msg.attach(MIMEText('send with file...', 'plant', 'utf-8'))
# 添加附件, 加上一个MIMEBase, 从本地读取一个图片:
with open('image.jpg', 'rb') as f:
	mime = MIMEBase('image', 'jpg', filename='image.jpg') # 设置附件的MIME和文件名
	mime.add_header('Content-Disposition', 'attachment', filename='image.jpg') # 加上必要的头信息
	mime.add_header('Content-ID', '<0>')
	mime.add_header('X-Attachment-ID', '0')
	mime.set_payload(f.read()) # 把附件内容读进来
	encoders.encode_base64(mime) # 使用Base64编码
	msg.attach(mime) # 添加到MIMEMutiipart

server = smtplib.SMTP_SSL(smtp_server, 465)
server.set_debuglevel(1)
server.login(from_addr, password)
server.sendmail(from_addr, [to_addr], msg.as_string())
server.quit()