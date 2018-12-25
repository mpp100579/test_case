#coding:utf-8


'''
count = 0
while (count < 9):
    print 'The count is:', count
    count = count + 1

print "Good bye!"

i = 1
while i < 10:
    i += 1
    if i % 2 > 0:  # 非双数时跳过输出
        continue
    print i  # 输出双数2、4、6、8、10

i = 1
while 1:  # 循环条件为1必定成立
    print i  # 输出1~10
    i += 1
    if i > 10:  # 当i大于10时跳出循环
        break

var = 1
while var == 1:  # 该条件永远为true，循环将无限执行下去
    num = raw_input("Enter a number  :")
    print "You entered: ", num

print "Good bye!"




# encoding:utf-8
class Parent(object):
    x = 1  # x是Parent类的属性(字段)

    def __init__(self):
        print 'creating Parents instance..'


class Child1(Parent):
    pass


class Child2(Parent):
    def __init__(self):
        print 'creating Child2 instance..'


class Child3(Parent):
    def __init__(self):
        Parent.__init__(self)  # 若不调用这一行,将不执行父类的构造函数
        print 'creating Child3 instance..'


class MyClass():
    def printMe(self):
        print 'gege'


if __name__ == '__main__':
    #类属性和实例属性的区别
    p = Parent()
    p.x = 11            #p.x实例属性，Parent.x类型属性
    print Parent.x, p.x    # Python也有类似Java的静态属性(类属性)，但是不用static关键字修饰,python 类中的属性若写成 "类名.属性" 形式，就是类属性，若写成"实例.属性" 形式，就是实例的属性，两者互不干扰（修改类的属性的值，不会改变实例属性的值，反之亦然）
    Parent.x = 5
    print Parent.x, p.x
    print '-------------------'



#coding:utf-8

import requests
import unittest
import time

# r=requests.get(
#     url='http://192.168.1.47:20003/GetRythonActualTimeData',
#     params={"sTime": "2018-12-06 00:00:00","eTime": "2018-12-06 00:00:00","TagNames": ["B427CBE24B28467DB0F9FE97097C2967","5433ABC8DBBA4B9E9553549B92456211","0470C088CC014714A3F19F00AB25ADDD"]})
# print r.url


r=requests.post(
    url='http://192.168.1.47:20003/GetRythonActualTimeData',
    data={"sTime": "2018-12-06 00:00:00","eTime": "2018-12-06 00:00:00","TagNames": ["B427CBE24B28467DB0F9FE97097C2967","5433ABC8DBBA4B9E9553549B92456211","0470C088CC014714A3F19F00AB25ADDD"]})
print r.json()
print u'HTTP状态码:',r.status_code

class test_one(unittest.TestCase):
    # 主构造函数
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    # 可选构造函数
    @classmethod
    def today(self):
        t = time.localtime()
        print (t.tm_year, t.tm_mon, t.tm_mday)

if __name__=='__main__':
    one=test_one(2018,12,06)
    print ("年：{year}, 月 :{month},日：{day}".format(year=2000, month=10,day=12))
    print (one.year,one.month,one.day)
    one.today()

'''
class MyTest(unittest.TestCase):  # 继承unittest.TestCase
    def tearDown(self):
        # 每个测试用例执行之后做操作
        print('测试用例执行完之后')

    def setUp(self):
        # 每个测试用例执行之前做操作
        print('测试用例执行之前操作')

    @classmethod
    def tearDownClass(self):
        # 必须使用 @ classmethod装饰器, 所有test运行完后运行一次
        print('所有测试用例执行完之后执行')

    @classmethod
    def setUpClass(self):
        # 必须使用@classmethod 装饰器,所有test运行前运行一次
        print('所有测试用例执行之前执行')

    def test_a_run(self):
        self.assertEqual(1, 1)  # 测试用例

    def test_b_run(self):
        self.assertEqual(2, 2)  # 测试用例


if __name__ == '__main__':
    unittest.main()  # 运行所有的测试用例
