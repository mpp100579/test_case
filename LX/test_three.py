#coding=utf-8
import urllib
import django
from django.http import HttpResponse
import linecache
import pprint

from m2 import url
from m2 import *
from m2.url import get_page

print m2.url.get_page





print django.get_version()
def hello(request):
    return HttpResponse("Hello world ! ")



#print url.get_page()
#print dir(mpp)#m2是包，包里面有文件夹/模块url,模块url下有个方法，查询包里的内置方法
#print mpp.__file__
#print dir(url)#查询模块、文件夹的内置方法
#print url.__file__
#print url.get_page()

print dir(urllib)#查看模块包含的方法

# 创建一个文件
filename = 'linecacheTest.txt'
myfile = open(filename, 'w')
for i in range(1, 5):
    myfile.write('This is the ' + str(i) + 'th line\n')
myfile.close()

# 获取所有的行
pprint.pprint(linecache.getlines(filename))

# 获取其中任意一行
pprint.pprint(linecache.getline(filename, 3))

# 获取其中第3,4行
pprint.pprint(linecache.getlines(filename)[2:4])

# 释放缓存
linecache.clearcache()
