# -*- coding:utf-8 -*-
import sys,os
print sys.argv #打印路径
os.system(sys.argv[0])
import sys

def readfile(filename):  #定义readfile函数，从文件中读出文件内容
    '''''''''Print a file to the standard output.'''
    f = file(filename)
    while True:
        line = f.readline()
        if len(line) == 0:
            break
        print line, # notice comma  分别输出每行内容
    f.close()
# Script starts from here
print sys.argv
if len(sys.argv) < 2:
    print 'No action specified.'
    sys.exit()
if sys.argv[1].startswith('--'):
    option = sys.argv[1][2:]
    # fetch sys.argv[1] but without the first two characters
    if option == 'version':  #当命令行参数为-- version，显示版本号
        print 'Version 1.2'
    elif option == 'help':  #当命令行参数为--help时，显示相关帮助内容
        print 'finished'


import string
import sys,os
def person():
    name=raw_input('input your name:')
    return name
    print 'name is %s'%name
    def one(name=[]):
        person()
        return one()
list=['ds','de']
one(list)
