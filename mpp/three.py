# -*- coding:utf-8 -*-
import unittest
import two


def suite1():

    suite = unittest.TestSuite() # 创建测试套件1

    suite.addTest(two.MyTestCase("test_Case1"))# 为套件添加测试用例1
    return suite


def suite2():
    # 创建测试套件2
    suite = unittest.TestSuite()
    # 为套件添加测试用例2
    suite.addTest(two.MyTestCase("test_Case2"))
    return suite


def all_suite():#所有测试用例套件集合
    suite = unittest.TestSuite((suite2(), suite1()))#把所有测试套件放在一起
    return suite