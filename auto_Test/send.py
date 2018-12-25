#coding=utf-8

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def SendMail(subject,msg,to_addrs,from_addr,smtp_addr,password):
    '''
    @subject:邮件主题
    @msg:邮件内容
    @to_addrs:收信人的邮箱地址
    @from_addr:发信人的邮箱地址
    @smtp_addr:smtp服务地址，可以在邮箱看，比如163邮箱为smtp.163.com
    @password:发信人的邮箱密码
    '''
    mail_msg = MIMEMultipart()      #创建一个带附件实例

    #构造附件test.docx
    att1 = MIMEText(open(r'E:\test\2018-07-23 15-29-55test_result.html','rb').read(), 'base64', 'gb2312')
    att1["Content-Type"] = 'application/octet-stream'
    att1.add_header('Content-Disposition', 'attachment', filename=u'测试报告.html'.encode('gbk'))
    mail_msg.attach(att1)
    #构建MIMEText纯文本内容
    txt = MIMEText(msg,'plain', 'utf-8')
    mail_msg.attach(txt)

    mail_msg['Subject'] = subject
    mail_msg['From'] =from_addr
    mail_msg['To'] = ','.join(to_addrs)
    try:
        s = smtplib.SMTP()
        s.connect(smtp_addr)  #连接smtp服务器
        s.login(from_addr,password)  #登录邮箱
        s.sendmail(from_addr, to_addrs, mail_msg.as_string()) #发送邮件
        s.quit()
        print "success"
    except Exception,e:
       print str(e)


if __name__ == '__main__':
    from_addr = "1005794498@qq.com"
    smtp_addr = "smtp.qq.com"      #设置服务器,使用其他邮件服务商的 SMTP 访问（QQ、网易、Google等）
    to_addrs = ["2906211933@qq.com"]
    subject = "send test"
    password = "ziqlcaotmtcabbbg"
    msg = "hello,this is just a send test"
    SendMail(subject,msg,to_addrs,from_addr,smtp_addr,password)