#coding=utf-8

import sys #sys模块，文件读写,sys 模块中其他令人感兴趣的项目有 sys.stdin、sys.stdout 和 sys.stderr 它们分别对应你的程序的标准输入、标准输出和标准错误流。
print sys.version

file ='info.txt'
def readfile(file):
 '''Print a file to the standard output.'''
f = open(file)
while True:
    line = f.readline()
    if len(line) == 0:
        break
    print 'there is not empty'
f.close()

import os #这个模块包含普遍的操作系统功能
#os.path.split()函数返回一个路径的目录名和文件名。 os.getcwd()函数得到当前工作目录，即当前 Python 脚本工作的目录路径。 os.getenv()和 os.putenv()函数分别用来读取和设置环境变量。os.listdir()返回指定目录下的所有文件和目录名。os.remove()函数用来删除一个文件。
print os.path.split('E:\python2.7.9\python_test\test_case\LX\test_po.txt')
# 删除一个已经存在的文件test2.txt
try:
    f=open('one.txt','r')
    f.close()#删除文件之前一定要记得关闭
    os.remove("one.txt")
except IOError as msg:
    print ('IO异常是%s'%msg)
    print ('meg内容为'+str(msg))
else:
    print '删除文件成功，没有异常'
finally:
    print 'Go on!'

#特殊函数方法的使用def__getitem__(self,key)
class DataBase:
    '''Python 3 中的类'''
    def __init__(self, id, address):
        '''初始化方法'''
        self.id = id
        self.address = address
        self.d = {self.id: 45, #初始化时候用一个字典把初始化参数赋值
                  self.address: "192.168.1.1",
                  }

    def __getitem__(self, key):  #在这我认为实例对象的key不管是否存在都会调用类中的__getitem__()方法。而且返回值就是__getitem__()方法中规定的return值。
        return self.__dict__.get(key, "100")
        #return self.d.get(key, "default")
        #return "hello"
data = DataBase(1, "192.168.2.11")
print data["hi"]
print data[data.id]
print data[2]



listone = [2, 3, 4]
listtwo = [2*i for i in listone if i > 2]
print listtwo
def powersum(power, *args):
    total = 0
    for i in args:
        total += pow(i, power)
    return total
print powersum(2,3,4)
print powersum(2,10)


#lambda 是表达式，语句被用来创建新的函数对象，并且在运行时返回它们。这里，我们使用了 make_repeater 函数在运行时创建新的函数对象，并且返回
#它。lambda 语句用来创建函数对象。本质上，lambda 需要一个参数，后面仅跟单个表达式作为函数体，而表达式的值被这个新建的函数返回。注意，即便是print 语句也不能用在 lambda 形式中，只能使用表达式。
def make_repeater(n):
    return lambda s: s*n
twice = make_repeater(2)
print twice('word')
print twice(5)

'''使用lambda表达式传入2个参数或者说2个对象a,b,用cmp方法比较两个对象的大小'''
class People :
  age = 0
  gender = 'male'
  def __init__ ( self , age , gender ):
    self . age = age
    self . gender = gender
  def toString ( self ):
    return 'Age:' + str(self.age ) + ' /t Gender:' + self.gender

#把所有类的对象放在一个列表里
List = [ People ( 21 , 'male' ), People ( 20 , 'famale' ), People ( 34 , 'male' ), People ( 19 , 'famale' )]
print 'Befor sort:'
for p in List :
  print p.toString ()

List.sort( lambda a,b: cmp( a.age , b.age ))#使用lambda表达式传入2个参数或者说2个对象a,b,用cmp方法比较两个对象的大小
print ' /n After ascending sort:'

for p in List :
  print p.toString ()

List.sort( lambda c,d : - cmp ( c.age ,d.age ))#使用lambda表达式传入2类个对象c,d，用cmp方法比较两个对象的大小，倒序打印出来
print ' /n After descending sort:'

for p in List :
  print p.toString ()