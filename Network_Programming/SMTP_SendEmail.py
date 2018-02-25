# Python对SMTP支持有smtplib和email两个模块
# email负责构造邮件, smtplib负责发送邮件

# 最简单的纯文本文件
from email.mime.text import MIMEText
msg = MIMEText('hello, send by Python...', 'plain', 'utf-8') # 第一个参数是邮件正文
															# 第二个参数是MIME的subtype, 'plain'表示纯文本
from_addr = input('From: ') # 输入email地址
password =  input('Password: ') # 输入email口令														
to_addr =  input('To: ') # 输入收件人地址
smtp_server = input('SMTP server: ') # 输入SMTP服务器地址

import smtplib
server = smtplib.SMTP_SSL(smtp_server, 465) # SMTP协议默认端口是25
server.set_debuglevel(1) # 打印出和SMTP服务器交互的所有信息
server.login(from_addr, password)
print('Login successing!')
server.sendmail(from_addr, [to_addr], msg.as_string())
server.quit()
												