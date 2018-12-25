# -*- coding:utf-8 -*-
import smtplib
from email.mime.text import MIMEText
from email.header import Header
'''
sender = '1005794498@qq.com'#from@php.cn
receivers = ['2906211933@qq.com','327971580@qq.com']  #接收邮件，可设置为你的QQ邮箱或者其他邮箱
email_host = 'smtp.qq.com'     #邮箱地址
email_pass='ziql caot mtca bbbg'# 此处为在qq开启SMTP服务时返回的密码 （须修改）

# 三个参数：第一个为文本内容，第二个 plain 设置文本格式，第三个 utf-8 设置编码
message = MIMEText('Python 邮件发送测试...', 'plain', 'utf-8')
message['From'] = Header("php中文网", 'utf-8')
message['To'] = Header("测试", 'utf-8')

subject = 'Python SMTP 邮件测试'
message['Subject'] = Header(subject, 'utf-8')

try:
    smtpObj = smtplib.SMTP(email_host, 25)
    smtpObj.login(sender, email_pass)
    smtpObj.sendmail(sender, email_pass,receivers, message.as_string())
    print "邮件发送成功"
except smtplib.SMTPException:
    print "Error: 无法发送邮件"
'''

import smtplib
from email.mime.text import MIMEText
_user = "1005794498@qq.com"
_pwd  = "ziqlcaotmtcabbbg"
listStr = ["2906211933@qq.com", "327971580@qq.com", "593607357@qq.com"]
_to = ','.join(listStr)
#_to   = "2906211933@qq.com","327971580@qq.com","1973366864@qq.com" ,"593607357@qq.com"'

msg = MIMEText("Test :you have to write a report !")
msg["Subject"] = "Topic: you don't panic"
msg["From"]    = _user
msg["To"]      = _to

try:
    s = smtplib.SMTP_SSL("smtp.qq.com", 465)
    s.login(_user, _pwd)
    s.sendmail(_user, _to, msg.as_string())
    s.quit()
    print("Success!")
except smtplib.SMTPException,e:
    print ("Falied,%s" %e)