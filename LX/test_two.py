#coding=utf-8
import json
import string
'''
a=[[1,2,3,],[4,5,6],[7,8,9,10,11]]
a[0][1]=10
a[1][2]=20
print a
#正向索引，反向索引，默认索引

b=[1,2,3,4,5,6,7,8]
print b[0:4:2]
#l = L[i:j:k]# 从0开始数，第i个元素到第j个元素的切片，间隔（步长为k），不包括L[j]
#l = L[i:] # 从i到最后一个元素的切片，包括L[i];l = L[;j]# 从第一个元素到j的切片，不包括L[j]

print b[1:2:3]
print b[:]
print b[-1:-5:-1]
print b[1::4]

dic = {"course": "我爱python"}
print dic
# 字典转化成json输出
dic1= '{"k1":123, "k2": "456", "ff":"ares"}'
dic2 = json.loads(dic1) # 根据字符串书写格式，将字符串自动转换成 字典类型
print dic2

a=[1,2,3,4,5]
b=[7,8,9]
print a+b
a.extend(b)
print a
a.append([40,'X',33])
print a
a.insert(5,'sd')
print a
del a[9][1]
print a
a.remove(1)
print a
a.pop()#列表Pop：返回最后一个元素，并从list中删除它。
print a
print 7 in a #判断元素是否在列表里返回true或者false
print 20 in a#判断元素是否在列表里,返回true或者false
print [x for x in range(1,11)]#方法1列表推导式生成一个包含1到10的列表
print range(1,11,1)#方法2用range方法

print range(1,11,2)#方法1用range，取基数
print [x for x in range(1,11) if x%2==1]#用判断表达式生成一个列表

print range(0,11,2)#方法1用range，取偶数
print [x for x in range(0,11) if x%2==0]

a=[3,2,3,4,1]
c=a.sort()#反转排序，sort方法返回值为None
if c is None:
    print 'haha'
print a

#字符串修改打印成列表
f='hjsfskl'
print id(f)
print list(f) #字符串a转换成列表
print f.replace('hj','mpp')#字符串修改
w=f.replace('hj','mpp')
print list(w)        #字符串修改后变成列表打印出来

print a[2:6]
b='fgdadddd'
print list(b)#字符串b转换成列表
d=2 #给变量d赋值
a='gjkkk'
print a.replace('jk','hh')#修改a字符串值，id位置没变
print list(a)#字符串a转换成列表值不发生改变
d=a    #把a字符串地址给变量d
print id(a)
print id(d)
print d #变量d引用的还是之前a变量值
del d #删除d的引用对a还是没有影响
print a

a=[1,3,4,'',2,7]
a[2]=3
print id(a)
d=4
d=a #把a列表地址赋值给d,
print id(d)
print d #d值也发生改变了
del d[:]#清空列表里的元素
del d #删除d的引用地址，对a没有影响 删除列表对象的引用
print a
del a[:]#清空列表里的元素
print a

def info(a):
    i=2
    b[i]='mpp'
    return b
b=[12,3,'',4]
print info(b)

b=set('dskgg')#Set为可变集合对象，frozenset()不可变集合对象
print b
b.add('python')
print b
b.update('python')
print b
print 3  not in b#判断元素是否在集合里返回true或者false
print 'k'in b



def info(a):
    a[1] =['bn',12,'p']
    c='kl'
    d=89

ab=['ds',2,'klfgld']
info(ab)
print ab
d=99
print d


#可变集合
info = set('abc')
info.add('python')##添加单个对象到集合里
print info
info.update('python')##把对象里的每个元素添加到集合里
print info
info.remove('python')
print info
a=set('abcdef')
b=set('defgh')
print a&b
print a|b

# for循环（#循环打印列表）
liststr = ['haha', 'gag', 'hehe', 'haha']
m = ['hjjjj']
for i in liststr:#如果i在包含列表中listr，就循环
    #print liststr循环打印列表值
    if i not in m:#如果i不包含在列表中m，就在m列表末尾追加i在listr中的值
        m.append(i)
print m
m = set(liststr)#把listr列表里的字符串转为集合，集合是无序不重复元素集
print list(m)#再打印转化为集合后的列表元素

# for循环（#循环打印字符串）
string = ''
str=u"追加字符"
for i in range(len(str)):#如果i在str字符串的长度范围内
    string+=str[i]
print string

#列表后面追加字符串，只有列表才能追加用append方法，先计算字符串的长度再来索引位置打印
ff =['yyy']#列表ff只有一个字符串元素
ff1='123477' #字符串ff1
for i in range(len(ff1)):#给i赋值=字符串ff1的长度范围5,再迭代，先计算字符串的长度再来索引位置打印
    ff.append(ff1[i])#在新建的列表ff后面追加字符串ff1中第i个对应的值
print i #打印ff1字符串i的长度是5
print ff[i]#打印末尾增加元素后，列表中i=5对应的值
print ff#打印末尾新增后的列表
print ff1[i]#打印字符串中i=5对应的值


print range(1,10,)
#打印字符串
x = 'runoob'
print list(x)
for i in range(len(x)):#把字符串长度坐标打印出来
    print(x[i])#根据字符串位置索引每个字母
#从1打印到100的列表
for i in range(1,50):
    print (i)
y=[ i for i in range(1,101)]
print y

print range(11,34,11)

a=['jd','tm',12333,'djkkk']
for i in range(len(a)):
    print i
    print '%d :%s'%(i,a[i])
    print (a[i])

a = ['i','am','lilei']
b = a
a[2] = 'laowang'
del a
print b

#列表操作
b = [1,2,3,4,5]
for i in range(6,9,1):
    if i not in b:
        b.append(i)
print b
b.extend([7,8])
print b
b = [1,2,3,4,5]
print b[-1:-3:-1]

if 2 in b:
    print '2 in b'
if 10 not in b:
    print '10 not in b'

b = [23,45,22,44,25,66,78]
print [m for m in b if m % 2 == 0]
print [m + 2 for m in b]

a=[('a',2),('b',3),('c',4)]
a.sort(key=lambda x:x[1])
print a
a.sort(key=lambda x:x[1],reverse=True)
print a

#字典操作
dic1={'key1':'h','key2':'c','key4':'a','key3':'haha','key5':'haha'}
dic1['ddd']=666
print dic1.keys()#直接打印字典的键值，以列表的形式
print dic1.items()#把字典的:键和值以列表的形式打印出来,并且是无序的
for x,y in dic1.items():#把列表的键x和值y迭代打印
    print x,y
key_list=dic1.keys()#把键列表赋值给变量key_list
print key_list#打印键，以列表的形式
print key_list.sort()#把键以列表的形式排序
for i in key_list:
    print i,dic1[i]#利用键表中键的唯一性，迭代打印键和值
print dic1['key2']#根据键查找对应的值打印
#根据值打印键
#search_value='haha'#查找值是'haha'对应的键
search_value='haha'
for x,y in dic1.items():
    if y==search_value:
        key_list.append(x)#如果值等于变量的值，就在键列表里追加
print key_list
print dic1.items()
print str(dic1)

#字符串操作转换
list1=['a','b','c','d']
print len(list1)
print range(len(list1))
j=[i for i in range(len(list1))]
print j
#for i in list1:
   # print i
#print tuple(list1)
#t=tuple(list1)
#print t
ls1 = ['a', 1, 'b', 2]
#ls2 = [str(i) for i in ls1]
#print ls2

str2="d,f,g,h"
for i in str2:
    print i
print str2
print str2.capitalize()#把字符串首写字母变大写
print str2.split(',')#把字符串生成字符串的列表

str1 = "(1,2,3)"
t=tuple(eval(str1))
print t
print list(eval(str1))

str = "{'a':1 ,'b':2}"
print eval(str)

ls1 = ['a', 'g', 'b', 'f']
ls2 = [str(i) for i in ls1]
print ls2
print sorted(ls1,key=string.upper)#用字符串方法排序,列表里面只能是字符串才能这样操作

str6='skdg567AF'
print len(str6)
print range(len(str6))#range函数打印长度列表
j=[i for i in str6]#用列表方式打印字符串
print j

print str6.replace('skd','guy')
print str6.split(',')#split把字符串生成字符串的列表
print sorted(str6)
print sorted(str6,reverse=True)#sorted把字符串转成列表形式从小到大排序
#isdigit（）：#判断是否都是数字组成
a=[i for i in str6 if not i.isdigit()]#用列表推导式除去字符串的中包含的数字,用列表形式[]赋值给变量a
print a
print sorted(a)#并且从低到高排序，先数字，大写字母，小写
print sorted(a,key=string.upper)#用字符串方法排序


new_list=[]#用新的列表来接收列表达式生成的列表值
for i in str6:
    if not i.isdigit():
        new_list.append(i)#新用列表来接收i的值
print new_list

str="12345dfgbhn"
print str.isdigit()
g=string.maketrans('12','rr')
print g
'''

def get_paper():
    return 'please open two window'
