# 邮件主题, 如何显示发件人, 收件人并非通过SMTP发送给MTA, 而是包含在发给MTA的文本中的
# 必须把From, To和Subject添加到MIMEText中
from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr

import smtplib
from_addr = input('From: ') # 输入email地址
password = input('Password: ') # 输入email口令														
to_addr = input('To: ') # 输入收件人地址
smtp_server = input('SMTP server: ') # 输入SMTP服务器地址

def _format_addrs(s): # 格式化一个邮件地址
	name, addr = parseaddr(s)
	return formataddr((Header(name, 'utf-8').encode(), addr))
msg = MIMEText('hello, send by A code ...', 'plain', 'utf-8')
msg['From'] = _format_addrs('Pythoner <%s>' % from_addr)
msg['To'] = _format_addrs('Manager<%s>' % to_addr)
msg['Subject'] = Header('From SMTP ...', 'utf-8').encode()

server = smtplib.SMTP_SSL(smtp_server, 465)
server.set_debuglevel(1)
server.login(from_addr, password)
server.sendmail(from_addr, [to_addr], msg.as_string())
server.quit()

# 在创建SMTP对象后, 立即调用startttls()方法, 
# 就创建了安全连接
# Message
# +- MIMEBase
# 	+- MIMEMultipart
# 	+- MIMENonMultipart
# 		+- MIMEMessage
# 		+- MIMEText
# 		+- MIMEImage