# -*- coding:utf-8 -*-
import os
def foo():
    bar=['htc','samsum','hwa','apple']
    bar.append('hello')
    return bar
print foo()


s = "路飞,hjjjjjjjjjUIUIUIUIUIUIUIUIUIUIUIUIUIUI金合欢花或或或或或或或或"
s1=s.decode('utf-8')
print s1
print (u'路'+u'飞')

s2=open('1.txt','r+')
s2.write(s)
s2.close()
with open('1.txt', 'r') as f:
    for line in f.readlines():
       print(line.strip()
