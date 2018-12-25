# coding:utf-8
from selenium import webdriver
from selenium.webdriver.common.by import By
import os

def sum(*arg):
    res = 0
    for e in arg:
        res += e
    return res
print sum(1, 2, 3, 4)
print sum(1, 1)

f = open("18-03-29.txt", "w")# 打开一个文件,往18-03-29.txt文件写
print "文件名: ", f.name
print "是否已关闭 : ", f.closed
print "访问模式 : ", f.mode
print "末尾是否强制加空格 : ", f.softspace
print "文件名: ", f.name
f.write( "www.baidu.com!\nVery good site!\n")#往文件里面写
a=11
f.write("您的年龄是：%s\n"%a)#往文件里面写
age=input("请输入您的年龄:")
print("您的年龄是：%s"%age)
print '您的年龄是:',age
print age
#i=input('please input your name:')
#f.write("您的姓名是：%s"%i)#往文件里面写
position=f.tell()#输出当前指针位置
print "当前文件位置 : ", position
position=f.seek(56.1)#设置指针位置
t='PPT'
f.write('%s\n'%t)
f.write('t\n我讲的是:%s'%t)
f.close()

document = open("testfile.txt", "w+")# 打开另一个文件,往testfile.txt文件写
print "文件名: ", document.name
document.write("这是我创建的第一个测试文件！\nwelcome!");#往文件里面写
print document.tell()#输出当前指针位置
document.seek(os.SEEK_SET)#设置指针回到文件最初
context = document.read()
print context
document.close()

f = open("18-03-29.txt", "r+")# 打开一个文件，把文件里面的内容读取出来
for line in f:
    print line
position = f.tell()# 查找当前位置
print "当前文件位置 : ", position
position = f.seek(0, 0)#把指针再次重新定位到文件开头
str = f.read(10)
print "重新读取的10个字符串是 : ", str
f.close()#关闭打开的文件
'''
文件定位
tell()方法告诉你文件内的当前位置, 换句话说，下一次的读写会发生在文件开头这么多字节之后。
seek（offset [,from]）方法改变当前文件的位置。Offset变量表示要移动的字节数。From变量指定开始移动字节的参考位置。
如果from被设为0，这意味着将文件的开头作为移动字节的参考位置;如果设为1，则使用当前的位置作为参考位置。如果它被设为2，
那么该文件的末尾将作为参考位置。


'''