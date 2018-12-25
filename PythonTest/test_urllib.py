# -*-coding:utf-8-*-
'''
from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
driver = webdriver.Firefox()
driver.get("http://weibo.com/login.php")
driver.maximize_window()           #浏览器打开之后设置全屏

import sys
import MySQLdb

reload(sys)
sys.setdefaultencoding('utf-8')

def getdata ():
    try:
        conn = MySQLdb.connect(host='localhost', user='root', passwd='root', db='test', port=3306, charset='utf8')
        try:
            cur = conn.cursor()
            sql = r'select * from person'
            cur.execute(sql)
            allPerson = cur.fetchall()
        finally:
            cur.close()
            conn.close()
    except Exception, e:
        print '数据库错误:', e
        return

    for rec in allPerson:
        print rec[0],rec[1]

if __name__ == '__main__':
    getdata()
'''
import re
import string
import urllib2
import urllib
import urllib2

import requests            #第三方库requests请求网页
import json
r = requests.get(url='https://www.jnu.edu.cn/')  # 最基本的GET请求
print r.cookies
for key,value in r.cookies.items():
    print key+'='+value
s=requests.session()
s.get('http://www.jnu.edu.cn/cookies/set/JSESSIONID/56B712F5DDB817DB2E5AA54602FBA814')
response=s.get('http://www.jnu.edu.cn/cookies')
print response.text

response= requests.get("http://www.baidu.com")
print string.center('获取cookies',200,'*')              #获取cookies
print(response.cookies)
for key,value in response.cookies.items():                  #打印cookies
    print(key+"="+value)
print string.center('会话维持,cookie的一个作用就是可以用于模拟登陆，做会话维持',200,'*')
s = requests.Session()                                 #获取会话，session
s.get("http://httpbin.org/cookies/set/BDORZ/27315")
response = s.get("http://httpbin.org/cookies")
print(response.text)
print response.url

print string.center('证书验证，现在的很多网站都是https的方式访问，所以这个时候就涉及到证书的问题',200,'*')
import requests
from requests.packages import urllib3
urllib3.disable_warnings()
response = requests.get("https://www.12306.cn",verify=False)
print(response.status_code)
print response.url

print string.center('认证设置,如果碰到需要认证的网站可以通过requests.auth模块实现',200,'*')
from requests.auth import HTTPBasicAuth
response = requests.get("http://192.168.1.56:81/",auth=HTTPBasicAuth("user","yujian"))
print(response.status_code)
print response.url

if response.status_code == requests.codes.ok:
    print("访问成功")
print(r.status_code)  # 获取返回状态
if r.status_code==200:
    print ("访问IT成功")
r = requests.get(url='http://dict.baidu.com/s', params={'wd': 'python'})  # 带参数的GET请求
print(r.url)#打印请求的URL
print(type(r.status_code),r.status_code)
print(type(r.headers),r.headers)
print(type(r.cookies),r.cookies)
print(type(r.url),r.url)
print(type(r.history),r.history)
print(type(r.text),r.text)  # 打印解码后的返回数据
'''
print(r.json())
print(json.loads(r.text))
print(type(r.json()))
'''
import requests                                                                #因为访问知乎需要头部信息
headers = {

    "User-Agent":"'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:49.0) Gecko/20100101 Firefox/49.0'"
}
response =requests.get("https://www.zhihu.com",headers=headers)
print(response.text)
'''
url='https://www.apple.com/'#Python2.7自带的urllib和urllib2请求网页
values = {'afid':'p238%7C1Z6yt4iBv-dc_mtid_18707vxu38484_pcrid_14838685234_' ,'cid':'aos-cn-kwba-brand'}
data = urllib.urlencode(values)
req = urllib2.Request(url,data)#urlopen方法也可通过建立了一个Request对象来明确指明想要获取的url。
response = urllib2.urlopen(req)
print response.geturl()
the_page = response.read()
#print the_page
'''
import urllib2
response = urllib2.urlopen('http://python.org/')#方式一，urlopen
print response.geturl()#获取页面URL
html = response.read()

req = urllib2.Request('http://python.org/')#方式二，urllib2.Request
response = urllib2.urlopen(req)
#print response.read()
response=urllib2.urlopen(req)
url=response.geturl()
#print url
info=response.info()
#print info
code=response.getcode()
#print code
'''
print dir()
print help()
print string.center('正则表达式',100,'*')

e='a1b2c3d4f'
print re.split(r'\d',e)

z=re.match(r'\w+$','ab3cdf')#前面是正则表达式，后面是需要匹配的
print z.groups((2))
print z.group()#把 匹配到的按格式拿出来


d=[i for i in e if not i.isdigit()]
print d

new_list=[]#用新的列表来接收列表达式生成的列表值
for i in e:
    if not i.isdigit():
        new_list.append(i)#新用列表来接收i的值
print new_list
'''

print string.center('获取登录页',200,'*')#没有太多的分析过程直接发送post请求，然后获取cookie,通过cookie去访问其他页面,
import requests
import json
def login():
    url = "http://192.168.1.56:81/"
    params = {
        "uid": "yujian",
        "paw":"bkc123456",
    }
    response = requests.post(url,data=params)
    # print response.text
    #res_dict = json.loads(response.text)
    #self.assertEqual(res_dict['code'], 200)

    cookie = response.cookies.get_dict()
    print(cookie)
    url2 ="http://192.168.1.56:81/eam/insp/paibanindex"
    response2 = requests.get(url2,cookies=cookie)
    #print(response2.text)
    print response.status_code
    print response.url
    print response2.url
login()