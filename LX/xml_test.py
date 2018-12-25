#coding=utf-8

# -*- coding: cp936 -*-
# python 27
# xiaodeng
# python 之模块之 xml.dom.minidom解析xml
# http://www.cnblogs.com/coser/archive/2012/01/10/2318298.html
# python有三种方法解析XML，SAX，DOM，以及ElementTree




# import xml.dom
# 这里主要通过xml.dom.minidom创建xml文档，然后解析用以熟悉api
# 常用方法function()
'''
dom=xml.dom.minidom.parse(xmldemo.xml)                     #加载和读取xml文件  minidom.parse(filename)
root=dom.documentElement                                #获取xml文档对象  doc.documentElement
bb=root.getElementsByTagName(TagName)                   #获取xml节点对象集合
for i in bb:
cc=i.getAttribute(AttributeName)                       #获取xml节点属性值
type=i.getElementByTagname('type')[0]                  #获取xml节点type标签对象的具体信息
print "Type:%s" % type.childNodes[0].data              #获得文本值



minidom.parse(filename)                     #加载和读取xml文件
doc.documentElement                         #获取xml文档对象
node.getAttribute(AttributeName)            #获取xml节点属性值
node.getElementsByTagName(TagName)          #获取xml节点对象集合
node.childNodes                             #获取子节点列表
node.childNodes[index].nodeValue        #获取xml节点值
node.firstChild                             #访问第一个节点
n.childNodes[0].data                        #获得文本值
node.childNodes[index].nodeValue        #获取XML节点值


doc=minidom.parse(filename)
doc.toxml('utf-8')                          #返回Node节点的xml表示的文本




'''

# test.xml
'''
<collection shelf="New Arrivals">               # 根节点名字，collection
<movie title="Enemy Behind">                  #定位到movie元素
   <type>War, Thriller</type>
   <format>DVD</format>
   <year>2003</year>
   <rating>PG</rating>
   <stars>10</stars>
   <description>Talk about a US-Japan war</description>
</movie>
<movie title="Transformers">
   <type>Anime, Science Fiction</type>
   <format>DVD</format>
   <year>1989</year>
   <rating>R</rating>
   <stars>8</stars>
   <description>A schientific fiction</description>
</movie>
   <movie title="Trigun">
   <type>Anime, Action</type>
   <format>DVD</format>
   <episodes>4</episodes>
   <rating>PG</rating>
   <stars>10</stars>
   <description>Vash the Stampede!</description>
</movie>
<movie title="Ishtar"> movie是元素，title是元素的属性
   <type>Comedy</type>
   <format>VHS</format>
   <rating>PG</rating>
   <stars>2</stars>
   <description>Viewable boredom</description>
</movie>
</collection>
'''

# 解析案例
from  xml.dom import minidom

doc = minidom.parse('test.xml')  # parse("foo.xml")
# parseString("<foo><bar/></foo>")

# 实例化
root = doc.documentElement  # 注意没括号

# 文档对象元素
print '--' * 25            #划横线的长度
print root.nodeName  # 节点名字，collection
print root.nodeValue  # 节点的值，None
print root.nodeType  # 节点类型，1
print root.ELEMENT_NODE  # 1
print '--' * 30               #划横线的长度

# 在集合中获取所有电影
nodes = root.getElementsByTagName('movie')  # 获取xml节点对象集合

n=nodes[0]
print n
a=n.childNodes[0].nodeValue
print a
print '--' * 50              #划横线的长度


# 打印每部电影的详细信息
for n in nodes:
    # print n#<DOM Element: movie at 0x1f9d968>
    t= n.getAttribute('title')  # 获得movie元素的的title的属性值
    print t
    type = n.getElementsByTagName('type')[0] # 获取xml节点type元素的具体信息
    print "Type:%s" % type.childNodes[0].data  #获得文本值
    print '--' * 30  # 划横线的长度
    format=n.getElementsByTagName('format')[0]
    print 'format:%s'%format.childNodes[0].data



