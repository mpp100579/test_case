# -*- coding:utf-8 -*-
import smtplib
from email.mime.text import MIMEText
from email.header import Header

sender = '1005794498@qq.com'
receiver = '2906211933@qq.com'
smtpserver = 'smtp.qq.com"'
username = '1005794498@qq.com'
password = 'ziqlcaotmtcabbbg'

# 邮件主题
mail_title = '主题：测试报告3'

# 读取html文件内容
f = open('report_test.html', 'rb')
mail_body = f.read()
f.close()

# 邮件内容, 格式, 编码
message = MIMEText(mail_body, 'html', 'utf-8')
message['From'] = sender
message['To'] = receiver
message['Subject'] = Header(mail_title, 'utf-8')

try:
    smtp = smtplib.SMTP()
    smtp.connect('smtp.qq.com')
    smtp.login(username, password)
    smtp.sendmail(sender, receiver, message.as_string())
    print("发送邮件成功！！！")
    smtp.quit()
except smtplib.SMTPException:
    print("发送邮件失败！！！")
