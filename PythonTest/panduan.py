#coding:utf-8

class Student(object):
    pass
s = Student()
s.name = 'Alice'
print(s.name) #result Alice

def set_age(self, age): # 定义一个函数作为实例方法
    self.age = age
from types import MethodType
s.set_age = MethodType(set_age, s) # 给实例绑定一个方法
s.set_age(25) # 调用实例方法
print s.age # 测试结果








list = []   #定义一个空的列表用来存储生产的数字
for i in range(1,5):   #定义百位数
    for j in range(1,5):   #定义十位数
        for k in range(1,5):  #定义个位数
            if i != j and j !=k and i != k:
                num = i*100+j*10+k
                print(num)
                list.append(num)   #将生成的数字加入到list列表中
                result_num = len(list)   #统计列表中元素的个数
print("可以组合的个数为%d"%(result_num))


#求1+2+3+...+100（第一种）
s=0
for i in range(100):
     i=i+1
     s=s+i
print s

#求1+2+3+...+100（第三种）
print reduce(lambda x,y:x+y,range(1,101))

#交换两个变量的值
# 第一种：
a=input("please input a number a:")
b=input("please input a number b:")
if a>b:
    tmp=a #tmp变量赋值给a,再把变量a赋值给b,最后把b变量赋值给temp
    a=b
    b=tmp
print a,b


import pdb

def make_bread():
    pdb.set_trace()
    return "I don't have time"

print(make_bread())

