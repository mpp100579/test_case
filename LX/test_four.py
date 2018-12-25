#coding=utf-8

import sys
'''
import urllib


a=[1,2,3,4,5,6]
try:
    print a[4]
except:
    print u'出错啦，'
else:
    print 'dsj'
finally:
    print 45

print '继续往下运行'

str1='http://www.fdsss1.com'
try:
    d=urllib.urlopen(str1)
except IOError:#还有很多其他异常需要去捕获
    print '哈哈，页面出错了！'
#try:

#except:

else:
    content=d.read
    print content
    #print content
    #print d.readline
    #print d.readlines
    #print d.read
finally:
    print '欢迎您'




try:
    a=3
    assert a > 4,'message出错啦'#先断言绝对不能出错的地方，语法，assert 表达式,'message出错信息'
except:
    exc=sys.exc_info()
    print exc


a=['1.50','456','678','abc','HGD','ABC']
print [i.center(5) for i in a]
print [i.upper() for i in a if i.isalpha()]#把有字母组成的变成大写
print [i.lower() for i in a if i.isupper()]#把大写变成小写
print [int(i) for i in a if i.isdigit()]#把数字的变成整形


while True:
    str1=raw_input('please input a stirng:')
    if str1!='quit':
        break                      #break停止执行后执行最后一句print
    print 'the str1 is %s,the lenth of str1 is %d'%(str1,len(str1))#if没有执行的话就执行下一句
print 'done'


while True:
    num=35
    guess_num=int(raw_input('please input a number:'))
    if guess_num==num:
        print 'you guess it, congratulations'
        print 'the number is %d'%guess_num
        break
    elif guess_num < num:
        print 'no,your put is small than the right number'
    else:
        print 'no,your pur is larger than the right number'
print 'Done'


def print_max(a,b):
    global x   #global全局变量
    if a > b:
        print a,'is max'
    else:
        print b,'is max'
    x=2
    print 'x is: %d'%x

print print_max(5,10)
x=20
y=8
print print_max(x,y)


def say(message,times=3,c=5):#形参的默认值只能是在末尾,给2个默认参数值,用return返回
    #print the string is dd or not,if is ,return t
    #print perform the two function with different parameter
  
    if message =='dd':
        return message * times
        #return ('message is:%s' % message, 'times is :%d' % times, 'c is %d' % c)
    else:
        return message*(times+1)
        #print('message is:%s' %message,'times is :%d'%times,'c is %d'%c )
print say('dd',5,6)
print say('f')
print say.__doc__#.__doc__方法为打印方法文档


print 'the command line arguments are:'
for i in sys.argv:
    print i
print'\n\n the PATHONPATH is',sys.path,'\n'
a=10
print dir(sys)








m = {'a':1,'b':2,'c':3}
print m['c']
print m.keys()
print m.values()
print m.items()
'''


shoplist = ['app','banana','carrort','mongo',67]
print [str(i)for i in shoplist]#依次打印列表的字符串
str1 = ''
shoplist.append(str1)
print [str(i)for i in shoplist]#依次打印列表的字符串
d = str1.join(str(shoplist))
print str(shoplist)
print type(d)
print d

if d.startswith('a'):
    print '1执行正确，继续往下执行'
if d.find('a'):
    print '2执行正确，继续往下执行'
if 'a' in d:
    print '3执行正确，继续往下执行'

#把列表连接成字符串（join）
shoplist = ['app','banana','carrort','mongo',88]
str1=[str(i)for i in shoplist]#把列表内的值分别转换成字符串列表
str2=','.join(str1)#再把列表连接成字符串（join）
print str2



#把字符串转换成列表，用字符串方法split
print list(str2)#把字符串转成列表，只能分别打印出来
shop='app,mongo,cc'
print shop.split(',')#把字符串转换成列表，用字符串方法split
print [str(i)for i in shop]#分别打印出字符串的所有字符


for i in shoplist:
    print i
print shoplist[:]#用切片方式打印所有列表元素
print shoplist[1:2:3]#用切片步长方式打印
mylist=shoplist
del shoplist[0]
print mylist
print mylist.index('banana')
print shoplist.index('banana')
mylist=shoplist[:]#列表切片赋值给其他对象，切片这种方式能使赋值后的变量不受之前的影响，操作切片后的列表对复制的对象列表没有影响，其他对象不会改变
del shoplist[0]
print mylist
print shoplist.index('carrort')
print mylist.index('carrort')




