#coding=utf-8
import cPickle as p #import pickle as p
'''
class Person:
    popuplation = 0

    def __init__(self,name):
        self.name=name
        print '初始化%s'%self.name
        Person.popuplation += 1
       #每次初始化一个实例就会增加人的数量一次#

    def __del__(self):#这个方法在对象消失的时候调用
        print '%s say bye bye'%self.name
        Person.popuplation-=1
        if Person.popuplation==0:
            print 'i am the last one'
        else:
            print 'there are still %d people left'%Person.popuplation

    def howmany(self):
        if Person.popuplation==1:
            print 'i am the only person there'
        else:
            print 'we have %d person here'%Person.popuplation

p_one = Person('')
print p_one.howmany()

p_one = Person('mpp')
print p_one.howmany()

p_one = Person('mpp1')
print p_one.howmany()

print Person.__doc__#打印类的说明

'''
#把文件/把字符串写进txt文件中，并且逐行读取出来写进txt中并且读取出来
poem = '''\
Programming is fun
When the work is done
if you wanna make your work also fun:
use Python!
'''
f = open('poem2.txt', 'w') # open for 'w'riting
f.write(poem) # write text to file
f.close() # close the file

f = file('poem2.txt')# if no mode is specified, 'r'ead mode is assumed by default
while True:
 line = f.readline()
 if len(line) == 0: # Zero length indicates EOF
    break
 print 'ok'
f.close() # close the file
#或者
file='test_poem.txt'
art='yyyyxxxx\dkkdkkkk'
f=open(file,'w')
f.write(art)
f.close()
with open(file,'r')as f:
    for line in f.readlines():
        print line

#列表序列化到txt文件中，为了在文件里储存一个对象，首先以写模式打开一个 file 对象，然后调用储存器模块的 dump 函数，把对象储存到打开的文件中
poem='''dskllkgfdlssssssssssssdgggggg356646[('dfhs'),('uuuu'),('fgsf'),566]'''
po=['ggg','hhh','jjj','kkk']
file2='test_po.txt'#假设生成的文件为test_po.txt文件给变量file
f2=open(file2,'w')#以写的模式打开此文件
p.dump(po,f2) # 把列表序列化到文件中保存，用p.dump(列表，打开的文件)
f2.write(poem)#往文件里写其他东西
f2.close()#关闭文件


#使用 pickle 模块的 load 函数的返回来取回对象。这个过程称为 取储存
del po#删除列表
f2=open(file2)#打开文件
storedlist = p.load(f2)#用p.load(打开的文件)反序列化取回对象，打印出来
print storedlist

#往txt里写东西并且追加，然后读取出来
tit='null'
f=open('test_tit.txt','w')
f.write(tit)
f.close()

t='paper pig'
f=open('test_tit.txt','a')
f.write(t)
print f #打印的是<open file 'test_tit.txt', mode 'a' at 0x00000000021D9150>
f.close()


with open('test_tit.txt','r')as f:
    for line in f.readlines():
        if line.find('null'):
            print 'd'
            break
        else:
            print 'there is empty'



#存取与取存储：
import cPickle as p #import pickle as p

shoplistfile = 'shoplist.data'  # the name of the file where we will store the object
shoplist = ['apple', 'mango', 'carrot'] # Write to the file
f = open(shoplistfile, 'w')
p.dump(shoplist, f) # dump the object to a file
f.close()

del shoplist # remove the shoplist
f = open(shoplistfile)# Read back from the storage
storedlist = p.load(f)
print storedlist
