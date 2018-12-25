#coding=utf-8
from _ast import Print
from string import join
import linecache
import sys
import string
'''
a=False
a='dgs'

print id(a)
print type(a)
b='dfds'
print id(b)
print type(b)

a = 'abcd'
c=a.replace('ab','ccc')
print c
print a[len(a)-1]
print a[len(a)-2]

print a[-1]
print a[0:]
print a[1:3]
print a[0:3]

a = 'jay'
b = 'python'
c=input("请输入任意数字：")
print "my name is %s"%a,"i love %s"%(b)
print 'my name is %s %s'%(a,12)
print 'my name is %s,i love %s,my age is %d years old!'%(a,b,c)
print ("He is %d years old"%(25))


a='my name is %s %s'%('12','apple')
pirnt a


#字符串拼接方法
v =",".join([a,b])
print v
v = "".join([a,b])
print v
#写入文件
o=open("a.txt","w")
o.write('hi\n second hi')
o.close()
#读出来
d=open('a.txt','r')
d.seek(0)
print d.read(1000)

#除了占位符还有内置方法用format替换
a = 'pyer'
b = 'apple'
print 'my name is {1} {0}'.format('apple','mpp')
print 'my name is {whose} {fruit}'.format(fruit='apple',whose='mpp')

o=open('info.txt','w')
o.write('this is my apple\nhahaha\ndsdsha\nwrrwha\ntrrhgha\nfdlkdsd\nfirw\new\neerrrr\n500')
o.close()
#linecache.getline引入linecache类的getline方法每行读取
a=open('info.txt','r')
a.seek(0)
print a.read(500)
print linecache.getline('info.txt',1)
print linecache.getline('info.txt',6)
print linecache.getline('info.txt',3)

#打印中间字符串
s = "i,am,lilei"
print s[2:4]
#修改某个字符串
a='i love mpp'
b=a.replace('mpp','wzx')
print b
#文件中字符串操作
file=open('test.txt','w')
file.write('2012来了。\n2012不是世界末日。\n2012欢乐多。\n')
file.close()
#文件读取出来，放到变量content中;转换成utf-8类型用变量dcontent接收
file1=open('test.txt','r')
content=file1.read()
dcontent=content.decode('utf-8')
file1.seek(0)#光标定位在首字符
print content#打印读取内容
print len(dcontent)#打印文本的长度

print content.replace('\n','')#3.请去除该文本的换行
print content.replace('2012','2013')#替换其中字符
print dcontent[len(dcontent)/2:len(dcontent)/2+5].encode('utf-8')#5.请取出最中间的长度为5的子串。
print dcontent[-2:].encode('utf-8')#6.请取出最后2个字符。
print dcontent[:11].encode('utf-8')#7.请从字符串的最初开始，截断该字符串，使其长度为11.


cinfo = '1234'
print id(cinfo)
print cinfo
print sys.getrefcount('1234')
binfo = '1234'
print id(binfo)
print sys.getrefcount('1234')

print string.digits
print string.lowercase
print string.punctuation
print string.ascii_lowercase
print string.ascii_uppercase

s = "i,am,lilei"
c = s.split(',')[1]
print c

f = open('test.txt','r')
content = f.read()
print content

dcontent = content.decode('utf-8')##转换为unicode
print len(dcontent)#2.请计算该文本的原始长度.

print content.replace('\n','')#3.请去除该文本的换行

print dcontent[:11].encode('utf-8')#7.请从字符串的最初开始，截断该字符串，使其长度为11.

a = "i,am,a,boy,in,china"
print a[7:10]
print a.find('i')##-1
print a.index('i')##报错
print a.find('i',a.find('china'))
print a.rfind('i')

f = open('test.log1','w')
sys.stdout = f
help(string)
f.close()

'''
names ='Tinada, Niuer, Zhangsan, Lisi, Wangwu, Zhaoliu'
names1=names.split()#字符串转列表
print names
print names1
l = ["hi","hello","world"]
print(" ".join(l))#列表转成字符串
name = input('Plz input the name:')
for names1 in names:
     Print('Your input is right!')
'''
print('1+2+3+4'.split('+'))  # 切割字符串，返回一个列表list
print('1+2+3+4'.split())  # 切割字符串，返回一个list
print('1+2+3\n1+2+3+4'.split('+'))   # 按照换行符分割
print('1+2+3\n1+2+3+4'.splitlines())  # 按照换行符分割
str = "Line1-abcdef \nLine2-abc \nLine4-abcd";
print str.split( )
print str.split(' ', 1 )
'''