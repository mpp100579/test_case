# -*- coding:utf-8 -*-
import requests

#技术监督
#post请求,不需要带请求头，只需要先传递参数
url="http://192.168.1.42/login/dologin"
#headers ={"Content-Type":"application/x-www-form-urlencoded; charset=UTF-8","User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36","Cookie":"theme=0C9C80D8CEFBFA1A; ASP.NET_SessionId=g0kgfzsyfc0jsducxudvnvf2"}
data = {'uid':'lidesheng','password':'bkc123456'}
print type(data)
r = requests.post(url=url,data=data)#字典作为json对象传递参数，传递参数要用到json对象
print r.text
print r.status_code
'''
content=json.dumps(data)      #把dict编码为json格式的字符串，数据传输需要json字符串
# JSON对象:
var str2 = { "name": "deluyi", "sex": "man" }属性名：属性值
JSON字符串:
var str1 = '{ "name": "deyuyi", "sex": "man" }'
print type(content)
print content
'''




#get请求，需要post请求后返回的cookie信息，把cookie加到get请求的头部
url="http://192.168.1.42/default/Home"
headers ={"Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
          "User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36",
          "Content-Type":"application/json",
          #"Cookie":"theme=0C9C80D8CEFBFA1A; ASP.NET_SessionId=e1qyapdvelonjhacgko1r452; .xCookie=EBF9202408AFFDFDBF6ED6077E57318DAE29CB8140C2BFB547976AEE5726D8A82AD04FA330215D29B612A70B4B1475146A64ECE8A9E88946FC3D3C7716A5D73DBFDC7FA659BF2ACCB1A733C6A8CFDC4EB0B5D842EDAF911A89BAF121F846FEA9ACECF02FCB6657288D04F81232A8E7357643171AED170A1DFDF165AB99DF6B2EE6D5E89E17F87408F1121329334CADF7DC7876EB87C07DD9DA2BE476B3BDF5D19879877F6973C9C96E66109FCD3B3E0CBEB9D4EB81C764E46ED3A060D5A4FD55C491581ACF95E430D272F31D3793604D464D024EBD0BA0F83684B32CB4133462"}
          "Cookie":"ASP.NET_SessionId=eb2miqnupz23tedad554pyrf"}
r = requests.get(url=url,params=headers)
print r.status_code
print r.url
print r.text
#print r.text