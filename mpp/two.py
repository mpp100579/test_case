# -*- coding:utf-8 -*-
import unittest
import one


class MyTestCase(unittest.TestCase):#测试用例类里面有初始化方法，清理退出方法，测试用例1：比较文本是否一致，测试用例2，比较文本是否一致
    # 初始化工作
    def setUp(self):
        pass

        # 退出清理工作

    def tearDown(self):
        pass

        # 具体的测试用例，一定要以test开头

    def test_Case1(self):                        #self.assertMultiLineEqual(a,b) #比较a文本与b文本是否一致，即便多了个换行，也会区分
        self.assertMultiLineEqual(one.test_login(br), u'主页')
    def test_Case2(self):
        self.assertMultiLineEqual(one.baidu2(), u'京公网安备11000002000001号')