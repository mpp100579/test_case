# -*- coding:utf-8 -*-

class Person:
    def __init__(self,age,sex):
        self.age=age
        self.sex=sex
    def set_age(self):
        self.age+=2
        return age
    def set_sex(self):
        if self.sex=='famle':
            return '女'
        else:
            return '男'


mpp1=Person(20,'famle')
print ("mpp1 的年龄是"+mpp1.age+"mpp1的性别是"+mpp1.sex)




def func(a):
    return a+1

def test_func1():
    assert func(4) == 5  # 成功示例
    print "jiafa success3"


def test_func2():
    assert func(3) == 4  # 失败示例
    print "jiafa success 4"