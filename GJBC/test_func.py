#coding=utf-8
#python 内置方法
print list(range(0,10,2))
#filter(function, iterable)filter() 函数用于过滤序列，过滤掉不符合条件的元素，返回由符合条件元素组成的新列表。
#该接收两个参数，第一个为函数，第二个为序列，序列的每个元素作为参数传递给函数进行判，然后返回 True 或 False，最后将返回 True 的元素放到新列表中。
import math

def is_sqr(x):
    return math.sqrt(x) % 1 == 0
newlist = filter(is_sqr, range(1, 101))
print(newlist)
print '---'*30

#setattr(object, name, value)setattr 函数对应函数 getatt()，用于设置属性值，该属性必须存在。
class A(object):
    n=4
a=A()
print a.n
print getattr(a,'n')#实例对象获取函数的属性值
setattr(a,'n',99)#实例对象重新设置函数的属性值
print a.n
print '---'*40

#新增了一种格式化字符串的函数 str.format()，它增强了字符串格式化的功能

print "{0} {1}".format("hello", "world")  # 设置指定位置
'hello world'
print "{1} {0} {1}".format("hello", "world")  # 设置指定位置
'world hello world'
print("网站名：{name}, 地址 {url}".format(name="菜鸟教程", url="www.runoob.com"))

# 通过字典设置参数
dic_one = {"name": "菜鸟教程", "url": "www.runoob.com"}
print("网站名：{name}, 地址 {url}".format(**dic_one))

# 通过列表索引设置参数
list_one = ['菜鸟教程', 'www.runoob.com']
print("网站名：{0[0]}, 地址 {0[1]}".format(list_one))  # "0" 是必须的
import os
print ('在 a.py 文件中 %s' % id(os))
print '__'*40

#__import__() 函数用于动态加载类和函数 。如果一个模块经常变化就可以使用 __import__() 来动态载入。
import os
print ('在 test_func.py 文件中 %s' % id(os))
print '---'*40

