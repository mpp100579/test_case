# coding=utf-8

__all__ = ['A','func']#__all__=[]用列表形式把方法暴露给别人调用，在别的模块中，导入该模块时，只能导入__all__中的变量，方法和类
#是一个字符串list，用来定义模块中对于from XXX import *时要对外导出的符号，即要暴露的借口，但它只对import *起作用，对from XXX import XXX不起作用。

import sys
__import__('a')        # 导入 a.py 模块

class A():
    def __init__(self, name, age):
        self.name = name
        self.age = age


class B():
    def __init__(self, name, id):
        self.name = name
        self.id = id


def func():
    print 'func() is called!'


def func1():
    print 'func1() is called!'
