
# coding:utf-8
data=['dsg','gsd','sdgre','yuh']
file=open('file1.txt','w')
'''
for item in data:
    file.write(item)
    file.write('\n')
print str(data)
print u'over...总共生成了{0}条数据'.format(len(data))





for i in range(len(data)):
    s = str(data[i]).replace('[','').replace(']','')#去除[],这两行按数据不同，可以选择
    s = s.replace("'",'').replace(',','')   #去除单引号，逗号，每行末尾追加换行符
    print s       #打印单个字符串
    print list(s) #打印单个字符串列表
    print ''.join(list(s))#打印列表的字符串合并的字符串，join后面只能跟list

print ''.join(data) #打印列表所有字符串,join负责将列表字符合并成一个字符串。
print str(data)      #打印列表字符串

# print ''.join(list(s))
print 'list把字符串转为列表打印'

'''


# !/usr/bin/env python
# coding=utf-8

from xlwt import *

# 需要xlwt库的支持
# import xlwt
file = Workbook(encoding='utf-8')
# 指定file以utf-8的格式打开
table = file.add_sheet('data')
# 指定打开的文件名

data = {
    "1": ["张三", 150, 120, 100],
    "2": ["李四", 90, 99, 95],
    "3": ["王五", 60, 66, 68]
}
# 字典数据

ldata = []
num = [a for a in data]
print num
# for循环指定取出key值存入num中
num.sort()
# 字典数据取出后无需，需要先排序

for x in num:
    # for循环将data字典中的键和值分批的保存在ldata中
    t = [int(x)]
    for a in data[x]:
        t.append(a)
    ldata.append(t)

for i, p in enumerate(ldata):
    # 将数据写入文件,i是enumerate()函数返回的序号数
    for j, q in enumerate(p):
        # print i,j,q
        table.write(i, j, q)
file.save('data.xlsx')
