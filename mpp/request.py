# -*- coding: utf-8 -*-
import requests
import json
import string
import urllib, urllib2


#1.返回一个URL请求
url='http://192.168.1.56:81/Default/GetHealthData'
headers={'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8','Referer':'http://192.168.1.56:81/default/KPICenter','Cookie':'ASP.NET_SessionId=ch4o3vee1fsmduhnlufqwymo; .ASPXAUTH=7EB5ADB89B9806FC9D3DDFF2B8188A445A9E51F541A6D76DC8CECAEB8C4AB701869B79AB89800C31E86E92C34B69C2AB47C66F997AB4A33F7686703409319595F3D7310F7AC8FA6C21749F52BAB78FDCA8789EEE07EB47035CF662AC80DFCE9CCE879F2A335556969022AD48DC162DAA59ADFE0C727279BE972E7D4769BB614F1D33273CFB78DA9B3CF72B7221126149'}
data={'uid':'yujian','password':'yujian612','siteid':'景德镇电厂','djlx':'C'}
'''
data=json.dumps(data)
print type(data)                #python类型对象dump编译成json字符串
'''
r=requests.post(url,data=data,headers=headers)
#print r.text
#把页面代码转成json
jsonStr=json.dumps(r.text)
print jsonStr
print '--'*80

#2.返回第二个URL请求
url='http://192.168.1.56:81/EAM/AbnomalAlert/GetXunJian'
headers={'Content-Type': 'application/json','Referer':'http://192.168.1.56:81/eam/abnomalalert/alertindex','User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36','Cookie':'ASP.NET_SessionId=zjzcjhfb53lvcvqz15usi0ar; .ASPXAUTH=2ED38234170BA7F27A54274EB61F38950FC40BAAD9F9A31CC712DE9164D09E52BA669AC5777795DE919329F903893513C96F8642B86FB9BF2E19CE50AA96B7133B9769EB873FF5B47AE2F6778A89203A2FA4155966DA6002424A3C9391E829FAA84BEB8B993C3B1FF823982200F91E1562E09E63466B9AE6610A37E13290A0D5B295312795F74852AE8AC71D3416B977'}
data={'page': '1', 'pageSize': '10', 'KeyWord': '', 'dateValue': 'today', 'ZYDM': 'QJ'}  #传入Python类型字典参数

data1=json.dumps(data)
print type(data1)                #python类型对象dump编译成json字符串

r=requests.post(url,data=data,headers=headers)           #传输的必须是json格式的字符串才能传输
#print r.text                返回页面代码
#把页面代码转成json
jsonStr=json.dumps(r.text)
print jsonStr
print '--'*80

#print r.json()                    #如果是Get请求，返回的是json字符串


data1=json.dumps(data)
print type(data1)                #python类型对象dump编译成json字符串

d=json.loads(data1)              #1.把json字符串解析成python对象，用loads，把json文件解析成Python对象用load
print d
print type(d)
print r.status_code

data = {
    "statusCode": 200,
    "data": {
        "totoal": "5",
        "height": "5.97",
        "weight": "10.30",
        "age": "11"
    },
    "msg": "成功"
}
json.dump(data, open("listStr.json","w"), ensure_ascii=False) #2.将Python内置类型（或对象）序列化为json对象后写入文件，用dump

strList = json.load(open("listStr.json"))   #3.读取文件中json形式的字符串元素 （.listStr.json格式的文件）转化成python类型用load读取解析
print strList



#另外举例读取txt文件,用loads把json字符串文件读取出来，编译成python类型对象
print '--'*100
file1 = open(r"E:\python2.7.9\python_test\test_case\mpp\jsonFile.txt")
try:
     f = file1.read()
     print(json.loads(f))
     #不要一次读取解析，而是一次解析后一行行读取
     arr = json.loads(f)
     for a in arr:
         print(a)
finally:
     file1.close()
#方法二，把json字符串文件直接读取出来用load解析
str1=json.load(open("jsonFile.txt"))
print str1
print type(str1)





print '--'*100
print string.center('python 解析json字符串,把json字符串解析成字典',60,'*')
s = json.loads('{"name":"test", "type":{"name":"seq", "parameter":["1", "2"]}}')
print s
print type(s)
print s.keys()
print s["name"]
print s["type"]["name"]
print s["type"]["parameter"][1]


print '--'*100
print string.center('把python类型(字典，元祖，数组)转换成json字符串',60,'*')
data = {
    "statusCode": 200,
    "data": {
        "totoal": "5",
        "height": "5.97",
        "weight": "10.30",
        "age": "11"
    },
    "msg": "成功"
}
s = json.dumps(data)   # dumps:把字典转换为json字符串
print type(s)
print s
