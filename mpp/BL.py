# -*- coding:utf-8 -*-

data1 = 8

def functionA1():        #改变全局变量的值
    global data1              #变量要看作用域，函数内的变量参与计算时候要看是局部变量还是全局变量,很明显，局部变量还没赋值的情况下不能参与计算，那就得声明是全局变量，计算出来后全局变量也发生了改变
    data1 = data1+5
    print data1

def functionA2():          #因为函数里面没有局部变量，就会默认去找全局变量，全局变量发生了改变就取全局变量发生改变后的值
    a=data1+1
    print a

def functionA3():        #因为函数里已经有设置了局部变量，就会去取局部变量
    data1=3
    data1=data1+6
    print data1

if __name__ == "__main__":
    functionA1()
    functionA2()
    functionA3()


import os
print os.getcwd()      # 返回当前的工作目录
#print os.chdir('/testmpp')   # 修改当前的工作目录
#print os.system('mkdir today')   # 执行系统命令 mkdir
#print dir(os)      #属性
#print help(os)    #方法
'''
a = [1,2,3]
print a.append([9,9])
print a.__sizeof__()
#print a.pop()
print a.__add__([3,2,5])
print help(a) #会显示list的帮助

import unittest
from selenium import webdriver
print help(webdriver)

import sys
print sys.stderr.write('Warning, log file not found starting a new one\n')       #错误输出重定向和程序终止

import random
print random.betavariate(3,5)
print random.choice([7,9,90,80])
print random.expovariate(34)
print random.random()

#print help(list)
#print dir(list)
l1=[1,2,4,5,7]
print l1.__add__([3,2,34,5,5])

print l1.__contains__(2)
import requests
print help(requests)
'''
import requests
import json



#优化检修
#post请求,不需要带请求头，只需要先传递参数
url="http://192.168.1.42:81/login/dologin"
#headers ={"Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8","User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36"}
data = {'uid':'dd','password':'bkc123456','isTerrace':'false'}
print type(data)
r = requests.post(url=url,data=data)#字典作为json对象传递参数，传递参数要用到json对象
print r.text
print r.status_code
'''
content=json.dumps(data)      #把dict编码为json格式的字符串，数据传输需要json字符串
# JSON对象:
var str2 = { "name": "deluyi", "sex": "man" }
JSON字符串:
var str1 = '{ "name": "deyuyi", "sex": "man" }'
print type(content)
print content
'''




#get请求，需要post请求后返回的cookie信息，把cookie加到get请求的头部
url="http://192.168.1.42:81/Default/HomePage?LinkUrl=/default/MainPage"
headers ={"Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8","User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36","Cookie":"ASP.NET_SessionId=luydfn1v5ojof2j5jcswgnt1; olCookie=DCC40D2BFDCA7FB6C1DDA54E65156454B6B367094CE12B32ADA825C33F92E546F9931BFA1A43BDBC2972CAA901D3B5D063BE0DE4B1670C9B8C090C8CFC4833AAAE7F4FF4B35A627E8C67DF9A73C1FBC24A0E7921B2C985CC94E9AB95778A07D168D186FA9816E7048D7C8A09A56DA068C333F98311472949589621E80B71FBDA902B243FBEBD944DACECA676EA732818"}
#content={"Cookie":"ASP.NET_SessionId=luydfn1v5ojof2j5jcswgnt1; olCookie=DCC40D2BFDCA7FB6C1DDA54E65156454B6B367094CE12B32ADA825C33F92E546F9931BFA1A43BDBC2972CAA901D3B5D063BE0DE4B1670C9B8C090C8CFC4833AAAE7F4FF4B35A627E8C67DF9A73C1FBC24A0E7921B2C985CC94E9AB95778A07D168D186FA9816E7048D7C8A09A56DA068C333F98311472949589621E80B71FBDA902B243FBEBD944DACECA676EA732818"}
r = requests.get(url=url,params=headers)
print r.status_code
print r.url
#print r.text