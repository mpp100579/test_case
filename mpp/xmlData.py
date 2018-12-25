# -*- coding:utf-8 -*-

import xml.dom.minidom  #xml.dom.minidom 模块被用来处理xml文件


# 打开xml文档
dom = xml.dom.minidom.parse('abc.xml')#parse():用于打开一个xml文件

# 得到文档元素对象,python获取catalog标签的信息
root = dom.documentElement#documentElement：用于得到dom对象的文档元素，并将获得的对象给root，每一个结点都有它的nodeName,nodeValue,nodeType属性
print root.nodeName                    #获得节点名catalog
#print root.nodeValue#获得节点值none
#print root.nodeType#获取节点类型1
#print root.ELEMENT_NODE

            #获得子标签：root.getElementByTagName
dom = xml.dom.minidom.parse('abc.xml')     #parse():用于打开一个xml文件
root = dom.documentElement               # 得到文档元素对象

bb = root.getElementsByTagName('caption')  #root.getElementByTagname()获取的是标签节点列表，
bb = bb[0]
print bb.nodeName#标签节点名.nodeName
print bb.firstChild.data#标签对的值.data

cc=dom.getElementsByTagName('caption')
c1=cc[0]
print c1.firstChild.data

bb = root.getElementsByTagName('login')
bb = bb[0]
print bb.nodeName

bb=root.getElementsByTagName('item')
bb=bb[0]
print bb.nodeName

#区分相同标签名字的标签
import xml.dom.minidom
# 打开xml文档
dom = xml.dom.minidom.parse('abc.xml')
# 获取文档元素对象
root = dom.documentElement

aa = root.getElementsByTagName('caption')
a = aa[2]
print a.nodeName
# 获取文档元素对象item
aa = root.getElementsByTagName('item')
a = aa[1]
print a.nodeName
print '*,'*80

import string
print string.center('获得标签的属性值',80,"*")#得标签的属性值
import xml.dom.minidom
# 打开xml文档
dom = xml.dom.minidom.parse('abc.xml')
# 得到文档元素对象
root = dom.documentElement
#  获取标签的属性值
itemlist = root.getElementsByTagName('login')#  获取标签的属性值列表：root.getElementsByTagName
item = itemlist[0]                            #获取标签列表的
un = item.getAttribute('username')
print un
pd = item.getAttribute('password')
print pd
cc=dom.getElementsByTagName('caption')
c1=cc[0]
print c1.firstChild.data

ii = root.getElementsByTagName('item')
i1 = ii[0]
i = i1.getAttribute('id')
print i
i2 = ii[1]
i = i2.getAttribute('id')
print i
