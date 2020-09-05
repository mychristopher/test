#！/usr/bin/python
# -*- coding: utf-8 -*-
#发邮件的库
import smtplib
#邮件文本
from email.mime.text import MIMEText

#SMTP服务器
SMTPServer = "smtp.163.com"
#发邮件的地址
sender = "cyf1366254420@163.com"
#发送者邮箱的密码（授权密码）
passwd = "123456789c"

#设置只发送的内容
message = "xiaoxiannv is a small sun, full of positive energy"

#转换成邮件文本
msg = MIMEText(message)

#标题
msg["Subject"] = "来自帅哥的问候"

#发送者
msg["From"] = sender

#创建SMTP服务器,一般邮件的端口号都是25
mailServer = smtplib.SMTP(SMTPServer,25)
#登陆邮箱
mailServer.login(sender,passwd)
#发送邮件
mailServer.sendmail(sender,["1366254420@qq.com"],msg.as_string())
#退出邮箱
mailServer.quit()