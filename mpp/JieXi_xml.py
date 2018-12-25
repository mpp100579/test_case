#coding=utf-8

from lxml import etree
import re


def operationXML(xml_file, lastModparentNode, lastModChildNode=[]):
    try:
        parentNode = ""
        allChildNodes = []
        doc = etree.ElementTree(file=xml_file)
        root = doc.getroot();
        ns = getNameSpace(doc)
        if ns != None:
            parentNode = root.findall(ns + lastModparentNode, namespaces=l)
        else:
            parentNode = root.findall(lastModparentNode, namespaces=l)
        if parentNode == None or len(parentNode) == 0:
            print ("%s is emtpy" % (xml_file))

            for node_contents in parentNode:
                childNode = []
             if len(lastModChildNode) != 0:
                    for childeNode in lastModChildNode:
                        node_text = ""
                        if ns == None:
                            node_text = node_contents.find(childeNode)
                        else:
                            node_text = node_contents.find(ns + childeNode)
                        childNode.append(node_text.text)
                else:
                    for childAll in list(node_contents):
                        childNode.append(childAll.text)
                allChildNodes.append(childNode)
            print allChildNodes
    except Exception, e:
        print e


        # 根据doc获得namespaces


def getNameSpace(doc):
    ns = None
    try:
        root = doc.getroot()
        r = re.compile('({.+})')
        if r.search(root.tag) != None:
            ns = r.search(root.tag).group(1)
    except Exception, e:
        print e
    return ns


if __name__ == "__main__":
    """ 
        xml的内容如下：(目前中文会乱码 ) 
        <?xml version="1.0" encoding="UTF-8"?>  
        <employees>  
                <employee>  
                    <name>xiaozhao</name>  
                    <sex>m</sex>  
                    <age>30</age>  
                </employee>  
                <employee>  
                    <name>zhao</name>  
                    <sex>boy</sex>  
                    <age>12</age>  
                </employee>  
        </employees> 
    """
    operationXML("D:/a.xml", "employee", ["name"])



import unittest
import os
import time

from xml.dom.minidom import parse
import xml.dom.minidom
'''
#获取xml文件地址
path = os.path.abspath('.')
data_path = os.path.join(path,'data.xml') #获取xml文件地址

DOMTree = xml.dom.minidom.parse(data_path)
data = DOMTree.documentElement

def get_attrvalue(node, attrname):
     return node.getAttribute(attrname)

# style = xml中的大类 ; typename = 细分属性; typevalue = 细分属性的值; valuename = xml文件，需要获取的值的tag;
def get_data_vaule(style, typename, typevalue, valuename):
    nodelist = data.getElementsByTagName(style)

    for node in nodelist:
        if typevalue == node.getAttribute(typename):
            node_name = node.getElementsByTagName(valuename)
            value = node_name[0].childNodes[0].nodeValue
            print value
            return value
    return
'''

import xml.dom.minidom

#在内存中创建一个空的文档
doc = xml.dom.minidom.Document()
#创建一个根节点Managers对象
root = doc.createElement('Managers')
#设置根节点的属性
root.setAttribute('company', 'xx科技')
root.setAttribute('address', '科技软件园')
#将根节点添加到文档对象中
doc.appendChild(root)

managerList = [{'name' : 'joy',  'age' : 27, 'sex' : '女'},
               {'name' : 'tom', 'age' : 30, 'sex' : '男'},
               {'name' : 'ruby', 'age' : 29, 'sex' : '女'}
]

for i in managerList :
  nodeManager = doc.createElement('Manager')
  nodeName = doc.createElement('name')
  #给叶子节点name设置一个文本节点，用于显示文本内容
  nodeName.appendChild(doc.createTextNode(str(i['name'])))

  nodeAge = doc.createElement("age")
  nodeAge.appendChild(doc.createTextNode(str(i["age"])))

  nodeSex = doc.createElement("sex")
  nodeSex.appendChild(doc.createTextNode(str(i["sex"])))

  #将各叶子节点添加到父节点Manager中，
  #最后将Manager添加到根节点Managers中
  nodeManager.appendChild(nodeName)
  nodeManager.appendChild(nodeAge)
  nodeManager.appendChild(nodeSex)
  root.appendChild(nodeManager)
#开始写xml文档
fp = open(r'E:\python2.7.9\python_test\test_case\mpp\Manager.xml', 'w')   #在字符串前加r,切记切记
doc.writexml(fp, indent='\t', addindent='\t', newl='\n', encoding="utf-8")