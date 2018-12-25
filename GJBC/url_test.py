#coding=utf-8
import urllib2
import urllib
import requests



#调用urllib2模块
import urllib2
#import urllib.request

#直接请求
response=urllib2.urlopen("http://www.baidu.com")
#获取状态码，如果是200表示成功
print response.getcode()
#读取爬取得内容
print response.read()









from xml.parsers.expat import ParserCreate

class DefaultSaxHandler(object):
    def start_element(self, name, attrs):
        print('sax:start_element: %s, attrs: %s' % (name, str(attrs)))

    def end_element(self, name):
        print('sax:end_element: %s' % name)

    def char_data(self, text):
        print('sax:char_data: %s' % text)


