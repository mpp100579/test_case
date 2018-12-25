# -*- coding: utf-8 -*-ds
name = "alex"
pwd = "123456"
print "i am %s " % name

import getpass

name = raw_input('请输入用户名：')
pwd = raw_input('请输入密码：')
count = 0
while count < 3:
    if name == "alex" and pwd == "123456":
        print("欢迎，alex！")
        break
    elif name != null or pwd !=null:
        print ("login fail!")
        break
    else:
        print("请输入用户名和密码:")
        break
