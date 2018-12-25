# -*- coding:utf-8 -*-
import requests

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