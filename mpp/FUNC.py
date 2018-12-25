# -*- coding:utf-8 -*-
import time
import string
import os
import random

def func1(x,y):
    return x+y
func2=lambda x,y:x+y#lambda函数用于运算简单的
print func2(4,8)
def test(func1,a,b):
    print func1(a,b)
test(func1,5,7)
test(func2,6,9)
func1(7,0)

func=lambda x,y:x+y
print func(4,6)
re=map(func,[1,5,6,7],[4,6,7,0])#map函数将每次从两个表中分别取出一个元素，带入到lambda所定义的函数
print re

print string.center('map()函数把元素为int的转化为字符串',90,"*")
L = [1,2,3,4,5,6,7,8,9]
S = list(map(str,L))
print("元素字符串类型为的转为int:",S)
l1=['1','2','3','5']
s1=list(map(int ,l1))
print ("元素类型为字符串的转为int类型:",s1)
print '--'*90
#利用map()函数，把用户输入的不规范的英文名字，变为首字母大写，其他小写的规范名字
def formating(name):
    return name.title()
L = list(map(formating, ['adam', 'LISA', 'barT'])) #map（函数，参数）函数可以只接收1个参数，参数是序列
print("练习1的答案:", L)

'''reduce()函数接收的参数和 map()类似，一个函数 f，一个list，但行为和 map()不同，reduce()传入的函数 f 必须接收两个参数，reduce()对list的每个元素反复调用函数f，并返回最终结果值。'''
print string.center('reduce()函数把列表变成整数',90,'*')
from functools import reduce                          #引入reduce函数
def fn(x, y):
    return x * 10 + y
a = reduce(fn, [1, 3, 5, 7, 9])                     #reduce(函数，参数),函数必须接收2个参数，反复调用函数，参数是序列
print("reduce结果为:",a)

def prod(L1=[]):                          #需要传参的是个列表就要用参数L1=[]
    def fn(x,y):
        return x * y
    return reduce(fn,L1)                          #reduce(函数，参数)
P = prod([1,2,3,4,5,6,7,8])
print("练习2乘积的答案:",P)

def func(a):
    if a>100:
        return True
    else:
        return False
print filter(func,[10,56,101,500])                     #filter过滤条件

def action1(n):
    print ('starting action1...')
    with open(current_time+'.txt','a')as f:
        f.write('end action%s\n'%n)
def action2(n):
    print ('starting aciotn2...')
    with open(current_time+'.txt','a')as f:
        f.write('end action%s\n'%n)
def action3(n):
    print ('starting action3...')
    with open(current_time+'.txt','a')as f:
        f.write('end action%s\n'%n)
current_time = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
action1('a'+current_time)
action2('b'+current_time)
action3(3)
print'--'*80    
'''
因为文本文件是储存字符的，list是一种高级数据结构，打印到文本文件中就变成字符串了。
如果你想使用文件储存list的话，需要直接将二进制数据存储到文件中，搜索关键字“python 序列化”。
'''
import string
print string.center('1.pickle序列化',80,'*')
import pickle
current_time = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
#print(current_time )
f=open(current_time+'.txt','wb')
list1=[('tom', 12, 86),('Lee', 15, 99),('Lucy', 11, 58),('Joseph', 19, 56)]
pickle.dump(list1,f)                                  #把列表存到txt文件中
f.close()

f=open('2018-05-10-10_45_07.txt','rb')
storedList = pickle.load(f)                      #把列表从txt文件读取出来
print(storedList)


print string.center('2.json序列化和反序列化',80,'*')
import json
dictObj =[{
    'url':'http://192.168.1.56:81/',
    'uid':'yujian',
    'password':'bkc123456',
}]
jsObj = json.dumps(dictObj)
fileObject = open('jsonFile.txt', 'wb')
f1=fileObject.write(jsObj)
print f1
fileObject.close()
f2=open('jsonFile.txt','rb')
print json.load(f2)
print '--'*90
print string.center('3.request请求',90,'*')
import requests
url = "http://192.168.1.56:81/"
postData =[{
    'uid':'yujian',
    'password':'bkc123456'
}]
#用session请求
session = requests.session()
headers = {'Content-Type': 'text/html'}             #请求头Content-Type很关键，决定了post请求参数
response1 = requests.post(url,headers=headers,data=postData)
print response1.cookies
print response1.status_code

def test_xdj():
    headers = {'Content-Type': 'text/html'}             #请求头Content-Type很关键，决定了post请求参数
    params = {'uid':'yujian','password':'bkc123456'}
    req = requests.post(url, headers=headers, params=params)
    print req.status_code
if __name__ == '__main__':
    url = "http://192.168.1.56:81/"
    test_xdj()
print '--'*80


print string.center('random随机字符串',80,'*')#random()是不能直接访问的，需要导入 random 模块，然后通过 random 静态对象调用该方法
#from random import Random
import random
#随机生成4到20位的用户名
def random_username():
    username = ''
    chars = 'AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz0123456789-_'
    length = len(chars) - 1#长度计算
   # random = random.random()
    for i in range(4,20):  ##随机生成4到20
        username +=chars[random.randint(0, length)]#随机生成0-length之间的整数
    print username
    return username

    #字符串随机
    str='dflkgfldlhhg'
    str1 = str[random.randint(0, len(str)-1)]#注意字符串索引越界问题，索引需要减一
    print str1
    #return username

#随机生成11个字符的手机号码
#from random import Random
def random_phonenum():
    num =''
    chars='1234567890'
    length=len(chars)-1
    #rd=Random()
    for j in range(0,11): #随机生成11个字符
        num +=chars[random.randint(0,length)]
    print num
    #return num

if __name__ == '__main__':
    random_username()
    random_phonenum()

a=10
b=0
try:
    c=a/b
    print c
except ZeroDivisionError as message: #打印python错误
    #print e.message
    print message


i=0
#sum=0
while 1:
    print i+1
    i+=1
    #sum=sum+i
    #print sum
    if i>10:
        break


inputValue=input("please input a int data :") #输入的不对，打印错误
if type(inputValue)!=type(1):
    raise ValueError
else:
    print inputValue

s=raw_input('please input a string:')
print 'your answer is %s'%s

a=5
a=a+a
print a
a+=a
print a
b=a+1
print b
b+=a
print b
c='sdg'
d=c+'jj'
print d
def count():
    fs = []
    for i in range(1,4):
        def f():
            return i*i
        fs.append(f)
    return fs
for f in count():
    print (f())


import sys
def add(a,b):
    print a+b
print sys.argv          #打印路径
if len(sys.argv)<2:
    print "argv is lower 2"
else:
    if sys.argv[1].startswith("-") and (len(sys.argv)==2):
        option=sys.argv[1][2:]
        if option=="help":
            print """this is my add,two parama a and b"""
        elif option=="version":
            print "v1.0"
        else:
            print "no this option"

    elif len(sys.argv)==3:
        try:
            a=int(sys.argv[1])
            b=int(sys.argv[2])
            add(a,b)
        except Exception ,e:
            print e
    else:
        print "parama is biger 3"





fileName='FUNC.py'
def use_func(f):    #可以看出函数引入一个参数是函数对象，因为返回的是一个函数
    return f()


import string
import logging
logging.basicConfig(level=logging.INFO)
def apper():
    alist=range(0,101)
    def lazy_sum(x,y):
        a= reduce(lambda x,y:x+y,alist)
        print a
        logging.warning('you have performed')
    return lazy_sum                   #返回嵌套函数的函数名就是返回函数

if __name__=='__main__':
    sum = apper()
    print sum(1,3)
