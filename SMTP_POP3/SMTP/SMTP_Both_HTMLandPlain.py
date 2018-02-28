from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart

import smtplib
from_addr = input('From: ') # 输入email地址
password = input('Password: ') # 输入email口令														
to_addr = input('To: ') # 输入收件人地址
smtp_server = input('SMTP server: ') # 输入SMTP服务器地址

def _format_addrs(s): # 格式化一个邮件地址
	name, addr = parseaddr(s)
	return formataddr((Header(name, 'utf-8').encode(), addr))
msg = MIMEMultipart('alternativa')
msg['From'] = _format_addrs('Pythoner <%s>' % from_addr)
msg['To'] = _format_addrs('Manager<%s>' % to_addr)
msg['Subject'] = Header('From SMTP ...', 'utf-8').encode()

msg.attach(MIMEText('hello', 'plain', 'utf-8'))
msg.attach(MIMEText('<html><body><h1>Hello</h1></body></html>', \
	'html', 'utf-8'))


server = smtplib.SMTP_SSL(smtp_server, 465)
server.set_debuglevel(1)
server.login(from_addr, password)
server.sendmail(from_addr, [to_addr], msg.as_string())
server.quit()