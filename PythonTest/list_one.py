# coding:utf8
import os
import sys
'''
print '--*字典内容打印'*50
person = {'name': 'nn', 'age': '26', 'city': 'wuhan', 'url': 'www.baidu.com'}
person_1=[]
code=('name','nn')
print 'item()方法把字典中每对key和value组成一个元组，并把这些元组放在列表中返回'
while code not in person_1:
    # for key, value in person.items():        #返回的是key,value,item()方法把字典中每对key和value组成一个元组，并把这些元组放在列表中返回
    # print 'key=', key, '，value=', value
    # print 'key=',key, ',value=,',value           #，号属于拼接字符，依次打印
    # print "key={n},value={w}".format(n=key,w=value)

    code=person.items()
    print code
    person_1 .append(code)
    pass

# person_1 .append(person.items())
# print person_1


print '把字典转成列表以下方式：'*8
print person_1

print '字典转列表打印的是key值'
print list(person)
print '字典转列表打印的是value值'
print list(person.values())
print '字典转列表打印的是每对key和value组成一个元组的列表'
print person.items()

print '把字符串转成列表以下方式：'*8






list_3=[]
person = {'name': 'lizhong', 'age': '26', 'city': 'BeiJing', 'blog': 'www.jb51.net'}
for x in person.items():    #返回的是每一对key,value对应的元组,
    print x
    list_3 .append(x)    #用列表接收，返回的是列表
print list_3

person = {'name': 'lizhong', 'age': '26', 'city': 'BeiJing', 'blog': 'www.jb51.net'}
for x in person:   #如果纯使用for..in则只能取得每一对元素的key值
    print x




print '----列表打印3种方式'*50
array = ["a", "b", "c"]

for item in array:
    print(item)

for index in range(len(array)):
    print(str(index) + "：" + array[index])

for index, val in enumerate(array):
    print(str(index+1) + "--" + val)
#函数原型：enumerate(sequence, [start=0])  #第一个参数是指列表，元祖，字符串；第二个参数为指定索引，表示下标开始的位置，取值为1即表示下标从1开始计算，默认从0开始；意思是打印输出索引与value值

dir = {'A': 'a',
       'B': 'b'}

xq = dir.keys()
print xq
yw = dir.values()

# 这段代码是遍历两个列表之后赋值给新的两个列表
for i in xq, yw:
    answer, question = i[:]  # 这里可以加代码对元素操作之后再赋值给新的列表
    print answer ,",", question  # 你可以把这句放在for循环外面在看下结果

print "---------"
# 复杂版
for j in xq:
    answer_ = j[:]
    print answer_, ",",
print"同理如下"
b=[x[0] for x in yw]
print b

print('多维数组打印------------------')
import numpy as np
a = np.array([[1,2,3], [4,5,6], [7,8,9]])
print(a[: ,2]) #找出下表为2的所有元素
print(a[:2])# 找到0 - 1的元素，第一列和第二列

list1 = ['1', '1']
list2 = ['A','B']
print list1 +list2
for x in list1, list2:
    reslut = x[:]        #列表切片，如果冒号：左边或者右边没有任何东西，那么这时候代表全体
    print reslut
c=[x[:] for x in list1,list2]
print "c is this caculate++=++++"
print c



print '读取txt中文序号和内容；'*3
with open("log.txt", "r") as f:
    index = 0
    for line in f.readlines():
        index=index+1
        line = line.strip('')  #去掉列表中每一个元素的换行符
        # print line
        # print type(line)
        print('({0},{1})'.format(index, line))
        # print (line.encode('utf-8'))


print '方式二：txt中文读取序号和内容'
for index, line in enumerate(open("log.txt",'r')):
    print('({0},{1})'.format(index, line)) #用格式化打印


print 'txt追加中文字符；'*3
Name=u'wee更多的多多多多'
Name1 = Name.encode('utf-8')
with open("log.txt", "a") as f:
    f.write(Name1)

print       '元祖中文打印用这种方式  decode是把其他编码的字符串转换成 Unicode 编码；'*3
tuple1 = ('小甲鱼', '耐克', '李宁', '香奈儿')
#方法三直接去掉转义字符\,然后打印出来
lstring = str(tuple1).decode('string_escape')
print lstring

#字典中文打印用这种方式
dict6 = {1:'淘宝', 2:'京东', 3:'天猫', 4:'1号店', 5:'美团'}
lstring = str(dict6).decode('string_escape')
print lstring

#列表中文打印
list_1=['dsg','四达刚发的','yr突然突然']
list_2= str(list_1).decode('string_escape')
print list_2





import cPickle as p
shoplistfile = 'shoplist.data'
shoplist = ['apple', 'mango', 'carrot']
f = file(shoplistfile, 'w')
p.dump(shoplist, f) # dump the object to a file
f.close()
del shoplist
f = file(shoplistfile)
storedlist = p.load(f)
print storedlist

'''
s1='jskdllkd'
d1=list(s1)
print d1


#中文字符串打印
str_1='大神看到烦付付付付付付付付付付付sddddddddd'
print str_1

print 'Python 将列表数据写入txt文件,*******************************write参数是字符串'
def text_save(filename, data):#filename为写入CSV文件的路径，data为要写入数据列表.
    file = open(filename,'a')
    i=0
    for i in range(len(data)):
        s = str(data[i]).replace('[','').replace(']','')#去除[],这两行按数据不同，可以选择
        s = s.replace("'",'').replace(',','') +'\n'   #去除单引号，逗号，每行末尾追加换行符
        file.write(s)
    print u'over...总共生成了{num}条数据'.format(num=len(s))
    file.close()
    print("保存文件成功")


import os
import sys
import xlwt
print 'Python 将列表数据写入excel文件'

#  将数据写入新文件
def data_write(file_path, datas):
    f = xlwt.Workbook()
    sheet1 = f.add_sheet(u'sheet1', cell_overwrite_ok=True)  # 创建sheet
    # 将数据写入第 i 行，第 j 列
    i = 0
    for data in datas:
        for j in range(len(data)):
            sheet1.write(i, j, data[j])
        i = i + 1
    f.save(file_path)  # 保存文件


if __name__=='__main__':
    list_4=['sdfj','435','325','sdg',["df","dft","dfg"]]
    text_save('2.txt',list_4)
    data_write('2.xlsx',list_4)


f=open('info_1.txt','w')
for i in range(0,500):
    f.write(bytes(i))



